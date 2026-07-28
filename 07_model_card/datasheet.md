# Dataset Datasheet

Following the framework proposed by **Gebru et al. (2021), Datasheets for Datasets.**

---

# 1. Motivation

### Why was this dataset created?

The dataset was prepared to develop and evaluate Machine Learning models capable of predicting the financial risk classification of Peruvian Municipal Savings and Credit Banks (CMACs). The objective is to support transparent, reproducible, and data-driven financial risk assessment using publicly available financial indicators.

### Who created the dataset?

The dataset was compiled and prepared by the author as part of the UNMSM Doctoral Program in Deep Technologies for academic research purposes.

---

# 2. Composition

### What do the instances represent?

Each row represents one financial observation of a Peruvian Municipal Savings and Credit Bank (CMAC).

### Number of instances

- Approximately **231 observations**.

### Variables

The dataset contains financial indicators published by the Superintendencia de Banca, Seguros y AFP (SBS), including:

- Capital Adequacy Ratio
- Total Liabilities / Capital Ratio
- Delinquent Loans Ratio
- Loans Over 90 Days Ratio
- Liquidity Indicators
- Deposits
- Provisions
- Operating Expenses
- Profitability Indicators

The target variable corresponds to the **financial risk classification** used in this study.

---

# 3. Collection Process

The data were compiled from publicly available financial information published by the **Superintendencia de Banca, Seguros y AFP (SBS)**.

No personal, confidential, or individually identifiable information is included in the dataset.

---

# 4. Preprocessing, Cleaning and Labeling

The following preprocessing steps were performed:

- Inspection of missing values
- Numerical feature selection
- Label Encoding of the target variable
- Train/Test split
- Fixed random seed (`random_state = 42`) for reproducibility

No synthetic observations were generated.

---

# 5. Uses

### Intended Uses

The dataset is intended for:

- Credit risk prediction
- Bankruptcy risk research
- Machine Learning benchmarking
- Explainable AI research
- Academic studies

### Not Recommended Uses

The dataset should not be used as the sole basis for regulatory, supervisory, or commercial financial decisions without additional validation.

---

# 6. Distribution

The dataset originates from publicly available SBS reports and is distributed exclusively for academic research within this repository.

---

# 7. Maintenance

The dataset is maintained by the project author.

Future versions may incorporate additional financial periods, updated SBS indicators, and expanded institutional coverage.

---

# AI Assistance Disclosure

AI (ChatGPT, OpenAI) was used to improve the writing, grammar, and Markdown formatting of this Datasheet. The dataset description and preprocessing workflow accurately represent the dataset used in this research.
