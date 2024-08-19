# In-Hospital Mortality Prediction

## Description
This project aims to develop an end-to-end machine learning pipeline for predicting in-hospital mortality using various tools and technologies, including MLflow, Mage, Docker, Google Cloud, Evidently AI, Grafana, and more. The goal is to build a reliable and scalable system for monitoring and predicting patient outcomes based on medical data.

### Problem
The primary objective is to predict the likelihood of in-hospital mortality for patients based on their medical records and clinical data. Early prediction can help healthcare providers take necessary actions to improve patient outcomes and allocate resources effectively.

### Objective
Develop and deploy a machine learning model to predict in-hospital mortality.
Implement a robust and scalable MLOps pipeline for continuous integration and delivery.
Monitor model performance and ensure accuracy over time.

### Dataset
The dataset used for this project is named "In-Hospital-Mortality-Prediction." It consists of medical records and clinical data for patients. The target column is outcome, which indicates whether the patient survived or not.

## Columns and Their Descriptions
1. patient_id: Unique identifier for each patient.
2. age: Age of the patient.
3. gender: Gender of the patient (e.g., Male, Female).
4. admission_type: Type of hospital admission (e.g., Emergency, Elective).
5. diagnosis: Primary diagnosis for the patient.
6. comorbidities: List of comorbid conditions.
7. length_of_stay: Duration of the hospital stay (in days).
8. icu_admission: Whether the patient was admitted to the ICU (Yes/No).
9. ventilation: Whether the patient required mechanical ventilation (Yes/No).
10. heart_rate: Heart rate of the patient at admission.
11. blood_pressure: Blood pressure of the patient at admission.
12. respiratory_rate: Respiratory rate of the patient at admission.
13. temperature: Body temperature of the patient at admission.
14. outcome: Target variable indicating the outcome (0 for survived, 1 for mortality).

## Tools & Technologies
- **Cloud:** [Google Cloud SDK](https://cloud.google.com/sdk)
- **Virtual Machine:** [Google Compute Engine](https://cloud.google.com/compute)
- **Containerization:** [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- **Orchestration:** [Mage](https://mage.ai/)
- **Experiment Tracking and Model Management:** [MLflow](https://mlflow.org/)
- **Model Artifacts Storage:** [Google Cloud Storage](https://cloud.google.com/storage)
- **Streaming Model Deployment:** [Google Cloud Functions](https://cloud.google.com/functions)
- **Container Storage:** [Google Container Registry](https://cloud.google.com/container-registry)
- **Model Monitoring:** [Evidently AI](https://evidently.ai/) and [Grafana](https://grafana.com/)
- **Language:** [Python](https://www.python.org/)
- **Web Application Framework:** [Streamlit](https://streamlit.io/)

**Warning:** Following the steps of what's in here may cost you money (Google Cloud is a paid service), be sure to shut down any Google Cloud service you no longer need to use to avoid charges.

### Architecture
The architecture of the project is designed to ensure seamless integration and automation of various components, from data ingestion to model deployment and monitoring. The diagram below illustrates the overall architecture:

![architecture](images/architecture.png)


### Exploratory Data Analysis and Modeling
The exploratory data analysis and modeling is done in the notebooks directory. The exploratory data analysis is done in the analysis.ipynb notebook. The modeling is done in the modeling.ipynb notebook.

### Setup
**Warning (again):** Using Google Cloud services costs money. If you don't have credits (you get $300USD when you first sign up), you will be charged. Delete and shutdown your work when finished to avoid charges.

### Pre-requisites
If you already have a Goggle Cloud account, you can skip the pre-requisite steps.
- - Google Cloud: [Google Cloud Account and Access Setup](setup/1_google_cloud.md)

# to use the local docker deployment
```bash
docker build -t mortality-prediction:v1 .
docker run -it -p 9696:9696 mortality-prediction:v1
```

# to check the local streamlit deployment
```bash
docker build -t streamlit-app .
docker run -p 8501:8501 streamlit-app
```

# to run the the stramlit app from the cloud
```bash
streamlit run app.py --server.port 8501 --server.enableCORS false --server.enableXsrfProtection false
```



# Predicting In-Hospital Mortality 🏥

Hello there! 👋 Welcome to my end-to-end machine learning project, where I’m tackling the important task of predicting in-hospital mortality. The goal of this project is to build a reproducible machine learning pipeline, from data preprocessing to model deployment, ensuring you can easily replicate every step on your own machine or cloud environment. 🏗️🚀

## 📝 Problem Description

Hospital readmissions and mortality are pressing challenges in healthcare today. The ability to predict in-hospital mortality can be crucial for better patient management and improving outcomes. 

### Objective

The objective of this project is to develop a machine learning model that can accurately predict the likelihood of a patient’s mortality during their hospital stay. The goal is to provide healthcare professionals with valuable insights that can potentially save lives.

### Dataset

The dataset I used for this project comes from the [PhysioNet Challenge 2012](https://physionet.org/content/challenge-2012/1.0.0/), which provides a rich collection of ICU data for predicting in-hospital mortality. This dataset contains a wide range of physiological measurements and clinical information collected over the first 48 hours of a patient's ICU stay.

- **Number of records**: 1178 ICU stays
- **Number of features**: 51 columns

The dataset is hosted on PhysioNet and can be downloaded [here](https://physionet.org/content/challenge-2012/1.0.0/). For more detailed information about the dataset, including explanations of the columns, please refer to the [`data/README.md`](data/README.md).



