# Fraud Detection AI System

A machine learning app that detects suspicious financial transactions, with an interactive Streamlit dashboard for real-time fraud prediction.

---

## Live Demo

Enter transaction details → get an instant fraud prediction via a trained Random Forest model.

> **App built with:** Python · scikit-learn · Streamlit · pandas · Jupyter

---

## Results

| Metric | Score |
|---|---|
| Model | Random Forest Classifier |
| Dataset size | 6M+ transactions |
| Key features | Transaction type, account balances, transfer amount |

---

## Project Overview

Financial fraud costs businesses billions of dollars annually. This project builds a complete ML pipeline to automatically flag suspicious transactions based on behavioral patterns — the same approach used by real fintech companies.

### What was built
- **EDA**: Analyzed transaction patterns, class imbalance, and feature correlations
- **Feature Engineering**: Extracted meaningful signals from balance changes and transaction types
- **Model Training**: Trained and evaluated a Random Forest classifier
- **Streamlit App**: Built an interactive web app where users can input transaction details and get a live fraud prediction
- **Feature Importance**: Identified that `oldbalanceOrg`, `oldbalanceDest`, and transaction `type` are the strongest fraud indicators

---

## Streamlit App

The app lets you enter:
- Transaction type (CASH_IN, CASH_OUT, DEBIT, PAYMENT, TRANSFER)
- Amount and account balances
- Flagged fraud indicator

And returns: **Fraudulent** or **Not Fraudulent**

---

## Tech Stack

- **Language**: Python
- **ML**: scikit-learn (Random Forest)
- **Data**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **App**: Streamlit
- **Model saving**: joblib
- **Environment**: Jupyter Notebook

---

## Project Structure

```
fraud-detection-ai/
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
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## Key Insight

The most important fraud indicator was `oldbalanceOrg` — accounts that are completely emptied in a single transaction are highly associated with fraudulent behavior. This aligns with real-world fraud patterns where stolen accounts are drained immediately.
