import requests
import pandas as pd

# Your dictionary
data = {
    'Anion gap': 0.229676, 'Urea nitrogen': 0.203024, 'INR': 0.144444, 'PT': 0.140299, 'NT-proBNP': 0.121075, 
    'Respiratory rate': 0.117015, 'atrialfibrillation_1': 0.100975, 'Creatine kinase': 0.076656, 
    'age': 0.06451, 'Creatinine': 0.046717, 'age_group_elderly': 0.032525, 'Creatine kinase_log': 0.014424, 
    'BMI_category_overweight': 0.008752, 'BMI_category_normal': -0.005249, 'age_BMI': -0.019846, 
    'age_group_middle-aged': -0.035927, 'PCO2': -0.049517, 'diabetes_1': -0.049997, 'BMI': -0.062086, 
    'Hypertensive': -0.068562, 'SP O2': -0.071189, 'Diastolic blood pressure': -0.087403, 
    'temperature': -0.092861, 'BMI_category_obese': -0.096868, 'Systolic blood pressure': -0.132857, 
    'PH': -0.150611, 'Urine output': -0.173135, 'Bicarbonate': -0.22265
}

# Convert the dictionary to a list of dictionaries (JSON serializable format)
data_list = [data]

# URL of the endpoint
url = "http://localhost:9696/predict"

# Send the request
response = requests.post(url, json=data_list)

# Print the response
print(response.json())
