# Paradigm Justification Statement

## Title

**Development of an Artificial Intelligence Model for Credit Risk Classification in Peruvian Financial Institutions Using SBS Financial Indicators**

**Research Paradigms for AI: Positivism, Interpretivism & Computational Thinking**

---

## 1.1 Research Topic & Context

The Peruvian financial system plays a fundamental role in maintaining economic stability by facilitating credit allocation, promoting investment, and safeguarding public confidence. To ensure the soundness of financial institutions, the Superintendencia de Banca, Seguros y AFP (SBS) continuously monitors financial indicators related to solvency, liquidity, profitability, operational efficiency, and portfolio quality.

Credit risk assessment is an important component of financial supervision because inaccurate risk classification may contribute to poor financial decisions, deterioration of financial portfolios, and increased institutional risk. Traditionally, financial risk assessment has relied on financial ratios and statistical approaches. However, the increasing volume and complexity of financial information create opportunities for Artificial Intelligence and Machine Learning techniques capable of identifying nonlinear relationships and interactions among financial variables.

The availability of standardized financial indicators published by the SBS provides an opportunity to develop and empirically evaluate a reproducible Machine Learning approach for financial risk classification in Peru.

Rather than assuming beforehand that a particular Machine Learning algorithm will provide the best predictive performance, this research proposes an experimental comparison of supervised learning algorithms under identical computational conditions. This approach allows model selection to be based on empirical evidence and objective evaluation metrics.

---

## 1.2 Preliminary Research Question

**To what extent can supervised Machine Learning models, trained on financial indicators published by the Superintendencia de Banca, Seguros y AFP (SBS), accurately classify credit risk levels of Peruvian financial institutions while maintaining reproducibility, interpretability, and scientific validity?**

### Three formulations of the same research question

### Version A — Predictive Focus

Which financial indicators contribute most to predicting credit risk levels in Peruvian financial institutions, and how accurately can supervised Machine Learning models classify different risk categories?

### Version B — Applied Focus

Can a reproducible Machine Learning pipeline support financial risk assessment using publicly available SBS financial indicators?

### Version C — Comparative Focus

Which supervised Machine Learning algorithm provides the best balance between predictive performance, interpretability, and reproducibility for credit risk classification using SBS financial indicators?

---

## 1.3 Chosen Paradigm & Justification

This research adopts a **Computational and Quantitative Empirical paradigm grounded in the positivist tradition**.

From a positivist perspective, financial risk is considered an objective and measurable phenomenon that can be represented through observable financial indicators. Variables such as capital adequacy, liquidity, profitability, portfolio quality, operational efficiency, and financial leverage capture different dimensions of institutional financial health that can be empirically measured, analyzed, and validated.

The objective of this research is not to understand the subjective perceptions or experiences of financial analysts or institutional decision-makers. Instead, the study seeks to identify measurable and reproducible patterns contained within structured financial data.

Consequently, a purely interpretivist paradigm is not selected because the principal research objective does not involve explaining human experiences, organizational culture, perceptions, or qualitative decision-making processes.

The computational paradigm is particularly appropriate because the research problem involves discovering potentially complex and multidimensional relationships among financial variables using Artificial Intelligence techniques. Supervised Machine Learning algorithms can learn these relationships from empirical observations and generate predictive models whose performance can be objectively evaluated.

Experimental computational research therefore serves as the methodological framework through which knowledge claims will be evaluated, while supervised Machine Learning constitutes the primary analytical approach.

This paradigm also aligns with principles of scientific rigor including transparent methodology, reproducible experiments, documented computational environments, objective evaluation metrics, and open research practices.

---

## 1.4 Implications of Paradigm Choice

### Data

The research will use structured quantitative financial information obtained from official SBS publications.

The dataset includes indicators associated with financial dimensions such as:

- Solvency
- Liquidity
- Profitability
- Operational efficiency
- Credit portfolio quality
- Financial leverage
- Other supervisory financial ratios

These variables constitute the empirical evidence from which the predictive models will learn patterns associated with the target risk classification.

### Research Method

The selected paradigm supports an **Experimental Research approach, specifically a Computational Machine Learning Experiment**.

Under this approach, supervised Machine Learning algorithms will be trained, benchmarked, and validated under comparable experimental conditions.

The algorithms initially considered are:

1. Logistic Regression
2. Decision Tree
3. Random Forest

The final predictive model will not be selected a priori. Instead, model selection will be supported by empirical evidence obtained from the experimental comparison.

### Validation

Knowledge claims will be supported through empirical and reproducible validation procedures.

The experimental framework will consider:

- Controlled train/test or train/validation/test partitions
- Fixed random seeds
- Stratification where appropriate
- Cross-validation where appropriate
- Identical evaluation conditions across competing algorithms
- Documentation of preprocessing and model parameters

Predictive performance will be evaluated using standard classification metrics such as:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

Particular attention will be given to class imbalance because overall accuracy alone may provide an incomplete representation of model performance when some risk categories are underrepresented.

### Expected Outputs

The study is expected to produce:

1. A validated Machine Learning model for financial risk classification.
2. An empirical comparison between supervised Machine Learning algorithms.
3. Identification of the financial indicators with the greatest predictive importance.
4. A reproducible Machine Learning pipeline.
5. A transparent computational workflow suitable for replication by other researchers.

### Scientific Contribution

The research seeks to contribute to the intersection between Artificial Intelligence and financial risk assessment by proposing a reproducible computational framework using publicly available SBS financial indicators.

The contribution is not limited to predictive performance. The study also emphasizes:

- Reproducibility
- Methodological transparency
- Model interpretability
- Objective benchmarking
- Documentation of the computational research process

This approach may provide empirical evidence regarding the applicability of supervised Machine Learning techniques to financial risk classification within the Peruvian financial context.

---

## 1.5 One Doubt or Tension

The principal uncertainty concerns the quality and representativeness of publicly available SBS financial data.

Financial indicators may contain missing values, reporting inconsistencies, changes in regulatory definitions over time, or strongly imbalanced risk categories. These characteristics may affect predictive performance and the external validity of the resulting model.

A second methodological tension concerns the trade-off between **predictive performance and interpretability**.

More complex Machine Learning algorithms may capture nonlinear relationships and interactions among financial variables more effectively, but financial applications also require transparent and understandable explanations of predictive decisions.

Consequently, the research must evaluate not only which model achieves the highest predictive performance, but also whether its predictions can be interpreted sufficiently to support scientifically valid and potentially useful financial risk assessment.

This trade-off between predictive capability, interpretability, and reproducibility will remain an important methodological consideration throughout the research.

---

## AI Assistance Disclosure

AI assistance (ChatGPT, OpenAI) was used for organizing the structure of this document, improving academic writing, and refining the presentation of the research paradigm and methodological terminology.

The research topic, selection of the research paradigm, interpretation of the SBS financial indicators, methodological decisions, and final research design represent the intellectual work and decisions of the author.

This disclosure is made in accordance with the AI Tool Use Policy of the course (Green category — brainstorming, outlining, grammar/style editing).
