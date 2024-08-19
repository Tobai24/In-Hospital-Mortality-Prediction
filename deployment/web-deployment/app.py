import streamlit as st
import pandas as pd
import pickle

# Load the saved model
with open("model.pkl", "rb") as f_in:
    model = pickle.load(f_in)

# Define a prediction function
def predict(features):
    preds = model.predict(features)
    return preds

# Streamlit app
st.title("🩺 In-Hospital Mortality Prediction")

# Description
st.markdown("""
## About This App 📝

This application is designed to predict the likelihood of in-hospital mortality based on various clinical and patient data. 
By entering the relevant medical parameters, the model will provide a prediction, helping healthcare providers make more informed decisions.

The app is particularly useful for early identification of high-risk patients, enabling timely intervention and potentially saving lives.

**Please note:** This app is intended for experimental purposes only and should not be used to make clinical decisions. 
The predictions provided are not a substitute for professional medical advice and should be interpreted with caution. 
The tool aims to assist in research and understanding but is not validated for clinical use.

""")

# Input features
st.sidebar.header("Enter Patient Data 🧑‍⚕️")

# Streamlit sidebar inputs
data = {
    'age': st.sidebar.number_input('Age', min_value=0, step=1),  
    'BMI': st.sidebar.number_input('BMI', min_value=0.0, step=0.1),  
    'atrialfibrillation': st.sidebar.selectbox('Atrial Fibrillation', [1, 0], format_func=lambda x: 'Yes' if x == 1 else 'No'),
    'Systolic blood pressure': st.sidebar.number_input('Systolic Blood Pressure', min_value=70, max_value=300, step=1), 
    'Diastolic blood pressure': st.sidebar.number_input('Diastolic Blood Pressure', min_value=40, max_value=200, step=1),  
    'diabetes': st.sidebar.selectbox('Diabetes', [1, 0], format_func=lambda x: 'Yes' if x == 1 else 'No'),
    'Respiratory rate': st.sidebar.number_input('Respiratory Rate', min_value=6, max_value=60, step=1),  
    'temperature': st.sidebar.number_input('Temperature', min_value=95.0, max_value=104.0, step=0.1),  
    'SP O2': st.sidebar.number_input('SP O2', min_value=0.0, max_value=100.0, step=0.1), 
    'Urine output': st.sidebar.number_input('Urine Output', min_value=0.0, step=0.1),  
    'PT': st.sidebar.number_input('PT', min_value=0.0, step=0.1), 
    'INR': st.sidebar.number_input('INR', min_value=1.0, max_value=5.0, step=0.1),  
    'Anion gap': st.sidebar.number_input('Anion Gap', min_value=0.0, step=0.1), 
    'PCO2': st.sidebar.number_input('PCO2', min_value=20.0, max_value=60.0, step=0.1),  
    'PH': st.sidebar.number_input('PH', min_value=6.8, max_value=7.8, step=0.01), 
    'Bicarbonate': st.sidebar.number_input('Bicarbonate', min_value=15.0, max_value=30.0, step=0.1),  
    'NT-proBNP': st.sidebar.number_input('NT-proBNP', min_value=0.0, step=1.0),  
    'Creatine kinase': st.sidebar.number_input('Creatine Kinase', min_value=0.0, step=1.0),  
    'Creatinine': st.sidebar.number_input('Creatinine', min_value=0.0, step=0.01),  
    'Urea nitrogen': st.sidebar.number_input('Urea Nitrogen', min_value=0.0, step=0.1), 
    'outcome': st.sidebar.number_input('Outcome', min_value=0.0, step=1.0),
    'Hypertensive': st.sidebar.selectbox('Hypertensive', [1, 0], format_func=lambda x: 'Yes' if x == 1 else 'No'),
    'age_group': st.sidebar.selectbox('Age Group', ['elderly', 'middle-aged', 'young']),  
    'BMI_category': st.sidebar.selectbox('BMI Category', ['normal', 'overweight', 'obese'])  
}



# Predict button
if st.button("🔍 Predict"):
    # Convert the inputs to a DataFrame
    input_df = pd.DataFrame([data])
    
    # Get prediction
    prediction = predict(input_df)
    result = "deceased" if prediction >= 0.6 else "survive"

    # Display the prediction
    st.subheader("Prediction Result")
    st.write(f"The patient is likely to be **{result}**.")

