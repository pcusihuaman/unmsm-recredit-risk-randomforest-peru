# Ethics Protocol (v0.1)

Applying the principles of the **Belmont Report (1979)** and the ethical framework presented in the UNMSM Doctoral Program course *Research Ethics in AI*, this protocol describes the ethical considerations for the research project:

**"Machine Learning Model for Predicting the Financial Risk Classification of Peruvian Municipal Savings and Credit Banks (CMACs) Using Public Financial Indicators."**

---

# 9.1 Purpose & Participants

## Research Purpose

The purpose of this research is to develop and evaluate a supervised Machine Learning model capable of predicting the financial risk classification of Peruvian Municipal Savings and Credit Banks (CMACs) using publicly available financial indicators published by the Superintendencia de Banca, Seguros y AFP (SBS).

## Participants

This research does **not** involve direct human participants.

No interviews, surveys, experiments, medical records, biometric information, or personal financial records are collected.

The study exclusively analyzes institutional financial information published by the SBS.

---

# 9.2 Data Collection

The dataset was compiled from publicly available financial reports released by the **Superintendencia de Banca, Seguros y AFP (SBS)**.

The collected information includes institutional financial indicators such as:

- Capital adequacy
- Liquidity ratios
- Delinquent loans
- Loan-loss provisions
- Deposits
- Operating expenses
- Profitability indicators

No web scraping, social media data, or privately obtained information is used.

---

# 9.3 Informed Consent

Because this study exclusively uses publicly available institutional financial information, **individual informed consent is not required**.

No personal, confidential, or identifiable information is processed.

The research complies with the ethical principle of **Respect for Persons** by avoiding the collection or processing of personal data.

---

# 9.4 Risks

| Potential Risk | Mitigation Strategy |
|----------------|--------------------|
| Incorrect model predictions | Results are presented only as decision-support information for research purposes. |
| Dataset bias | Model performance is evaluated using independent test data and multiple evaluation metrics. |
| Misinterpretation of predictions | Results are accompanied by methodological limitations and explanatory documentation. |
| Future distribution shift | The model should be periodically retrained using updated SBS financial reports. |

Overall research risk is considered **minimal**, since no human participants or confidential information are involved.

---

# 9.5 Benefits

Expected benefits include:

- Supporting academic research in financial risk prediction.
- Promoting reproducible Machine Learning research.
- Improving transparency in AI-based financial analysis.
- Providing a benchmark for future studies using Peruvian financial data.

No direct financial benefit is expected for individual institutions.

---

# 9.6 Confidentiality

The dataset contains **institutional financial information only**.

No names, identification numbers, customer records, or personal financial information are included.

All analyses are performed using publicly available aggregated data.

The repository distributes only the processed research dataset and documentation used for this study.

---

# 9.7 Data Storage & Retention

The project repository is maintained using GitHub version control.

Research files include:

- Source code
- Documentation
- Trained models
- Experimental results
- Processed datasets

Research materials will be retained throughout the doctoral project and updated as new SBS reports become available.

---

# 9.8 Conflict of Interest

The author declares:

- No commercial funding.
- No financial relationship with the Superintendencia de Banca, Seguros y AFP (SBS).
- No conflicts of interest related to the development or evaluation of the proposed Machine Learning model.

Any future funding or institutional collaboration will be disclosed in subsequent versions of this protocol.

---

# 9.9 AI-Specific Considerations

## Training Data Provenance

All training data originate from publicly available financial reports published by the Superintendencia de Banca, Seguros y AFP (SBS).

## Consent Status

The research uses institutional public data only.

No personal information requiring informed consent is processed.

## Model Deployment Harms

Incorrect predictions could be misinterpreted if the model were used outside its intended academic context.

For this reason, the model is presented exclusively as a research and decision-support tool and **not** as an automated financial decision system.

## Dual-Use Risk

The model could potentially be misused as the sole basis for financial supervision or investment decisions.

To mitigate this risk, all documentation clearly states that human expert judgment must accompany any interpretation of model predictions.

---

# Ethical Framework

This protocol follows the ethical principles discussed throughout the course:

- **Belmont Report (1979):**
  - Respect for Persons
  - Beneficence
  - Justice

It also considers the Peruvian ethical framework presented during the course:

- Ley N.º 29733 – Personal Data Protection
- Ley N.º 31814 – Promotion of Artificial Intelligence
- CONCYTEC National Code of Scientific Integrity

---

# AI Assistance Disclosure

AI (ChatGPT, OpenAI) was used to improve the writing, grammar, and Markdown formatting of this Ethics Protocol. The ethical considerations, methodological decisions, risk assessment, and proposed mitigation strategies accurately represent the research conducted by the author and are disclosed in accordance with the AI use policy of the course.
