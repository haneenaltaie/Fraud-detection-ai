import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Fraud Detection AI System", layout="centered")

st.title("Fraud Detection AI System")
st.subheader("Machine Learning App for Detecting Suspicious Transactions")

st.write("Enter transaction details below to predict whether a transaction is fraudulent or not.")

# -----------------------------
# Load Model
# -----------------------------
model_path = "models/fraud_model.pkl"

if not os.path.exists(model_path):
    st.error("Model file not found. Please make sure fraud_model.pkl is in the same folder.")
else:
    model = joblib.load(model_path)

    # -----------------------------
    # User Inputs
    # -----------------------------
    step = st.number_input("Step", min_value=1, value=1)

    type_options = {
        "CASH_IN": 0,
        "CASH_OUT": 1,
        "DEBIT": 2,
        "PAYMENT": 3,
        "TRANSFER": 4
    }
    transaction_type = st.selectbox("Transaction Type", list(type_options.keys()))
    type_encoded = type_options[transaction_type]

    amount = st.number_input("Amount", min_value=0.0, value=1000.0)
    oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0, value=5000.0)
    newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0, value=4000.0)
    oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0, value=0.0)
    newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0, value=1000.0)
    isFlaggedFraud = st.selectbox("Flagged Fraud", [0, 1])

    # -----------------------------
    # Prediction
    # -----------------------------
    if st.button("Predict Fraud"):
        input_data = pd.DataFrame([{
            'step': step,
            'type': type_encoded,
            'amount': amount,
            'oldbalanceOrg': oldbalanceOrg,
            'newbalanceOrig': newbalanceOrig,
            'oldbalanceDest': oldbalanceDest,
            'newbalanceDest': newbalanceDest,
            'isFlaggedFraud': isFlaggedFraud
        }])

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("This transaction is predicted as FRAUD.")
        else:
            st.success("This transaction is predicted as NOT FRAUD.")