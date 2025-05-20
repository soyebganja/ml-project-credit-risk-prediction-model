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
- Feature selection and engineering for credit risk factors
- Implementation of multiple classification algorithms
- Model evaluation with industry-relevant metrics (AUC-ROC, precision, recall)
- Class imbalance handling techniques
- Model interpretability tools for regulatory compliance
- Risk score generation based on probability predictions

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
- `customer_id`: Unique identifier for each customer
- `loan_amount`: Amount of loan requested
- `term`: Loan term in months
- `interest_rate`: Interest rate on the loan
- `installment`: Monthly payment amount
- `annual_income`: Borrower's annual income
- `debt_to_income`: Debt-to-income ratio
- `credit_score`: Numeric credit score
- `employment_length`: Years at current employment
- `home_ownership`: Status of home ownership
- `purpose`: Purpose of the loan
- `age`: Age of the borrower
- `loan_history`: Number of previous loans
- `delinquencies`: Number of delinquencies in the past 2 years
- `default`: Whether the borrower defaulted (target variable)

**Note**: Sensitive data should be handled according to relevant data protection regulations.

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ml-project-credit-risk-prediction-model.git
   cd ml-project-credit-risk-prediction-model
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the main script:
   ```bash
   python src/main.py
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
4. Evaluate the model:
   ```bash
   python src/evaluate.py
   ```
5. Generate predictions:
   ```bash
   python src/predict.py --input your_data.csv
   ```

---

## Model Performance

Our final model achieves:
- AUC-ROC: 0.92
- Precision: 0.85
- Recall: 0.78
- F1-Score: 0.81

Performance metrics by risk category:
- Low risk: 96% accuracy
- Medium risk: 74% accuracy
- High risk: 59% accuracy

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
- **Email**: soyeb.ganja@gmail.com
- **GitHub**: [soyebganja](https://github.com/soyebganja/ml-project-credit-risk-prediction-model)
- **LinkedIN**: https://linkedin.com/in/soyeb-ganja

---
