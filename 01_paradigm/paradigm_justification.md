# Paradigm Justification Statement
##  Title .Development of an Artificial Intelligence Model (Random Forest) to Estimate Bankruptcy-Related Credit Risk in the Peruvian Financial Sector Using SBS Financial Indicators.  
Research Paradigms for AI: Positivism, Interpretivism & Computational Thinking

---

# 1.1 Research Topic & Context

The Peruvian financial system plays a fundamental role in maintaining economic stability by facilitating credit allocation, promoting investment, and safeguarding public confidence. To ensure the soundness of financial institutions, the Superintendence of Banking, Insurance and Private Pension Funds (SBS) continuously monitors financial indicators related to solvency, liquidity, profitability, operational efficiency, and portfolio quality.

Credit risk assessment is one of the most critical supervisory activities because inaccurate risk classification may lead to poor lending decisions, deterioration of financial portfolios, and increased systemic risk. Traditionally, this evaluation has relied on financial ratios and statistical approaches. However, the increasing volume and complexity of financial information create opportunities for Artificial Intelligence and Machine Learning techniques capable of identifying nonlinear relationships that conventional methods may fail to detect.

The availability of standardized financial indicators published by the SBS provides an opportunity to develop a reproducible machine learning model capable of supporting credit risk classification while contributing to more transparent, evidence-based, and data-driven financial supervision in Peru.

---

# 1.2 Preliminary Research Question

To what extent can a supervised machine learning model, trained on financial indicators published by the Superintendence of Banking, Insurance and AFP (SBS), accurately classify credit risk levels of Peruvian financial institutions while maintaining reproducibility, interpretability, and scientific validity?

### Three formulations of the same research question

### Version A — Predictive Focus

Which financial indicators contribute most to predicting credit risk levels in Peruvian financial institutions, and how accurately can supervised machine learning models classify different risk categories?

### Version B — Applied Focus

Can a reproducible machine learning pipeline support financial supervision by improving credit risk assessment using publicly available SBS financial indicators?

### Version C — Comparative Focus

Which supervised machine learning algorithm provides the best balance between predictive performance, interpretability, and reproducibility for credit risk classification using SBS financial indicators?

---

# 1.3 Chosen Paradigm & Justification

This research adopts a **Computational and Quantitative Empirical paradigm grounded in the positivist tradition**, with Machine Learning serving as the methodological framework for knowledge generation.

From a positivist perspective, credit risk is considered an objective and measurable phenomenon that can be represented through observable financial indicators. Variables such as capital adequacy, liquidity, profitability, portfolio quality, operational efficiency, and financial leverage are assumed to capture aspects of institutional financial health that can be empirically measured, analyzed, and validated.

The objective of this research is not to understand the subjective perceptions of financial analysts or institutional decision-makers, but rather to identify reproducible patterns contained within structured financial data. Consequently, an interpretivist paradigm is not appropriate because the study does not seek to explain human experiences, organizational culture, or qualitative decision-making processes.

The computational paradigm is particularly suitable because the research problem involves discovering complex and multidimensional relationships among financial variables using Artificial Intelligence techniques. Rather than manually defining decision rules, supervised machine learning algorithms learn these relationships directly from empirical evidence and generate predictive models that can be objectively evaluated through reproducible experiments.

This paradigm also aligns with the principles of scientific rigor emphasized throughout this course: transparent methodology, reproducible experiments, documented computational environments, objective evaluation metrics, and open research practices.

---

# 1.4 Implications of Paradigm Choice

## Data

The research will exclusively use structured quantitative financial information obtained from official SBS publications, including indicators related to solvency, liquidity, profitability, operational efficiency, credit portfolio quality, and other supervisory ratios.

## Methods

The paradigm supports supervised machine learning methods for classification. Different algorithms will be experimentally evaluated under the same reproducible framework before selecting the final predictive model according to objective performance criteria.

## Validation

Knowledge claims will be supported through empirical validation using reproducible experiments, train-validation-test partitions, fixed random seeds, cross-validation where appropriate, and standard evaluation metrics such as Accuracy, Precision, Recall, F1-score, ROC-AUC, and Confusion Matrix.

## Expected Outputs

The study is expected to produce:

- A validated credit risk classification model.
- A reproducible machine learning pipeline.
- Identification of the financial indicators with the greatest predictive importance.
- A transparent computational workflow suitable for replication by other researchers.

## Scientific Contribution

The research seeks to contribute to the emerging intersection between Artificial Intelligence and financial supervision by proposing a reproducible computational framework for credit risk classification using publicly available SBS financial information. Beyond predictive performance, the study contributes to methodological transparency, reproducibility, and explainability in AI-based financial decision support.

---

# 1.5 One Doubt or Tension

The principal uncertainty concerns the quality and representativeness of publicly available supervisory data. Financial indicators may present missing values, reporting inconsistencies, temporal changes in regulatory criteria, or class imbalance that could affect model performance and external validity.

An additional challenge involves balancing predictive accuracy with model interpretability. While more complex machine learning algorithms may achieve higher classification performance, financial supervision also requires transparent and explainable models that justify their predictions. Addressing this trade-off between predictive capability and interpretability will constitute an important methodological consideration throughout the research.

