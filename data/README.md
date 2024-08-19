# 📊 Dataset Overview

## About the Dataset

This project uses a dataset sourced from Kaggle for predicting in-hospital mortality, focusing on ICU patient data. The original dataset contained **51 columns**, but I reduced it to **24 columns** for ease of use and to focus on the most relevant clinical features. The reduced dataset is stored in the `processed_data.csv` file in this directory.

- **Number of records**: 1,178 ICU stays
- **Original number of features**: 51 columns  
- **Reduced number of features**: 24 columns

### 🔗 Original Dataset Link

The original dataset can be found here:

- [Download Original Dataset from Kaggle](https://www.kaggle.com/datasets/saurabhshahane/in-hospital-mortality-prediction)

### 🎯 Target Column

- **Outcome**: This is the target column representing the in-hospital mortality outcome.
  - **0**: Patient survived.
  - **1**: Patient deceased.

### 🧬 Column Descriptions

Below is a detailed description of the **24 columns** used in this project (found in `processed_data.csv`):

| Column Name               | Description                                                                                  |
|---------------------------|----------------------------------------------------------------------------------------------|
| `age`                      | Age of the patient (in years).                                                               |
| `BMI`                      | Body Mass Index, calculated from height and weight (kg/m²).                                  |
| `atrialfibrillation`       | Indicator of whether the patient has atrial fibrillation (1 for Yes, 0 for No).              |
| `Systolic blood pressure`  | Systolic blood pressure (in mmHg).                                                           |
| `Diastolic blood pressure` | Diastolic blood pressure (in mmHg).                                                          |
| `diabetes`                 | Indicator of whether the patient has diabetes (1 for Yes, 0 for No).                         |
| `Respiratory rate`         | Number of breaths per minute.                                                                |
| `temperature`              | Body temperature (in °C).                                                                    |
| `SP O2`                    | Oxygen saturation level (%).                                                                 |
| `Urine output`             | Volume of urine output (in milliliters).                                                     |
| `PT`                       | Prothrombin time (in seconds), measures blood clotting.                                      |
| `INR`                      | International Normalized Ratio, standardized prothrombin time value.                         |
| `Anion gap`                | Difference between measured cations and anions in serum (in mmol/L).                         |
| `PCO2`                     | Partial pressure of carbon dioxide (in mmHg), indicates respiratory function.                |
| `PH`                       | Blood pH level, indicating acidity or alkalinity of the blood.                               |
| `Bicarbonate`              | Bicarbonate levels in the blood (in mmol/L), relates to the body's acid-base balance.        |
| `NT-proBNP`                | N-terminal pro b-type natriuretic peptide (in pg/mL), a marker for heart failure.            |
| `Creatine kinase`          | Creatine kinase enzyme level (in U/L), indicative of muscle damage or stress.                |
| `Creatinine`               | Creatinine level (in mg/dL), used to assess kidney function.                                 |
| `Urea nitrogen`            | Blood urea nitrogen (in mg/dL), another indicator of kidney function.                        |
| `outcome`                  | The target variable representing the patient's in-hospital mortality outcome.                |
| `Hypertensive`             | Indicator of whether the patient has a history of hypertension (True for Yes, False for No). |
| `age_group`                | Categorical grouping of the patient’s age into different ranges.                             |
| `BMI_category`             | Categorical grouping of BMI into different ranges (e.g., underweight, normal, overweight).   |

---

## Usage

Before using this dataset, make sure to download the original dataset from the Kaggle link above, and also use the reduced version (`processed_data.csv`) for analysis. The reduced dataset focuses on the critical features for predicting in-hospital mortality. For detailed preprocessing steps, refer to the code provided in the `notebooks/` directory.
