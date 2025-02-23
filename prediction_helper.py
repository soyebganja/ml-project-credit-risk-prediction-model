import joblib
import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

# Path to save model and it's componenet
MODEL_PATH = 'artifacts/model_data.joblib'

# Load the data and it's component
model_data = joblib.load(MODEL_PATH)
model = model_data['model']
scaler = model_data['scaler']
features = model_data['features']
cols_to_scale = model_data['cols_to_scale']

def prepare_df(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, open_loan_accounts,
        residence_type, loan_purpose, loan_type
      ):
  
  input_data = {
      'age': age,
      'loan_tenure_months': loan_tenure_months,
      'number_of_open_accounts': open_loan_accounts,
       'credit_utilization_ratio': credit_utilization_ratio, 
       'loan_to_income': loan_amount / income if income > 0 else 0, 
       'delinquency_ratio': delinquency_ratio,
       'avg_dpd_per_delinquency': avg_dpd_per_delinquency, 
       'residence_type_Owned': 1 if residence_type == 'Owned' else 0,
       'residence_type_Rented': 1 if residence_type == 'Rented' else 0, 
       'loan_purpose_Education': 1 if residence_type == 'Education' else 0, 
       'loan_purpose_Home': 1 if loan_purpose == 'Home' else 0,
       'loan_purpose_Personal': 1 if loan_purpose == 'Personal' else 0, 
       'loan_type_Unsecured': 1 if loan_purpose == 'Unsecured' else 0,
        # Adding additional columns
        'number_of_dependants': 1, # Dummy value
        'years_at_current_address': 1, # Dummy value
        'zipcode': 1, # Dummy value
        'sanction_amount': 1, # Dummy value
        'processing_fee': 1, # Dummy value
        'gst': 1, # Dummy value
        'net_disbursement': 1, # Dummy value
        'principal_outstanding': 1, # Dummy value
        'bank_balance_at_application': 1, # Dummy value
        'number_of_closed_accounts': 1, # Dummy value
        'enquiry_count': 1 # Dummy value
    }
  
  df = pd.DataFrame(input_data)

  df[cols_to_scale] = scaler.transform(df[cols_to_scale])

  df = df[features]

  return df


def calculate_credit_score(input_df, base_score=300, __scale_length=600):
  x = np.dot(input_df.values, model.coef_.T) * model.intercept_

  default_probability = 1 / (1+np.exp(-x))
  non_default_probability = 1 - default_probability

  credit_score = base_score + non_default_probability.flatten() * __scale_length


  def get_rating(score):
    if 300 <= score < 500:
      return 'Poor'
    elif 500 <= score < 650:
      return 'Average'
    elif 650 <= score < 750:
      return 'Good'
    elif 750 <= score <= 900:
      return 'Excellent'
    else:
      return 'Undefined'
    

  rating = get_rating(credit_score[0])


  return default_probability.flatten()[0], credit_score, rating

  
def predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, open_loan_accounts,
        residence_type, loan_purpose, loan_type
      ):
  
  input_df = prepare_df(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, open_loan_accounts,
        residence_type, loan_purpose, loan_type
      )
  
  probability, credit_score, rating = calculate_credit_score(input_df)

  return probability, credit_score, rating
