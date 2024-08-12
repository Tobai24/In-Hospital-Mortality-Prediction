import mlflow
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import numpy as np
import mlflow.sklearn



if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        df: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    X = df.drop('outcome', axis=1)
    y = df['outcome']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    categorical_features = X_train.select_dtypes(include=['object']).columns
    numerical_features = X_train.select_dtypes(exclude=['object']).columns

    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment("mlflow_runs")

    # Enable MLflow autologging
    mlflow.sklearn.autolog()

    # Define preprocessing for numerical and categorical data
    numeric_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean'))
    ])

    categorical_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),  
        ('onehot', OneHotEncoder(handle_unknown='ignore')) 
    ])

    # Combine preprocessing pipelines
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_pipeline, X.select_dtypes(include=['float64']).columns),
            ('cat', categorical_pipeline, X.select_dtypes(include=['object']).columns)
        ]
    )

    # Define different models
    models = {
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Support Vector Classifier": SVC(probability=True, random_state=42),
        "Logistic Regression": LogisticRegression(max_iter=200, random_state=42)
    }

    # Train and log each model
    for model_name, model in models.items():
        with mlflow.start_run(run_name=model_name):
            # Create a pipeline with preprocessing and the model
            pipeline = Pipeline([
                ('preprocessor', preprocessor),
                ('classifier', model)
            ])

            # Train the model
            pipeline.fit(X_train, y_train)

            # Make predictions
            predictions = pipeline.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            precision, recall, f1, _ = precision_recall_fscore_support(y_test, predictions, average='weighted')
            
            mlflow.log_metric("accuracy", accuracy)
            mlflow.log_metric("precision", precision)
            mlflow.log_metric("recall", recall)
            mlflow.log_metric("f1_score", f1)
            
            mlflow.sklearn.log_model(pipeline, model_name)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'