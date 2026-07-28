# Model Card

Following the framework proposed by **Mitchell et al. (2019), Model Cards for Model Reporting.**

---

# 1. Model Details

**Model name:** Random Forest for Financial Risk Classification

**Developed by:** Paul Cusi

**Institution:** Universidad Nacional Mayor de San Marcos (UNMSM)

**Program:** Doctoral Program in Deep Technologies

**Date:** July 2026

**Model type:** Random Forest Classifier (Scikit-learn)

**Training framework:** Python + Scikit-learn

**Repository:** This GitHub repository

---

# 2. Intended Use

### Primary Intended Use

The model is designed to predict the financial risk classification of Peruvian Municipal Savings and Credit Banks (CMACs) using publicly available financial indicators published by the Superintendencia de Banca, Seguros y AFP (SBS).

### Intended Users

- Researchers
- Graduate students
- Financial risk analysts
- Academic institutions

### Out-of-Scope Uses

This model should not be used as the sole basis for regulatory supervision, lending decisions, or investment decisions without expert validation.

---

# 3. Factors

The model performance may be influenced by:

- Quality of financial indicators
- Changes in macroeconomic conditions
- Data availability
- Class imbalance
- Temporal changes in the financial system

---

# 4. Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

Final test accuracy:

**Accuracy = 94.29%**

---

# 5. Evaluation Data

Evaluation was performed using a held-out test set obtained from the original SBS dataset.

The evaluation follows a reproducible Train/Test split using:

- Train: 70%
- Test: 30%
- random_state = 42

---

# 6. Training Data

The model was trained using approximately **231 financial observations** from Peruvian Municipal Savings and Credit Banks (CMACs).

Training variables include:

- Capital adequacy
- Liquidity
- Delinquent loans
- Deposits
- Provisions
- Operating expenses
- Profitability indicators

Target variable:

- Financial Risk Classification

The dataset is fully described in **08_dataset_sheet/datasheet.md**.

---

# 7. Quantitative Analyses

The Random Forest model achieved an overall classification accuracy of **94.29%** on the test dataset.

Feature importance analysis identified the following variables as the most influential:

- Provisions / Delinquent Loans
- Credit per Employee
- Loans Over 90 Days
- Delinquent Loans Ratio
- Operating Expenses

These variables contributed most to the prediction of financial risk classification.

---

# 8. Ethical Considerations

The model was trained exclusively using publicly available institutional financial data obtained from the Superintendencia de Banca, Seguros y AFP (SBS).

No personal, confidential, or sensitive individual information was used.

The model is intended to support academic research and should not replace professional financial judgment.

---

# 9. Caveats and Recommendations

This model has several limitations:

- It was trained using historical financial information only.
- Performance may decrease when applied to future financial periods.
- The model has not been externally validated using independent datasets.
- Predictions should be interpreted as decision-support information rather than definitive financial assessments.

Future work includes:

- External validation with new SBS reports.
- Comparison with XGBoost and LSTM models.
- Explainability analysis using SHAP.
- Annual model retraining as new financial data become available.

---

# AI Assistance Disclosure

AI (ChatGPT, OpenAI) was used to improve the writing, grammar, and Markdown formatting of this Model Card. The model description, experimental methodology, evaluation results, and limitations accurately represent the Machine Learning model developed in this research.
