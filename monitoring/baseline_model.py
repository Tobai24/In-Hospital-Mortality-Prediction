import pandas as pd
from datetime import datetime, timedelta
import requests
import random
import logging 
import uuid
import pytz
import io
import psycopg
import pickle
import time
from tqdm import tqdm
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metrics import ColumnDriftMetric, DatasetDriftMetric, DatasetMissingValuesMetric
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")

SEND_TIMEOUT = 10
rand = random.Random()

create_table_statement = """
drop table if exists dummy_metrics;
create table dummy_metrics(
	timestamp timestamp,
	prediction_drift float,
	num_drifted_columns integer,
	share_missing_values float
)
"""

data = pd.read_csv('../data/processed_df.csv')


data = data.dropna(subset=['outcome'])

# Separate features and target variable
X = data.drop('outcome', axis=1)
y = data['outcome']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


if isinstance(X_train, pd.DataFrame):
    df_train = X_train.copy()
else:
    # Convert X_train to DataFrame if it's a NumPy array
    df_train = pd.DataFrame(X_train, columns=[f'feature_{i}' for i in range(X_train.shape[1])])

# Add the target values to the DataFrame
df_train['outcome'] = y_train.values

if isinstance(X_test, pd.DataFrame):
    df_test = X_test.copy()
else:
    # Convert X_train to DataFrame if it's a NumPy array
    df_train = pd.DataFrame(X_test, columns=[f'feature_{i}' for i in range(X_train.shape[1])])

# Add the target values to the DataFrame
df_test['outcome'] = y_test.values

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Identify categorical and numerical columns
categorical_features = X.select_dtypes(include=['object']).columns
numerical_features = X.select_dtypes(exclude=['object']).columns

# Create preprocessing pipelines
numeric_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')), 
    ('scaler', StandardScaler())  # Add the StandardScaler here
])

categorical_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),  
    ('onehot', OneHotEncoder(handle_unknown='ignore')), 
])

# Combine pipelines into a single ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_pipeline, numerical_features),
        ('cat', categorical_pipeline, categorical_features)
    ]
)

# Create the final pipeline with preprocessing and logistic regression
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=6000))
])



pipeline.fit(X_train, y_train)


# Make predictions
train_pred = pipeline.predict(X_train)

df_train['prediction'] = train_pred


test_pred = pipeline.predict(X_test)

df_test['prediction'] = test_pred


with open("models/model.pkl", "wb") as f_out:
    pickle.dump(pipeline, f_out)



column_mapping = ColumnMapping(
    target=None,
    prediction='prediction',
    #numerical_features=numerical_features,
    #categorical_features=categorical_features
)



report = Report(metrics=[
    ColumnDriftMetric(column_name='prediction'),
    DatasetDriftMetric(),
    DatasetMissingValuesMetric()
]
)


def prep_db():
	with psycopg.connect("host=localhost port=5432 user=postgres password=example", autocommit=True) as conn:
		res = conn.execute("SELECT 1 FROM pg_database WHERE datname='test'")
		if len(res.fetchall()) == 0:
			conn.execute("create database test;")
		with psycopg.connect("host=localhost port=5432 dbname=test user=postgres password=example") as conn:
			conn.execute(create_table_statement)


def calculate_metrics_postgresql(curr, i):
	current_data = df_train

	#current_data.fillna(0, inplace=True)
	current_data['prediction'] = pipeline.predict(current_data.fillna(0))

	report.run(reference_data = df_test, current_data = current_data,
		column_mapping=column_mapping)

	result = report.as_dict()

	prediction_drift = result['metrics'][0]['result']['drift_score']
	num_drifted_columns = result['metrics'][1]['result']['number_of_drifted_columns']
	share_missing_values = result['metrics'][2]['result']['current']['share_of_missing_values']

	curr.execute(
		"insert into dummy_metrics(timestamp, prediction_drift, num_drifted_columns, share_missing_values) values (%s, %s, %s, %s)",
		((datetime.now() + timedelta(days=i), prediction_drift, num_drifted_columns, share_missing_values))
	)
 


def batch_monitoring_backfill():
	prep_db()
	last_send = datetime.now() - timedelta(seconds=10)
	with psycopg.connect("host=localhost port=5432 dbname=test user=postgres password=example", autocommit=True) as conn:
		for i in range(0, 27):
			with conn.cursor() as curr:
				calculate_metrics_postgresql(curr, i)

			new_send = datetime.now()
			seconds_elapsed = (new_send - last_send).total_seconds()
			if seconds_elapsed < SEND_TIMEOUT:
				time.sleep(SEND_TIMEOUT - seconds_elapsed)
			while last_send < new_send:
				last_send = last_send + timedelta(seconds=10)
			logging.info("data sent")

if __name__ == '__main__':
	batch_monitoring_backfill()