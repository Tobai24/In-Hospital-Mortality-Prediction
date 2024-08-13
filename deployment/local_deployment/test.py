import requests
import pandas as pd

# Your dictionary
data = {
    'age': 78,
    'BMI': 37.851434,
    'atrialfibrillation': 0,
    'Systolic blood pressure': 95.444444,
    'Diastolic blood pressure': 60.259259,
    'diabetes': 1,
    'Respiratory rate': 21.75,
    'temperature': 36.12037,
    'SP O2': 94.384615,
    'Urine output': 1766.0,
    'PT': 14.2,
    'INR': 1.2,
    'Anion gap': 12.545455,
    'PCO2': 52.0,
    'PH': 7.333333,
    'Bicarbonate': 26.363636,
    'NT-proBNP': 24440.0,
    'Creatine kinase': 24.0,
    'Creatinine': 1.3,
    'Urea nitrogen': 32.727273,
    'outcome': 1.0,
    'Hypertensive': False,
    'age_group': 'elderly',
    'BMI_category': 'obese'
}

# Convert the dictionary to a list of dictionaries (JSON serializable format)
data_list = [data]

# URL of the endpoint
url = "http://localhost:9696/predict"

# Send the request
response = requests.post(url, json=data_list)

# Print the response
print(response.json())
