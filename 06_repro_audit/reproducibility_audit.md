# Reproducibility Audit

## Objective

This document evaluates the reproducibility of the proposed Machine Learning framework for bankruptcy-related credit risk classification using official financial indicators published by the Superintendencia de Banca, Seguros y AFP (SBS) of Peru.

The objective is to ensure that an independent researcher can reproduce the complete experimental workflow using the information provided in this repository.

---

# Reproducibility Checklist

| Component | Status | Description |
|-----------|:------:|-------------|
| Research question | ✅ | Clearly defined. |
| Dataset source | ✅ | Official financial indicators obtained from SBS. |
| Data availability | ✅ | Publicly accessible. |
| Data preprocessing | ✅ | Fully documented. |
| Feature selection | ✅ | Explicitly described. |
| Machine Learning models | ✅ | Documented with implementation details. |
| Hyperparameters | ✅ | Reported. |
| Train/Test split | ✅ | Documented. |
| Evaluation metrics | ✅ | Accuracy, Precision, Recall, F1-score and ROC-AUC. |
| Random seed | ✅ | Fixed to ensure reproducibility. |
| Software environment | ✅ | Documented. |
| Source code | ✅ | Available in this repository. |
| Version control | ✅ | Managed using Git and GitHub. |

---

# Computational Environment

| Component | Specification |
|-----------|---------------|
| Programming Language | Python 3.12 |
| Development Environment | Google Colab |
| Operating System | Linux (Google Colab Runtime) |
| Version Control | Git + GitHub |

---

# Python Libraries

| Library | Purpose |
|----------|---------|
| pandas | Data manipulation |
| numpy | Numerical computation |
| scikit-learn | Machine Learning algorithms |
| matplotlib | Visualization |
| seaborn | Statistical visualization |
| joblib | Model serialization |

---

# Randomness Control

To ensure reproducibility, all experiments use a fixed random seed.

```python
random_state = 42
```

This configuration guarantees identical data partitioning and deterministic model training whenever supported by the selected algorithm.

---

# Experimental Workflow

```text
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Feature Selection
        │
        ▼
Train/Test Split
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Result Analysis
```

---

# Data Versioning

The study uses official financial indicators published by the Superintendencia de Banca, Seguros y AFP (SBS).

No manual modification of the original dataset is performed. All preprocessing operations are executed programmatically and documented within the repository.

---

# Repository Structure

```text
project/

├── data/
├── notebooks/
├── models/
├── outputs/
├── src/
├── requirements.txt
└── README.md
```

---

# Potential Threats to Reproducibility

| Risk | Mitigation |
|------|------------|
| Changes in the SBS database | Archive the downloaded dataset used in the experiments. |
| Library version updates | Specify package versions in requirements.txt. |
| Random initialization | Use a fixed random seed (42). |
| Different hardware environments | Execute experiments using Google Colab. |

---

# Reproducibility Assessment

The proposed framework satisfies the fundamental principles of computational reproducibility by documenting:

- Data source
- Data preprocessing
- Experimental workflow
- Model configuration
- Evaluation methodology
- Computational environment
- Software dependencies
- Version control

Consequently, an independent researcher should be able to reproduce the reported experiments using the documentation and source code contained in this repository.

---

# Future Improvements

Future versions of this repository may incorporate:

- Docker containers.
- Continuous Integration (CI) workflows.
- Automated experiment tracking.
- Model versioning.
- Dataset version control using DVC.

---

**AI Use Disclosure**

AI (ChatGPT, OpenAI) was used to improve writing clarity, document organization, and formatting. The reproducibility strategy, computational decisions, and experimental design were defined by the author.
