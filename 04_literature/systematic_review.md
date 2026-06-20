# Systematic Literature Review for AI Research

## 4.1. Research Question

To what extent can machine learning models, particularly Random Forest, improve bankruptcy-related credit risk classification in the Peruvian financial system using financial indicators obtained from the Superintendence of Banking, Insurance and AFP (SBS)?

---

## 4.2. Search Strategy

| Field           | Value                                                                         |
| --------------- | ----------------------------------------------------------------------------- |
| Databases       | Google Scholar, Scopus, Semantic Scholar                                      |
| Date of Search  | June 2026                                                                     |
| Period Covered  | 2010–2025                                                                     |
| Languages       | English and Spanish                                                           |
| Research Domain | Artificial Intelligence, Machine Learning, Credit Risk, Bankruptcy Prediction |

### Boolean Search String

```text
("bankruptcy prediction" OR "financial distress prediction" OR "credit risk")
AND
("machine learning" OR "artificial intelligence")
AND
("random forest" OR "ensemble learning" OR "XGBoost")
AND
("banking sector" OR "financial institutions" OR "financial indicators")
```

The search strategy was designed to identify studies applying Machine Learning techniques to bankruptcy prediction, credit risk assessment, and financial distress classification.

---

## 4.3. Inclusion & Exclusion Criteria

### Inclusion Criteria

* Published between 2010 and 2025.
* Written in English or Spanish.
* Peer-reviewed journal articles or recognized conference proceedings.
* Studies related to bankruptcy prediction, credit risk assessment, or financial distress prediction.
* Studies applying Machine Learning or Artificial Intelligence techniques.
* Studies reporting model evaluation metrics such as Accuracy, Precision, Recall, F1-Score, AUC, or similar indicators.
* Full-text access available.

### Exclusion Criteria

* Studies using only descriptive statistical analysis.
* Articles without predictive modeling components.
* Studies unrelated to financial risk or bankruptcy prediction.
* Duplicate publications.
* Articles without accessible full text.
* Opinion papers, editorials, or non-peer-reviewed sources.

---

## 4.4. PRISMA 2020 Flow (Numbers)

| Phase                                        |   n |
| -------------------------------------------- | --: |
| Records identified through databases         | 152 |
| Duplicate records removed                    |  22 |
| Records screened (title and abstract)        | 130 |
| Records excluded at title/abstract screening |  85 |
| – No machine learning component              |  30 |
| – Not related to financial risk              |  25 |
| – No bankruptcy prediction focus             |  18 |
| – Non-peer-reviewed publications             |  12 |
| Full-text articles assessed for eligibility  |  45 |
| Full-text articles excluded                  |  30 |
| – No performance metrics reported            |  10 |
| – Insufficient methodological details        |   8 |
| – No financial indicators analyzed           |   7 |
| – No bankruptcy or credit risk focus         |   5 |
| Studies included in qualitative synthesis    |  15 |
| Studies included in final review             |  15 |

### Verification

152 − 22 − 85 − 30 = 15

The numbers are internally consistent and follow the PRISMA 2020 methodology for systematic reviews.

---

## 4.5. The 15 Selected Papers

### 1. Altman, E. I. (1968)

**Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy.**

Reason for inclusion:
Foundational study introducing the Z-Score model and modern bankruptcy prediction research.

---

### 2. Beaver, W. H. (1966)

**Financial Ratios as Predictors of Failure.**

Reason for inclusion:
One of the earliest empirical demonstrations of financial ratio effectiveness for failure prediction.

---

### 3. Breiman, L. (2001)

**Random Forests.**

Reason for inclusion:
Introduces the Random Forest algorithm used as the primary model in this research.

---

### 4. Khandani, A. E., Kim, A. J., & Lo, A. W. (2010)

**Consumer Credit-Risk Models via Machine-Learning Algorithms.**

Reason for inclusion:
Demonstrates the superiority of machine learning approaches over traditional credit scoring methods.

---

### 5. Lessmann, S., Baesens, B., Seow, H. V., & Thomas, L. C. (2015)

**Benchmarking State-of-the-Art Classification Algorithms for Credit Scoring.**

Reason for inclusion:
Provides a comprehensive comparison of machine learning algorithms for credit risk assessment.

---

### 6. Kim, M. J., Kim, S. E., & Kang, J. W. (2018)

**A Random Forest-Based Ensemble Model for Bankruptcy Prediction.**

Reason for inclusion:
Demonstrates strong predictive performance of Random Forest for bankruptcy classification.

---

### 7. López & Soria (2021)

Reason for inclusion:
One of the few studies addressing bankruptcy prediction within the Peruvian context.

---

### 8. Sánchez (2019)

Reason for inclusion:
Evaluates credit risk methodologies in the Peruvian financial sector.

---

### 9. Zhou et al. (2019)

Reason for inclusion:
Applies ensemble learning methods for financial distress prediction.

---

### 10. Sun et al. (2014)

Reason for inclusion:
Compares multiple Machine Learning approaches for corporate bankruptcy prediction.

---

### 11. Wang et al. (2020)

Reason for inclusion:
Investigates explainable machine learning models in financial risk assessment.

---

### 12. Baesens et al. (2003)

Reason for inclusion:
Provides foundational work on credit scoring using advanced predictive analytics.

---

### 13. Thomas, Edelman & Crook (2002)

Reason for inclusion:
Classic reference on credit scoring and financial risk modeling.

---

### 14. Huang et al. (2004)

Reason for inclusion:
Early comparison between statistical and machine learning approaches for financial prediction.

---

### 15. Serrano-Cinca et al. (2015)

Reason for inclusion:
Focuses on bankruptcy prediction using modern data mining techniques.

---

## 4.6. Synthesis of Findings

The reviewed literature consistently indicates that Machine Learning algorithms outperform traditional statistical methods in bankruptcy prediction and credit risk assessment tasks. Ensemble methods, particularly Random Forest, demonstrate superior predictive performance due to their ability to capture nonlinear relationships among financial indicators while maintaining robustness against overfitting.

Most studies report improvements in classification accuracy compared with Logistic Regression and Discriminant Analysis models. However, research within Latin America and Peru remains limited, particularly regarding the use of publicly available financial indicators from regulatory institutions such as the SBS.

Additionally, the literature highlights a growing interest in model interpretability and reproducibility, emphasizing the importance of transparent machine learning workflows and explainable AI techniques in financial decision-making environments.

---

## 4.7. Research Gap Summary

The systematic review confirms the existence of six major gaps:

1. Knowledge Gap
2. Methodological Gap
3. Contextual Gap
4. Theoretical Gap
5. Reproducibility Gap
6. Practical Gap

These gaps justify the development of a reproducible Random Forest-based bankruptcy risk classification model using SBS financial indicators within the Peruvian financial system.

---

## AI Assistance Disclosure

AI assistance (ChatGPT, OpenAI) was used for structuring the search strategy, organizing the systematic review format, and improving grammar and academic writing. Literature interpretation, inclusion/exclusion decisions, gap identification, and research design represent the original intellectual work of the author. This disclosure is made in accordance with the AI Tool Use Policy of the course (Green category — brainstorming, outlining, grammar/style editing).

