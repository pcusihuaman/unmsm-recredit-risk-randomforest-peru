# Research Protocol Outline (v0.1)

## 3.1. Title

Development of an Artificial Intelligence Model (Random Forest) to Estimate Bankruptcy Risk in the Banking Sector in Peru Using Financial Indicators from the Superintendence of Banking, Insurance and AFP (SBS).

---

## 3.2. Abstract

Bankruptcy risk estimation is a critical challenge within modern financial systems because inaccurate risk assessments may lead to loan defaults, deterioration of portfolio quality, and financial instability. Traditional financial analysis methods, although widely adopted, often struggle to capture complex and nonlinear relationships among financial indicators. This research develops and validates a machine learning-based predictive model using the Random Forest algorithm to estimate bankruptcy-related credit risk within the Peruvian financial sector. The model is trained using financial indicators obtained from the Superintendence of Banking, Insurance and AFP (SBS) covering the period 2014–2025. Risk levels are classified into categories B (Low Risk), C (Medium Risk), and D (High Risk). The model is evaluated through Accuracy, Precision, Recall, F1-Score, Confusion Matrix analysis, and Feature Importance techniques. Preliminary results indicate an overall classification accuracy of 93%, demonstrating the effectiveness of ensemble machine learning methods for financial risk assessment and decision support.

---

## 3.3. Introduction & Problem Statement

### Problem Statement

Credit risk represents one of the most important sources of financial losses within banking institutions because it directly impacts portfolio quality, profitability, and institutional stability. Traditional risk assessment methods generally rely on financial ratios and statistical models that may not adequately capture nonlinear interactions among financial variables.

The Peruvian financial system has generated increasing volumes of financial information during the last decade, creating opportunities to apply advanced analytical techniques capable of improving predictive accuracy. Despite this data availability, empirical studies applying machine learning algorithms for bankruptcy risk estimation within Peru remain limited.

Artificial Intelligence and Machine Learning have demonstrated superior predictive capabilities in multiple financial applications due to their ability to identify hidden patterns and complex relationships among variables. Consequently, there is a need to evaluate whether these techniques can improve bankruptcy risk estimation using financial indicators published by the SBS.

### Relevance — The "So What?" Test

This research addresses the gap between traditional financial risk assessment methodologies and modern machine learning approaches. The study contributes to both academic knowledge and professional practice by demonstrating how publicly available financial indicators can be transformed into predictive tools capable of supporting risk management and decision-making processes.

The results may benefit financial institutions, regulators, and researchers by providing evidence regarding the effectiveness of Random Forest models for bankruptcy risk estimation in the Peruvian financial context. Additionally, the proposed methodology is reproducible and may be extended to other financial risk prediction problems.

---

## 3.4. Literature Review

The prediction of bankruptcy and financial distress has been extensively studied within financial research. Altman (1968) introduced the Z-Score model, demonstrating the predictive power of financial ratios in bankruptcy prediction. Beaver (1966) established that financial indicators could be used to anticipate business failure before it occurs.

The emergence of machine learning techniques has significantly expanded predictive capabilities within financial risk management. Breiman (2001) proposed Random Forest as an ensemble learning algorithm capable of improving classification performance while reducing overfitting. Khandani, Kim, and Lo (2010) demonstrated that machine learning models outperform traditional credit scoring approaches by capturing nonlinear relationships among financial variables.

Kim, Kim, and Kang (2018) found that Random Forest achieved superior performance in bankruptcy prediction compared to alternative classification algorithms. Lessmann et al. (2015) emphasized the importance of benchmarking modern machine learning techniques for credit scoring applications and highlighted the strong performance of ensemble methods.

Although international research has advanced considerably, the application of Random Forest models for bankruptcy risk estimation within the Peruvian financial sector remains relatively limited. This study contributes to closing that gap by evaluating the performance of a machine learning model using SBS financial indicators.

---

## 3.5. Research Questions / Hypotheses

### General Research Question

To what extent can a Random Forest machine learning model improve bankruptcy risk classification in the Peruvian financial system using financial indicators obtained from the SBS?

### Specific Research Questions

1. Which financial indicators exhibit the strongest association with bankruptcy-related risk levels within the Peruvian financial sector?

2. Can a Random Forest model accurately classify financial entities into risk categories B, C, and D using SBS financial indicators?

3. Which variables contribute most significantly to the predictive performance of the model?

4. How effective is Random Forest compared with traditional financial risk assessment approaches for bankruptcy risk estimation?

### Working Hypothesis

A Random Forest classification model trained using SBS financial indicators will achieve high predictive performance (Accuracy ≥ 0.90) and accurately classify entities into risk categories B, C, and D while identifying the most influential financial variables associated with bankruptcy-related risk.

---

## 3.6. Methodology

### Research Paradigm

Computational / Quantitative Empirical Paradigm.

### Research Design

Applied, quantitative, non-experimental research.

### Data Sources

Financial indicators obtained from the Superintendence of Banking, Insurance and AFP (SBS), corresponding to entities operating within the Peruvian financial system.

### Temporal Scope

2014–2025.

### Population

Financial records published by the SBS.

### Sample

231 observations selected according to data availability and completeness criteria.

### Dependent Variable

Credit Risk Classification:

* B: Low Risk
* C: Medium Risk
* D: High Risk

### Independent Variables

Financial indicators associated with:

* Solvency
* Asset Quality
* Profitability
* Liquidity
* Operational Efficiency
* Foreign Currency Exposure

### Algorithm

Primary Model:

* Random Forest Classifier

Future Benchmark Models:

* Logistic Regression
* Support Vector Machine (SVM)
* XGBoost

### Development Process

1. Data collection from SBS.
2. Data cleaning and preprocessing.
3. Variable selection and transformation.
4. Dataset preparation.
5. Model training.
6. Model validation.
7. Performance evaluation.
8. Feature importance analysis.

### Validation Metrics

Primary Metrics:

* Accuracy
* Precision
* Recall
* F1-Score

Secondary Analysis:

* Confusion Matrix
* Feature Importance Ranking

---

## 3.7. Ethical Considerations

This study exclusively utilizes publicly available secondary financial information obtained from the SBS. No personal, confidential, or sensitive information is collected or processed.

The research follows principles of transparency, reproducibility, academic integrity, and responsible AI. All datasets, source code, methodological decisions, and experimental procedures will be documented and version-controlled through GitHub to ensure reproducibility and accountability.

The study does not involve human participants, surveys, interviews, or experimental interventions. Consequently, ethical risks are considered minimal.

---

## 3.8. Expected Results

* Structured and documented financial dataset based on SBS indicators.
* Reproducible Random Forest classification model.
* Classification accuracy greater than 90%.
* Identification of the most influential financial indicators associated with bankruptcy-related risk.
* Feature importance ranking supporting financial interpretability.
* Public GitHub repository documenting the complete research workflow.
* Benchmark framework for future comparison with alternative machine learning algorithms.
* Academic manuscript suitable for scientific dissemination.

---

## 3.9. Timeline & Budget

### Preliminary Timeline (12 Months)

**Months 1–2**

* Literature review.
* Definition of research framework.
* Collection of SBS financial data.
* Repository setup and version control configuration.

**Months 3–4**

* Data cleaning and preprocessing.
* Exploratory Data Analysis (EDA).
* Variable selection and transformation.

**Months 5–6**

* Random Forest model development.
* Hyperparameter tuning.
* Initial model training.

**Months 7–8**

* Model validation and performance evaluation.
* Confusion Matrix analysis.
* Accuracy, Precision, Recall, and F1-Score calculation.

**Months 9–10**

* Feature importance analysis.
* Model interpretation.
* Benchmark preparation for future comparisons with alternative algorithms.

**Months 11–12**

* Documentation of results.
* GitHub repository finalization.
* Research report writing and final presentation.

### Preliminary Budget Estimate

| Item                            | Description                                                                                                        | Estimated Cost (S/.) |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------: |
| Cloud Computing Resources       | Optional Google Colab Pro subscription and additional cloud resources if required                                  |                  150 |
| Internet and Data Access        | Internet services used for accessing SBS data, scientific literature, GitHub, and cloud platforms                  |                  120 |
| Data Storage and Backup         | Cloud storage and backup services for datasets, notebooks, trained models, and documentation                       |                   80 |
| Academic Resources              | Scientific articles, conference proceedings, and specialized references not available through institutional access |                  150 |
| Miscellaneous Research Expenses | Printing, documentation, presentation materials, and contingency expenses                                          |                  100 |
| **Total Estimated Budget**      |                                                                                                                    |              **600** |

### Budget Justification

The estimated budget is relatively low because the project relies primarily on publicly available data sources and open-source technologies. Google Colab is used as the primary development environment, Python and Scikit-Learn are freely available, GitHub provides version control without licensing costs, and SBS financial indicators are publicly accessible. No fieldwork, surveys, interviews, laboratory infrastructure, or proprietary software are required.

### Funding Source

The project will be self-funded by the researcher and supported through open-source technologies including Python, Scikit-Learn, Google Colab, GitHub, and publicly available SBS financial datasets.

