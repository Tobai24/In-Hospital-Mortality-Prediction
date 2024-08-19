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
    'age': st.sidebar.number_input('Age', min_value=0, step=1),  # Whole numbers only, no negative values
    'BMI': st.sidebar.number_input('BMI', min_value=0.0, step=0.1),  # Allow decimal values for BMI
    'atrialfibrillation': st.sidebar.selectbox('Atrial Fibrillation', [0, 1]),
    'Systolic blood pressure': st.sidebar.number_input('Systolic Blood Pressure', min_value=0),
    'Diastolic blood pressure': st.sidebar.number_input('Diastolic Blood Pressure', min_value=0),
    'diabetes': st.sidebar.selectbox('Diabetes', [0, 1]),
    'Respiratory rate': st.sidebar.number_input('Respiratory Rate', min_value=0.0),
    'temperature': st.sidebar.number_input('Temperature', min_value=0.0),
    'SP O2': st.sidebar.number_input('SP O2', min_value=0.0),
    'Urine output': st.sidebar.number_input('Urine Output', min_value=0.0),
    'PT': st.sidebar.number_input('PT', min_value=0.0),
    'INR': st.sidebar.number_input('INR', min_value=0.0),
    'Anion gap': st.sidebar.number_input('Anion Gap', min_value=0.0),
    'PCO2': st.sidebar.number_input('PCO2', min_value=0.0),
    'PH': st.sidebar.number_input('PH', min_value=0.0),
    'Bicarbonate': st.sidebar.number_input('Bicarbonate', min_value=0.0),
    'NT-proBNP': st.sidebar.number_input('NT-proBNP', min_value=0.0),
    'Creatine kinase': st.sidebar.number_input('Creatine Kinase', min_value=0.0),
    'Creatinine': st.sidebar.number_input('Creatinine', min_value=0.0),
    'Urea nitrogen': st.sidebar.number_input('Urea Nitrogen', min_value=0.0),
    'outcome': st.sidebar.number_input('Outcome', min_value=0.0),
    'Hypertensive': st.sidebar.selectbox('Hypertensive', [0, 1]),  
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

