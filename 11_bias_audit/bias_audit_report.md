
# Bias Audit Report

## Objective

Evaluate whether the Machine Learning pipeline introduced significant bias during
data preparation and model training.

---

## Dataset

- Domain: Credit Risk Classification
- Source: Financial indicators of Peruvian Municipal Savings Banks.
- Target Variable: CALIFICACIÓN

---

## Class Distribution

The dataset contains the following class distribution:

| Class   |   Samples |
|:--------|----------:|
| B       |       110 |
| C       |        69 |
| D       |        49 |

The train-test split was performed using stratified sampling, preserving the
original class proportions.

---

## Model Evaluation

The project compared four classification models.

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 89.86% |
| Random Forest | 89.86% |
| Decision Tree | 85.51% |
| Dummy Classifier | 47.83% |

Cross-validation showed that Random Forest achieved the highest average
generalization performance (89.87%).

---

## Feature Analysis

The most influential variables were:

- Provisions / Non-performing Loans
- Loans per Employee
- Loans over 90 Days
- Operating Expenses

These variables correspond to financial indicators and not to protected
personal attributes.

---

## Bias Assessment

No demographic attributes (gender, ethnicity, age or similar) are present in
the dataset.

Therefore, demographic fairness metrics were not applicable.

The use of stratified sampling preserved class proportions and reduced sampling
bias.

The classification results do not indicate systematic favoritism toward a
single class.

---

## Conclusion

No significant evidence of dataset or model bias was identified under the
available information.

Future studies may incorporate demographic or customer-level variables to
perform a broader fairness assessment.
