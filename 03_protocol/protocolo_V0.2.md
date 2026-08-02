# Research Protocol Outline (v0.1)

---

# 3.1. Title

**Development and Validation of a Machine Learning-Based Predictive Model for Bankruptcy Risk Classification in the Peruvian Financial System Using Financial Indicators from the Superintendencia de Banca, Seguros y AFP (SBS)**

---

# 3.2. Abstract

Bankruptcy risk assessment represents one of the most important challenges in financial supervision because inaccurate risk classification may lead to loan defaults, deterioration of portfolio quality, and financial instability. Traditional statistical approaches often fail to capture complex nonlinear relationships among financial indicators.

This research develops and validates a supervised Machine Learning framework for bankruptcy risk classification using official financial indicators published by the Superintendencia de Banca, Seguros y AFP (SBS) of Peru for the period **2014–2025**.

Three supervised learning algorithms—**Logistic Regression, Decision Tree, and Random Forest**—are compared under identical experimental conditions to identify the model with the highest predictive performance. The selected model is evaluated using Accuracy, Precision, Recall, F1-score, ROC-AUC, Confusion Matrix, and Feature Importance analysis.

The entire workflow is implemented under a reproducible computational research framework using Python, Scikit-Learn, Google Colab, GitHub, and version-controlled documentation.

The expected contribution is a transparent and reproducible methodology capable of supporting bankruptcy risk assessment while identifying the financial indicators most strongly associated with credit risk in the Peruvian financial system.

---

# 3.3. Introduction & Problem Statement

## Problem Statement

Credit risk represents one of the principal sources of financial losses within banking institutions because it directly affects portfolio quality, profitability, regulatory compliance, and financial stability.

Traditional bankruptcy prediction methods generally rely on statistical models and financial ratios that assume linear relationships among variables. Although widely adopted, these approaches often fail to capture the complex nonlinear interactions present in modern financial systems.

During the last decade, the Peruvian financial system has generated an increasing volume of structured financial information through the Superintendencia de Banca, Seguros y AFP (SBS). This growing availability of high-quality financial data creates an opportunity to apply Artificial Intelligence techniques capable of improving predictive accuracy.

Despite these advances, empirical studies applying supervised Machine Learning techniques to bankruptcy risk estimation using official SBS financial indicators remain limited in Peru.

---

## Relevance — The "So What?" Test

This research addresses the gap between traditional financial risk assessment methodologies and modern Artificial Intelligence techniques.

The study contributes to:

- Financial supervision.
- Evidence-based decision making.
- Explainable Artificial Intelligence (XAI).
- Reproducible computational research.

The proposed methodology may also serve as a benchmark for future AI applications in financial regulation and bankruptcy prediction.

---

# 3.4. Literature Review

Altman (1968) demonstrated the predictive value of financial ratios through the Z-Score model. Beaver (1966) showed that financial indicators can anticipate business failure before bankruptcy occurs.

Breiman (2001) introduced Random Forest as an ensemble learning algorithm capable of improving predictive performance while reducing overfitting. Khandani, Kim, and Lo (2010) demonstrated that Machine Learning models outperform traditional credit scoring methods by capturing nonlinear relationships among financial variables.

Lessmann et al. (2015) emphasized the importance of benchmarking multiple Machine Learning algorithms in credit scoring applications and highlighted the strong performance of ensemble methods.

Although international research has advanced considerably, relatively few studies have evaluated supervised Machine Learning models using official SBS financial indicators within the Peruvian financial system.

This study addresses that methodological and empirical gap.

---

# 3.5. Research Questions / Hypotheses

## General Research Question

To what extent can a supervised Machine Learning approach accurately classify bankruptcy-related credit risk in the Peruvian financial system using financial indicators published by the SBS under a reproducible computational research framework?

---

## Specific Research Questions

- Which financial indicators exhibit the strongest association with bankruptcy-related credit risk?

- Which supervised Machine Learning algorithm achieves the highest predictive performance?

- Can Explainable AI techniques identify the most influential variables supporting financial decision-making?

- Can the proposed methodology provide a reproducible computational framework for future bankruptcy prediction studies?

---

## Working Hypothesis

A supervised Machine Learning model trained using SBS financial indicators will achieve predictive performance above **90% Accuracy** while providing interpretable evidence regarding the financial variables most strongly associated with bankruptcy-related credit risk.

---

# 3.6. Methodology

## Research Paradigm

Computational / Quantitative Empirical (Positivist) Paradigm.

---

## Research Method

**Experimental Research using Computational Machine Learning.**

---

## Research Design

- Applied Research
- Quantitative Research
- Non-experimental Design
- Comparative Computational Experiment

---

## Data Sources

Official financial indicators published by the **Superintendencia de Banca, Seguros y AFP (SBS)**.

**Study Period:** 2014–2025.

---

## Population

Financial institutions supervised by the SBS.

---

## Sample

231 observations selected according to data availability and completeness.

---

## Unit of Analysis

Each observation corresponds to one financial institution represented by its annual financial indicators reported to the SBS.

---

## Target Variable

Credit Risk Classification

- B — Low Risk
- C — Medium Risk
- D — High Risk

---

## Predictor Variables

Financial indicators associated with:

- Solvency
- Asset Quality
- Liquidity
- Profitability
- Operational Efficiency
- Foreign Currency Exposure

---

## Experimental Strategy

Three supervised Machine Learning algorithms will be evaluated under identical experimental conditions:

- Logistic Regression
- Decision Tree
- Random Forest

Each algorithm will use the same preprocessing pipeline, identical train/test partitions, and standardized evaluation metrics to ensure fair comparison.

The model with the best predictive performance will be selected as the final predictive model.

---

## Validation Strategy

The experimental evaluation includes:

- Train/Test Split
- Cross Validation
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

All experiments will be executed using fixed random seeds to ensure reproducibility.

---

## Explainability

Model interpretability will be evaluated through:

- Feature Importance
- SHAP Analysis (if implemented)

The objective is to identify the financial indicators contributing most significantly to bankruptcy risk prediction.

---

## Reproducibility Plan

The complete computational workflow will be documented using:

- Python
- Google Colab
- Scikit-Learn
- GitHub

allowing independent replication of all experiments.

---

# 3.7. Ethical Considerations

This research exclusively utilizes publicly available financial information obtained from the SBS.

No personal, confidential, or sensitive information is processed.

The study follows principles of:

- Transparency
- Reproducibility
- Academic Integrity
- Responsible Artificial Intelligence
- Explainable Artificial Intelligence (XAI)

All source code, datasets, methodological decisions, and experimental procedures will be documented and version-controlled using GitHub.

---

# 3.8. Expected Results

- Structured SBS financial dataset.
- Reproducible computational pipeline.
- Comparative benchmark of supervised Machine Learning algorithms.
- Validated predictive model.
- Classification Accuracy greater than **90%**.
- Identification of the most influential financial indicators.
- Explainable AI analysis.
- Public GitHub repository documenting the complete workflow.
- Scientific manuscript suitable for publication.

---

# 3.9. Timeline & Budget

## Preliminary Timeline (12 Months)

| Period | Activities |
|----------|------------|
| Months 1–2 | Literature review, research framework, SBS data collection |
| Months 3–4 | Data preprocessing and exploratory analysis |
| Months 5–6 | Model development and hyperparameter tuning |
| Months 7–8 | Model validation and performance evaluation |
| Months 9–10 | Feature importance and explainability analysis |
| Months 11–12 | Documentation, GitHub repository, final report |

---

## Preliminary Budget Estimate

| Item | Estimated Cost (S/.) |
|------|---------------------:|
| Google Colab Pro / Cloud Resources | 150 |
| Internet Services | 120 |
| Cloud Storage & Backup | 80 |
| Scientific Literature | 150 |
| Miscellaneous | 100 |
| **TOTAL** | **600** |

---

## Budget Justification

The project relies primarily on publicly available financial data and open-source technologies. Development will be conducted using Google Colab, Python, Scikit-Learn, and GitHub, minimizing infrastructure costs while ensuring reproducibility.

Bibliography

Baesens, B., Van Gestel, T., Viaene, S., Stepanova, M., Suykens, J., & Vanthienen, J. (2003). Benchmarking state-of-the-art classification algorithms for credit scoring. *Journal of the Operational Research Society, 54*(6), 627–635. https://doi.org/10.1057/palgrave.jors.2601545

Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32. https://doi.org/10.1023/A:1010933404324

Gundersen, O. E., & Kjensmo, S. (2018). State of the art: Reproducibility in artificial intelligence. *Proceedings of the AAAI Conference on Artificial Intelligence, 32*(1), 1644–1651. https://doi.org/10.1609/aaai.v32i1.11503

Hutson, M. (2018). Artificial intelligence faces reproducibility crisis. *Science, 359*(6377), 725–726. https://doi.org/10.1126/science.359.6377.725

Khandani, A. E., Kim, A. J., & Lo, A. W. (2010). Consumer credit-risk models via machine-learning algorithms. *Journal of Banking & Finance, 34*(11), 2767–2787. https://doi.org/10.1016/j.jbankfin.2010.06.001

Kim, M.-J., & Kang, D.-K. (2010). Ensemble with neural networks for bankruptcy prediction. *Expert Systems with Applications, 37*(4), 3373–3379. https://doi.org/10.1016/j.eswa.2009.10.012

Lessmann, S., Baesens, B., Seow, H.-V., & Thomas, L. C. (2015). Benchmarking state-of-the-art classification algorithms for credit scoring: An update of research. *European Journal of Operational Research, 247*(1), 124–136. https://doi.org/10.1016/j.ejor.2015.05.030

Pineau, J., Vincent-Lamarre, P., Sinha, K., Larivière, V., Beygelzimer, A., d’Alché-Buc, F., Fox, E., & Larochelle, H. (2021). Improving reproducibility in machine learning research (A report from the NeurIPS 2019 reproducibility program). *Journal of Machine Learning Research, 22*(164), 1–20.

Serrano-Cinca, C., Gutiérrez-Nieto, B., & López-Palacios, L. (2015). Determinants of default in P2P lending. *PLOS ONE, 10*(10), e0139427. https://doi.org/10.1371/journal.pone.0139427

Thomas, L. C., Edelman, D. B., & Crook, J. N. (2002). *Credit scoring and its applications*. Society for Industrial and Applied Mathematics.
---

## Funding Source

This research will be self-funded and supported through open-source technologies including Python, Google Colab, Scikit-Learn, GitHub, and publicly available SBS financial datasets.
