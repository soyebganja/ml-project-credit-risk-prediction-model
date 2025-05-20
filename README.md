# Credit Risk Prediction Model

This project implements machine learning models to predict credit risk, helping financial institutions assess borrower reliability and make informed lending decisions based on various customer attributes and financial history.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Credit risk assessment is crucial for financial institutions to minimize defaults and optimize lending strategies. This project uses machine learning algorithms to analyze borrower data and predict the probability of default or credit risk level. The models provide objective risk assessments that can be used to improve decision-making processes in loan approvals.

---

## Features

- Comprehensive data preprocessing pipeline for financial data
- Feature engineering focused on credit risk indicators
- Implementation of multiple classification algorithms (Random Forest, XGBoost, Neural Networks)
- Model evaluation with industry-relevant metrics (AUC-ROC, precision, recall)
- Class imbalance handling techniques for default prediction
- Credit scoring methodology based on default probability
- Risk categorization (Excellent, Good, Fair, Poor)
- Interactive web interface for real-time predictions
- Detailed explanation of risk factors influencing predictions

---

## Tech Stack

- **Programming Language**: Python 3.8+
- **Libraries/Frameworks**:
  - Pandas, NumPy: Data manipulation and analysis
  - Scikit-learn: Model training and evaluation
  - XGBoost, LightGBM: Gradient boosting frameworks
  - Imbalanced-learn: Handling class imbalance
  - SHAP, LIME: Model interpretability
  - Matplotlib, Seaborn: Data visualization
  - Flask/FastAPI: API deployment (optional)

---

## Dataset

The dataset used contains the following features:
- `age`: Age of the borrower
- `income`: Annual income of the borrower
- `loan_amount`: Amount of loan requested
- `loan_to_income_ratio`: Ratio of loan amount to income
- `loan_tenure`: Loan term in months
- `avg_days_past_due`: Average days past due for previous loans
- `delinquency_ratio`: Ratio of delinquent payments to total payments
- `credit_utilization`: Percentage of available credit being used
- `open_loan_accounts`: Number of currently open loan accounts
- `residence_type`: Type of residence (Owned, Rented, etc.)
- `loan_purpose`: Purpose of the loan (Education, Home, etc.)
- `education`: Education level of the borrower
- `loan_type`: Type of loan (Secured, Unsecured)
- `default`: Whether the borrower defaulted (target variable)

**Note**: Sensitive data should be handled according to relevant data protection regulations.

---

## Project Structure

```
ml-project-credit-risk-prediction-model/
├── data/
│   ├── raw/              # Raw data files
│   └── processed/        # Processed data files
├── notebooks/            # Jupyter notebooks for exploration and analysis
├── src/
│   ├── __init__.py
│   ├── app.py            # Web application interface
│   ├── preprocess.py     # Data preprocessing scripts
│   ├── features.py       # Feature engineering
│   ├── train.py          # Model training
│   ├── evaluate.py       # Model evaluation
│   ├── predict.py        # Prediction script
│   └── utils.py          # Utility functions
├── models/               # Saved model files
├── tests/                # Unit tests
├── requirements.txt      # Project dependencies
├── setup.py              # Package installation
└── README.md             # Project documentation
```

---

## Usage

1. Prepare your dataset and place it in the `data/` directory
2. Run data preprocessing:
   ```bash
   python src/preprocess.py
   ```
3. Train the model:
   ```bash
   python src/train.py
   ```
4. Make predictions using the model:
   ```bash
   python src/predict.py --input your_data.csv
   ```
5. Alternatively, use the web interface:
   ```bash
   python src/app.py
   ```
   Then navigate to `http://localhost:5000` in your browser

### Sample Input Parameters

```
Age: 35
Income: 75000
Loan Amount: 160000
Loan to Income Ratio: 2.13
Loan Tenure (months): 60
Avg Days Past Due (DPD): 3
Delinquency Ratio: 0.05
Credit Utilization (%): 35
Open Loan Accounts: 2
Residence Type: Owned
Loan Purpose: Education
Education: Graduate
Loan Type: Unsecured
```

---

## Model Output

The model generates the following outputs:
- **Default Probability**: Percentage likelihood of loan default (e.g., 19.73%)
- **Credit Score**: Numerical credit score (e.g., 781.65)
- **Rating**: Credit quality rating (e.g., Excellent, Good, Fair, Poor)

Sample output:
```
Default Probability: 19.73%
Credit Score: 781.65
Rating: Excellent
```

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a meaningful message"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
## Contact

For any inquiries, feel free to reach out:
- **LinkedIN**: https://linkedin.com/in/soyeb-ganja
- **Email**: soyeb.ganja@gmail.com
- **GitHub**: [soyebganja](https://github.com/soyebganja/ml-project-credit-risk-prediction-model)

---
