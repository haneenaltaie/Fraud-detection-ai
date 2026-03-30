import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Fraud Detection AI System",
    page_icon="💳",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("💳 Fraud Detection AI System")
st.markdown("### Machine Learning Model for Detecting Suspicious Financial Transactions")

st.write(
    "This application predicts whether a financial transaction is likely to be **fraudulent** "
    "based on transaction details such as amount, account balances, and transaction type."
)

st.markdown("---")

# -----------------------------
# Load Model
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "..", "models", "fraud_model.pkl")

if not os.path.exists(model_path):
    st.error(f"Model file not found at: {model_path}")
else:
    model = joblib.load(model_path))

    st.subheader("📌 Enter Transaction Details")

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

    st.markdown("---")

    # -----------------------------
    # Prediction
    # -----------------------------
    if st.button("🔍 Predict Fraud"):
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
        prediction_proba = model.predict_proba(input_data)[0][1]

        st.subheader("📊 Prediction Result")

        if prediction == 1:
            st.error("⚠️ This transaction is predicted as **FRAUD**.")
        else:
            st.success("✅ This transaction is predicted as **NOT FRAUD**.")

        st.metric("Fraud Probability", f"{prediction_proba:.2%}")

        st.markdown("---")
        st.info("This prediction is based on the trained Random Forest machine learning model.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("### 📘 Project Summary")
st.write(
    "This project was developed using **Python, Scikit-learn, Pandas, and Streamlit** "
    "to demonstrate an end-to-end machine learning workflow for fraud detection."
)