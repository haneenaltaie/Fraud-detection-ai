# Fraud Detection AI System

## Overview
This project is a machine learning-based fraud detection system designed to identify suspicious financial transactions. The model was built using Python and trained on transaction data containing financial behavior patterns such as transaction amount, account balances, and transfer types.

An interactive Streamlit application was also developed to allow users to test transaction inputs and predict whether a transaction is likely fraudulent or not.

---

## Objectives
- Detect potentially fraudulent financial transactions
- Build and evaluate a machine learning classification model
- Create an interactive fraud prediction dashboard
- Demonstrate practical AI and data science skills using a real-world inspired dataset

---

## Dataset
The dataset used in this project contains transaction-level financial data with the following key features:

- `step`
- `type`
- `amount`
- `oldbalanceOrg`
- `newbalanceOrig`
- `oldbalanceDest`
- `newbalanceDest`
- `isFlaggedFraud`
- `isFraud` (Target Variable)

### Target Variable
- `0` = Not Fraud
- `1` = Fraud

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

## Project Structure
```bash
fraud-detection-ai-project/
│
├── data/
│   └── Fraud.csv
│
├── notebooks/
│   └── fraud_detection_model.ipynb
│
├── app/
│   └── streamlit_app.py
│
├── models/
│   └── fraud_model.pkl
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore