# Research Question + Method-Fit Matrix

## 2.1 Research Question (Method-Ready Precision)

To what extent can a supervised machine learning model, comparing Logistic Regression, Decision Tree, and Random Forest, trained on financial indicators obtained from the Superintendence of Banking, Insurance and AFP (SBS), accurately classify credit risk levels in the Peruvian financial system and identify the most influential financial indicators associated with risk?

---

## 2.2 Three Candidate Methods

| Method      | Method 1 — Random Forest Classification                                                                | Method 2 — Logistic Regression                                              | Method 3 — Decision Tree                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Description | Ensemble machine learning model capable of handling nonlinear relationships and variable interactions. | Traditional statistical classification model widely used in credit scoring. | Tree-based classification model with high interpretability and simple decision rules. |

---

## 2.3 E.D.F.C.V. Scoring Matrix (1–5 per criterion)

| Criterion               | Key Question                                                          | Method 1 (Random Forest) | Method 2 (Logistic Regression) | Method 3 (Decision Tree) |
| ----------------------- | --------------------------------------------------------------------- | ------------------------ | ------------------------------ | ------------------------ |
| E – Epistemological Fit | Does this method match the Computational / Positivist paradigm?       | 5/5                      | 5/5                            | 5/5                      |
| D – Data Availability   | Can SBS financial indicators support this method?                     | 5/5                      | 5/5                            | 5/5                      |
| F – Feasibility         | Is implementation realistic within the course timeline?               | 5/5                      | 5/5                            | 5/5                      |
| C – Contribution Type   | Does the method provide predictive insights and variable importance?  | 5/5                      | 3/5                            | 4/5                      |
| V – Venue Fit           | Is the method accepted in finance, AI, and machine learning research? | 5/5                      | 4/5                            | 4/5                      |
| TOTAL                   |                                                                       | 25/25                    | 22/25                          | 23/25                    |

*Scores are preliminary and intended only as methodological justification.*

---

## 2.4 Defense of the Winner: Method 1 — Random Forest

### Why Method 1 wins

The research objective is to accurately classify credit risk levels using financial indicators from the SBS. Random Forest is selected because it can model nonlinear relationships, handle interactions among financial variables, reduce overfitting through ensemble learning, and provide measures of feature importance that improve interpretability.

Additionally, Random Forest has demonstrated strong performance in financial risk prediction studies and can effectively manage heterogeneous financial datasets.

### Why not Method 2 (Logistic Regression)

Logistic Regression is widely accepted in credit scoring and provides high interpretability. However, it assumes mostly linear relationships between predictors and the target variable, which may limit its ability to capture complex interactions among financial indicators.

### Why not Method 3 (Decision Tree)

Decision Trees are easy to interpret and visualize, but they are more sensitive to overfitting and instability. Small changes in the dataset may lead to substantially different tree structures, reducing generalization performance compared with ensemble methods.

### One Open Tension

Although Random Forest is expected to provide the best predictive performance, its internal decision process is less transparent than Logistic Regression. Balancing predictive accuracy and interpretability remains an important consideration, particularly in financial environments where decision makers often require clear explanations for risk classifications.

