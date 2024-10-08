import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(df, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here

    X = df.drop('outcome', axis=1)
    y = df['outcome']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    logged_model = 'runs:/2d5714f01af742d7b7884d2381d43b1b/Logistic Regression'

    # Load model as a PyFuncModel.
    loaded_model = mlflow.pyfunc.load_model(logged_model)

    Log_reg = mlflow.sklearn.load_model(logged_model)

    y_pred = Log_reg.predict(X_test)

    return y_pred



