import streamlit as st
import pandas as pd
import numpy as np

from prediction_helper import predict

def main():
  st.title("Credit Risk Modeling App")
  
  # Row 1 - First set of controls
  col1, col2, col3 = st.columns(3)
  
  with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
  with col2:
    income = st.number_input("Income", min_value=0, max_value=1000000, value=50000)
  with col3:
    loan_amount = st.number_input("Loan Amount", min_value=0, max_value=1000000, value=100000)
  
  # Row 2 - Second set of controls
  col4, col5, col6 = st.columns(3)
  
  with col4:
    loan_tenure_months = st.number_input("Loan Tenure (months)", min_value=1, max_value=360, value=12)
  with col5:
    avg_dpd_per_delinquency = st.number_input("Days Past Due (DPD)", min_value=0, max_value=1000, value=0)
  with col6:
    credit_utilization_ratio = st.slider("Credit Utilization (%)", min_value=0, max_value=100, value=30)
  
  # Row 3 - Third set of controls
  col7, col8, col9 = st.columns(3)
  
  with col7:
    residence_type = st.selectbox("Residence Type", ["Owned", "Rented", "Mortgage"])
  with col8:
    loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Auto", "Personal"])
  with col9:
    loan_type = st.selectbox("Loan Type", ["Secured", "Unsecured"])
  
  # Row 4 - New controls
  col10, col11, col12 = st.columns(3)
  
  loan_to_income_ratio = loan_amount / income if income > 0 else 0
  with col10:
    st.write("Loan to Income Ratio: ")
    st.write(f"{loan_to_income_ratio:.2f}")
    # loan_to_income_ratio = st.number_input("Loan to Income Ratio", min_value=0.0, max_value=1.0, value=0.3, format="%.2f")
  with col11:
    delinquency_ratio = st.number_input("Delinquency Ratio", min_value=0.0, max_value=1.0, value=0.0, format="%.2f")
  with col12:
    open_loan_accounts = st.number_input("Open Loan Accounts", min_value=0, max_value=50, value=0)
  
  # Submit button
  if st.button("Submit Application"):
    probability, credit_score, rating = predict(
      age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
      delinquency_ratio, credit_utilization_ratio, open_loan_accounts,
      residence_type, loan_purpose, loan_type
    )

    # st.write(f"Default Probability: {probability:.2f}")
    # st.write(f"Credit Score: {credit_score:.2f}")
    # st.write(f"Rating: {rating}")

if __name__ == "__main__":
  main()
