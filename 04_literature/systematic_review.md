# Systematic Literature Review

## 4.1 Research Question

**Research Question**

To what extent can supervised Machine Learning models accurately classify bankruptcy-related credit risk using official financial indicators published by the Superintendencia de Banca, Seguros y AFP (SBS) within the Peruvian financial system?

---

# 4.2 Search Strategy

The literature review followed a structured search strategy based on the PRISMA 2020 framework to identify relevant studies on bankruptcy prediction, credit risk assessment, and supervised Machine Learning.

| Field | Description |
|---------|-------------|
| Database | Semantic Scholar |
| Date of Search | June 2026 |
| Period Covered | **1966–2025** |
| Languages | English, Spanish |
| Document Types | Journal Articles and Conference Papers |
| Search Fields | Title, Abstract, Keywords |

### Search Query

```text
("bankruptcy prediction"
OR
"financial distress"
OR
"credit risk")

AND

("machine learning"
OR
"random forest"
OR
"decision tree"
OR
"logistic regression"
OR
"ensemble learning")

AND

("financial indicators"
OR
"financial ratios")

AND

("banking sector"
OR
"financial institutions")
```

---

# 4.3 Inclusion and Exclusion Criteria

## Inclusion Criteria

- Peer-reviewed publications.
- Published between **1966 and 2025**.
- Written in English or Spanish.
- Studies addressing bankruptcy prediction, financial distress, or credit risk.
- Studies applying supervised Machine Learning techniques.
- Research using financial indicators or financial ratios.

## Exclusion Criteria

- Duplicate publications.
- Non-peer-reviewed documents.
- Studies unrelated to financial risk prediction.
- Papers without experimental validation.
- Studies lacking sufficient methodological information.

---

# 4.4 PRISMA Screening Process

The study selection process followed the PRISMA 2020 guidelines.

| Screening Stage | Records |
|-----------------|--------:|
| Records identified | 138 |
| Duplicate records removed | 16 |
| Records screened | 122 |
| Records excluded | 82 |
| Full-text articles assessed | 40 |
| Full-text articles excluded | 25 |
| **Studies included in the review** | **15** |

The complete screening workflow is illustrated in **prisma_diagram.png**.

Verification:

```text
138 − 16 − 82 − 25 = 15 studies included
```

---

# 4.5 Selected Studies

## Classical Foundations

| Study | Main Contribution |
|--------|------------------|
| Beaver (1966) | Demonstrated that financial ratios can predict corporate failure. |
| Altman (1968) | Introduced the Z-score model for bankruptcy prediction. |
| Thomas et al. (2002) | Established theoretical foundations for modern credit scoring. |

---

## Machine Learning Approaches

| Study | Main Contribution |
|--------|------------------|
| Breiman (2001) | Proposed the Random Forest algorithm. |
| Baesens et al. (2003) | Compared Machine Learning techniques for credit scoring. |
| Khandani et al. (2010) | Applied Machine Learning to consumer credit risk. |
| Lessmann et al. (2015) | Large-scale benchmark comparing bankruptcy prediction algorithms. |
| Serrano-Cinca et al. (2015) | Financial distress prediction using Machine Learning. |
| Kim et al. (2018) | Bankruptcy prediction using ensemble learning methods. |

---

## Reproducibility and Scientific Integrity

| Study | Main Contribution |
|--------|------------------|
| Hutson (2018) | Highlighted reproducibility challenges in Artificial Intelligence research. |
| Gundersen & Kjensmo (2018) | Proposed reproducibility practices for computational research. |
| Pineau et al. (2021) | Presented best practices for reproducible Machine Learning experiments. |

---

## Peruvian Financial Context

| Study | Main Contribution |
|--------|------------------|
| Sánchez (2019) | Financial risk assessment within the Peruvian banking sector. |
| López & Soria (2021) | Bankruptcy prediction applied to Peruvian financial institutions. |
| SBS (2025) | Official financial indicators published by the Superintendencia de Banca, Seguros y AFP. |

---

# 4.6 Literature Synthesis

The reviewed literature shows a clear evolution from traditional statistical bankruptcy prediction models toward supervised Machine Learning approaches capable of modeling complex nonlinear relationships among financial indicators.

Classical studies established the theoretical foundations of bankruptcy prediction, while more recent research consistently demonstrates that supervised Machine Learning techniques generally achieve superior predictive performance compared with conventional statistical methods.

However, the literature also reveals important limitations regarding reproducibility, Explainable Artificial Intelligence (XAI), and the application of Machine Learning using official financial indicators from emerging economies. Furthermore, empirical evidence specifically focused on the Peruvian financial system remains limited.

These findings justify the development of a reproducible and interpretable Machine Learning framework based on official financial indicators published by the Superintendencia de Banca, Seguros y AFP (SBS).

---

# 4.7 Research Gap

The literature review reveals five principal research gaps:

- Limited empirical evidence using official SBS financial indicators.
- Limited benchmarking of supervised Machine Learning algorithms under identical experimental conditions.
- Scarce studies focused on the Peruvian financial system.
- Limited adoption of Explainable Artificial Intelligence (XAI).
- Insufficient reproducibility practices in Machine Learning research.

These gaps motivate the present research and are discussed in detail in **gap_analysis.md**.

---

# 4.8 Future Research Opportunities

Future research may extend this work by incorporating advanced Machine Learning algorithms such as XGBoost, LightGBM, CatBoost, and deep learning architectures. Additional studies may also integrate macroeconomic indicators, longitudinal financial information, Explainable Artificial Intelligence (XAI), and real-time financial risk monitoring systems for financial institutions.

---

**AI Use Disclosure**

AI (ChatGPT, OpenAI) was used to improve writing clarity, document organization, and formatting. The literature search strategy, study selection, interpretation of findings, and research conclusions are the original work of the author.
