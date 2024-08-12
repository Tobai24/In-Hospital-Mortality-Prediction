import pandas as pd 
import requests
import io

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    url = "https://raw.githubusercontent.com/Tobai24/In-Hospital-Mortality-Prediction/main/data/dataset.csv"

    # Get the content of the file
    response = requests.get(url)

    # Raise an error if the request was unsuccessful
    response.raise_for_status()

    # Load the CSV content into a DataFrame
    df = pd.read_csv(io.StringIO(response.text))

    # Return the DataFrame (assuming this is within a function)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'