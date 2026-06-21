# Reproducible Machine Learning Pipeline

## Project Title

Bankruptcy-Related Credit Risk Classification Using Random Forest and SBS Financial Indicators in Peru

---

## Objective

This pipeline develops and evaluates a Random Forest model to classify bankruptcy-related credit risk using financial indicators obtained from the Superintendence of Banking, Insurance and AFP (SBS) of Peru.

---

## Dataset

Source:

- Superintendencia de Banca, Seguros y AFP (SBS)

Period:

- 2014–2025

Target Variable:

- CALIFICACIÓN

Classes:

- B = Low Risk
- C = Medium Risk
- D = High Risk
- E = Very High Risk

---

## Pipeline Workflow

1. Load financial dataset (bd3.xlsx)
2. Transform matrix structure
3. Select target variable (CALIFICACIÓN)
4. Encode categorical classes using LabelEncoder
5. Split data into training and testing subsets (70/30)
6. Train Random Forest Classifier
7. Evaluate model performance
8. Generate feature importance ranking

---

## Model Configuration

RandomForestClassifier

```python
RandomForestClassifier(
    n_estimators=300,
    random_state=42
)
```

---

## Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Feature Importance

---

## Results

### Accuracy

0.942857 (94.29%)

### Main Findings

Most influential variables:

1. Provisiones / Créditos Atrasados (%)
2. Créditos Directos / Empleados
3. Créditos Atrasados > 90 días
4. Créditos Atrasados (criterio SBS)
5. Gastos de Operación / Margen Financiero

---

## Repository Structure

```text
05_pipeline/

├── data/
│   └── raw/
│       └── bd3.xlsx

├── notebooks/
│   └── random_forest_credit_risk.ipynb

├── src/

├── models/

├── results/
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── model_metrics.md

├── README.md

└── requirements.txt
```

---

## Software

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Google Colab

---

## Reproducibility

To reproduce the experiment:

```bash
pip install -r requirements.txt
```

Open:

```text
notebooks/random_forest_credit_risk.ipynb
```

Run all cells sequentially.

---

## Limitations

The dataset presents class imbalance, with some risk categories having very few observations. This affects predictive performance for minority classes and should be considered when interpreting the results.

---

## AI Assistance Disclosure

AI assistance (ChatGPT, OpenAI) was used for documentation support, repository organization, and academic writing improvements. Model development, dataset preparation, implementation, experimentation, and interpretation of results remain the responsibility of the author.
