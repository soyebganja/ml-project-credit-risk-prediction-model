import streamlit as st
import pandas as pd
import numpy as np

from prediction_helper import predict

def main():
  st.title("Doom Finance: Credit Risk Modeling")
  
  # Row 1 - First set of controls
  col1, col2, col3 = st.columns(3)
  
  with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=28)
  with col2:
    income = st.number_input("Income", min_value=0, max_value=10000000, value=1200000)
  with col3:
    loan_amount = st.number_input("Loan Amount", min_value=0, max_value=10000000, value=2560000)
  
  # Row 2 - Second set of controls
  col4, col5, col6 = st.columns(3)
  
  loan_to_income_ratio = loan_amount / income if income > 0 else 0
  with col4:
    st.write("Loan to Income Ratio: ")
    st.write(f"{loan_to_income_ratio:.2f}")
  with col5:
    loan_tenure_months = st.number_input("Loan Tenure (months)", min_value=1, max_value=360, value=36)
  with col6:
    avg_dpd_per_delinquency = st.number_input("Avg Days Past Due (DPD)", min_value=0, max_value=1000, value=20)
  
  # Row 3 - Third set of controls
  col7, col8, col9 = st.columns(3)
  
  with col7:
    delinquency_ratio = st.number_input("Delinquency Ratio", min_value=0, max_value=100, value=30)
  with col8:
    credit_utilization_ratio = st.number_input("Credit Utilization (%)", min_value=0, max_value=100, value=30)
  with col9:
    open_loan_accounts = st.number_input("Open Loan Accounts", min_value=0, max_value=50, value=2)
  
  # Row 4 - New controls
  col10, col11, col12 = st.columns(3)
  
  with col10:
    residence_type = st.selectbox("Residence Type", ["Owned", "Rented", "Mortgage"])
  with col11:
    loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Auto", "Personal"])
  with col12:
    loan_type = st.selectbox("Loan Type", ["Unsecured", "Secured"])
  
  
  # Submit button
  if st.button("Calculate Risk"):
    probability, credit_score, rating = predict(
      age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
      delinquency_ratio, credit_utilization_ratio, open_loan_accounts,
      residence_type, loan_purpose, loan_type
    )

    st.write(f"Default Probability: {probability*100:.2f}%")
    st.write(f"Credit Score: {credit_score:.2f}")
    st.write(f"Rating: {rating}")

if __name__ == "__main__":
  main()
