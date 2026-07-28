# Data Management Plan

This Data Management Plan (DMP) describes how research data will be collected, stored, managed, protected, shared, and preserved throughout the doctoral research project:

**"Machine Learning Model for Predicting the Financial Risk Classification of Peruvian Municipal Savings and Credit Banks (CMACs) Using Public Financial Indicators."**

This plan follows the FAIR Principles (Findable, Accessible, Interoperable and Reusable) together with the research integrity recommendations discussed during Session 10.

---

# 10.1 Data Description

The dataset used in this research consists of publicly available financial information published by the **Superintendencia de Banca, Seguros y AFP (SBS)**.

### Dataset characteristics

| Item | Description |
|------|-------------|
| Source | Superintendencia de Banca, Seguros y AFP (SBS) |
| Data type | Structured tabular financial data |
| Number of observations | Approximately 231 financial observations |
| Variables | Financial indicators and risk classification |
| Format | Microsoft Excel (.xlsx), CSV |
| Personal data | None |

The dataset contains institutional financial indicators, including:

- Capital adequacy ratios
- Liquidity indicators
- Delinquent loan ratios
- Loan-loss provisions
- Deposits
- Operating expenses
- Profitability indicators

---

# 10.2 FAIR Compliance

| FAIR Principle | Implementation |
|----------------|----------------|
| **Findable** | All project files are organized in a public GitHub repository with clear documentation. |
| **Accessible** | Source code, documentation and processed datasets are publicly available through GitHub. Original SBS reports remain publicly accessible through the SBS website. |
| **Interoperable** | Data are stored using open and widely supported formats (CSV, Markdown, XLSX). Variable names are documented in the Dataset Datasheet. |
| **Reusable** | Complete documentation, preprocessing workflow, and model description allow other researchers to reproduce the study. |

---

# 10.3 Data Protection

The research uses **public institutional financial information only**.

No personal, confidential, or identifiable information is collected or processed.

Since no personal data are included, anonymization procedures are not required.

Nevertheless, the following good research practices are applied:

- Version control using Git.
- Documentation of preprocessing steps.
- Preservation of original data files.
- Reproducible preprocessing scripts.

---

# 10.4 Storage & Backup

Project files are managed using GitHub version control.

Research materials include:

- Source code
- Documentation
- Dataset
- Trained models
- Experimental results

Backup strategy:

- Local computer copy
- GitHub repository
- External backup drive

This strategy minimizes the risk of accidental data loss.

---

# 10.5 Legal Compliance

The project considers the following ethical and legal framework discussed during the course.

| Regulation | Application |
|------------|-------------|
| Ley N.º 29733 – Personal Data Protection | No personal information is processed. |
| Ley N.º 31814 – Promotion of Artificial Intelligence | The model is developed under principles of transparency and accountability. |
| CONCYTEC National Code of Scientific Integrity | Research documentation and experimental results are maintained for reproducibility. |

---

# 10.6 Data Sharing Plan

| Research Artifact | Sharing Plan |
|-------------------|-------------|
| Source code | Public GitHub repository |
| Documentation | Public GitHub repository |
| Dataset | Public SBS data with preprocessing documentation |
| Trained models | Public repository |
| Experimental results | Public repository |

The project promotes open science by providing sufficient documentation for independent reproduction.

---

# 10.7 Retention Period

Research materials will be retained throughout the doctoral program.

Following project completion:

- Source code will remain available through GitHub.
- Documentation will remain publicly accessible.
- Public SBS datasets may be updated as new financial reports become available.
- New versions of the model may be released as additional data are incorporated.

---

# AI Assistance Disclosure

AI (ChatGPT, OpenAI) was used to improve the writing, grammar, and Markdown formatting of this Data Management Plan. The data sources, management strategy, storage procedures, FAIR implementation, and legal compliance accurately represent the research conducted by the author and are disclosed according to the AI use policy of the course.
