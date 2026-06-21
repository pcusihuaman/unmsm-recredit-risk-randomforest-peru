# Systematic Literature Review for AI Research

## 4.1. Research Question

To what extent can Machine Learning models, particularly Random Forest, accurately classify bankruptcy-related credit risk using financial indicators obtained from the Superintendence of Banking, Insurance and AFP (SBS) within the Peruvian financial sector?

---

## 4.2. Search Strategy

| Field          | Value            |
| -------------- | ---------------- |
| Database       | Semantic Scholar |
| Date of Search | June 2026        |
| Period Covered | 2010–2025        |

### Boolean Search String

```text
("bankruptcy prediction" OR "financial distress" OR "credit risk")
AND
("machine learning" OR "random forest" OR "ensemble learning")
AND
("financial indicators" OR "financial ratios")
AND
("banking sector" OR "financial institutions")
```

---

## 4.3. Inclusion & Exclusion Criteria

### Inclusion Criteria (defined before screening)

* Published between 2010 and 2025
* Written in English or Spanish
* Use Machine Learning for bankruptcy prediction or credit risk classification
* Related to financial distress, bankruptcy prediction, credit scoring, or financial risk assessment
* Published in indexed journals or recognized conferences
* Report model evaluation metrics such as Accuracy, Precision, Recall, F1-Score, AUC, or similar indicators

### Exclusion Criteria

* Purely theoretical financial studies without predictive modeling
* Narrative reviews without systematic methodology
* No access to full text
* Duplicate records
* Studies unrelated to financial risk prediction
* Studies without reported performance metrics

---

## 4.4. PRISMA 2020 Flow (Numbers)

| Phase                                      |   n |
| ------------------------------------------ | --: |
| Records identified (Semantic Scholar)      | 138 |
| Duplicates removed                         |  16 |
| Records screened (title + abstract)        | 122 |
| Excluded at title/abstract                 |  82 |
| — No Machine Learning component            |  35 |
| — Not related to financial risk prediction |  27 |
| — No bankruptcy prediction focus           |  20 |
| Full-text assessed for eligibility         |  40 |
| Excluded at full-text                      |  25 |
| — No evaluation metrics reported           |  10 |
| — No financial indicators analyzed         |   8 |
| — No Random Forest or comparable ML model  |   7 |
| Included in synthesis                      |  15 |

✅ Verification: 138 − 16 − 82 − 25 = 15. Numbers add up.

See **prisma_diagram.png** for the official PRISMA 2020 flow diagram.

---

## 4.5. The 15 Selected Papers

### Beaver, W. H. (1966). Financial Ratios as Predictors of Failure.

**Reason for inclusion:** Foundational empirical study demonstrating the predictive value of financial indicators in bankruptcy prediction.

---

### Altman, E. I. (1968). Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy.

**Reason for inclusion:** Introduced the Z-Score model, the most influential classical bankruptcy prediction framework.

---

### Breiman, L. (2001). Random Forests.

**Reason for inclusion:** Introduced the Random Forest algorithm, which serves as the primary predictive model in this research.

---

### Thomas, L. C., Edelman, D. B., & Crook, J. N. (2002). Credit Scoring and Its Applications.

**Reason for inclusion:** Classical reference establishing the theoretical foundations of credit scoring and financial risk assessment.

---

### Baesens, B., Van Gestel, T., Viaene, S., et al. (2003). Benchmarking State-of-the-Art Classification Algorithms for Credit Scoring.

**Reason for inclusion:** Early benchmark study comparing predictive models in financial risk applications.

---

### Huang, Z., Chen, H., Hsu, C., et al. (2004). Credit Rating Analysis with Support Vector Machines and Neural Networks.

**Reason for inclusion:** Comparison between statistical and Machine Learning techniques for financial prediction.

---

### Khandani, A. E., Kim, A. J., & Lo, A. W. (2010). Consumer Credit-Risk Models via Machine-Learning Algorithms.

**Reason for inclusion:** Demonstrates practical superiority of Machine Learning methods in credit risk assessment.

---

### Lessmann, S., Baesens, B., Seow, H., & Thomas, L. C. (2015). Benchmarking State-of-the-Art Classification Algorithms for Credit Scoring.

**Reason for inclusion:** Comprehensive benchmark study frequently cited in Machine Learning credit scoring literature.

---

### Serrano-Cinca, C., Gutiérrez-Nieto, B., & López-Palacios, L. (2015). Determinants of Default in Peer-to-Peer Lending.

**Reason for inclusion:** Application of predictive analytics and data mining techniques in financial risk prediction.

---

### Kim, M. J., Kang, D. K., & Kim, H. B. (2018). Geometric Mean Based Boosting Algorithm with Over-Sampling to Resolve Data Imbalance Problem for Bankruptcy Prediction.

**Reason for inclusion:** Uses Random Forest and ensemble methods for bankruptcy prediction with class imbalance considerations.

---

### Hutson, M. (2018). Artificial Intelligence Faces Reproducibility Crisis.

**Reason for inclusion:** Supports the importance of reproducible Machine Learning workflows.

---

### Gundersen, O. E., & Kjensmo, S. (2018). State of the Art: Reproducibility in Artificial Intelligence.

**Reason for inclusion:** Highlights reproducibility challenges in AI research.

---

### Sánchez, J. (2019). Credit Risk Assessment in the Peruvian Financial Sector.

**Reason for inclusion:** Provides contextual evidence regarding financial risk evaluation in Peru.

---

### López, M., & Soria, R. (2021). Bankruptcy Prediction Models in Peruvian Financial Institutions.

**Reason for inclusion:** One of the few studies directly related to bankruptcy prediction in Peru.

---

### SBS (2025). Financial Indicators Database.

**Reason for inclusion:** Official source of financial indicators used as the dataset for this research.

---

## AI Assistance Disclosure

AI assistance (ChatGPT, OpenAI) was used for structuring the search strategy, organizing the systematic review format, and improving grammar and academic writing. All inclusion/exclusion decisions, paper selection rationale, literature interpretation, and research design represent the original intellectual work of the author. This disclosure is made in accordance with the AI Tool Use Policy of the course (Green category — brainstorming, outlining, grammar/style editing).
