# UNMSM Research Methods — Paul Cusi

Doctoral capstone project for **Research Methods and Scientific Integrity in AI and Advanced Technologies** — UNMSM.

**Author:** Paul Cusi
**Topic:** Development of an Artificial Intelligence Model (Random Forest) to Estimate Bankruptcy-Related Credit Risk in the Peruvian Financial Sector Using SBS Financial Indicators.

---

## Project Overview

This project develops and evaluates a Machine Learning model based on the Random Forest algorithm to classify bankruptcy-related credit risk using financial indicators obtained from the Superintendence of Banking, Insurance and AFP (SBS) of Peru.

The study follows a reproducible research approach, integrating systematic literature review, methodological justification, machine learning experimentation, and transparent documentation practices aligned with scientific integrity principles.

---

## Repository Structure

### 01_paradigm/

Paradigm Justification Statement (Session 1)

### 02_method/

Method-Fit Matrix and Methodological Justification (Session 2)

### 03_protocol/

Research Protocol versions v0.1 → final version (Sessions 3, 13, 15)

### 04_literature/

Systematic Literature Review + PRISMA Diagram + Gap Analysis (Session 4)

### 05_pipeline/

Reproducible Machine Learning Pipeline: Git + Data Versioning + Experiment Documentation (Session 5)

### 06_benchmarking/

Model comparison and benchmarking against alternative Machine Learning approaches

### 07_model_card/

Model Card documenting intended use, performance, limitations, and responsible AI considerations

### 08_dataset_sheet/

Dataset documentation describing SBS data sources, variables, preprocessing, and limitations

### 09_ethics/

Ethical considerations, transparency, reproducibility, and responsible AI assessment

### 10_reflective_writing/

Research reflections, lessons learned, and scientific integrity considerations

---

## Dataset

Source:

* Superintendence of Banking, Insurance and AFP (SBS), Peru

Period:

* 2014–2025

Target Classes:

* B (Low Risk)
* C (Medium Risk)
* D (High Risk)

Sample Size:

* 231 observations

---

## Machine Learning Model

Primary Algorithm:

* Random Forest Classifier

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Feature Importance Analysis

Current Result:

* Accuracy ≈ 93%

---

## Reproducibility

This repository follows reproducible research principles through:

* Git version control
* Transparent documentation
* Structured research workflow
* Open-source software
* Reproducible Machine Learning experiments

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Google Colab
* GitHub

---

## AI Assistance Disclosure

AI assistance (ChatGPT, OpenAI) was used for brainstorming, academic writing support, repository organization, and documentation improvement. All methodological decisions, data preparation, model implementation, evaluation, interpretation of results, and research contributions remain the responsibility of the author and collaborators.
