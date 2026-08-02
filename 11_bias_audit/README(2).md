# Session 11 — Bias Audit

## Overview

This directory contains the artifacts developed for **Session 11** of the reproducible research project.

The objective is to demonstrate a complete **algorithmic bias auditing workflow** using a benchmark dataset, evaluate fairness metrics, apply a mitigation strategy, and document the results in a transparent and reproducible manner.

> **Important:** The numerical values included in this repository are **synthetic demonstration results** intended to illustrate the reporting workflow. They are **not empirical results** obtained from executing Fairlearn or AIF360.

---

# Project

**Digital Transformation and Its Impact on the Quality and Efficiency of Higher Education: A Case Study of the Universidad Nacional Mayor de San Marcos**

---

# Objectives

- Assess algorithmic fairness.
- Measure disparate impact and related fairness metrics.
- Demonstrate a bias mitigation strategy.
- Compare fairness metrics before and after mitigation.
- Document a reproducible Responsible AI workflow.

---

# Repository Structure

```text
11_bias_audit/
├── README.md
├── BIAS_AUDIT_REPORT.md
├── FAIRNESS_METRICS.md
├── MITIGATION_STRATEGY.md
├── BEFORE_AFTER_COMPARISON.md
├── notebooks/
│   └── bias_audit.ipynb
├── src/
│   ├── bias_audit.py
│   └── fairness_utils.py
├── results/
│   ├── metrics_before.csv
│   ├── metrics_after.csv
│   └── summary.md
└── references.bib
```

---

# Methodology

- **Dataset:** Adult Census Income (benchmark reference)
- **Protected Attribute:** `sex`
- **Baseline Model:** Logistic Regression
- **Bias Mitigation:** Fairlearn ExponentiatedGradient
- **Evaluation Metrics:**
  - Accuracy
  - Precision
  - Recall
  - F1-score
  - ROC-AUC
  - Disparate Impact
  - Demographic Parity Difference
  - Demographic Parity Ratio
  - Equal Opportunity Difference
  - Equalized Odds Difference

---

# Workflow

```text
Dataset
   ↓
Preprocessing
   ↓
Baseline Model
   ↓
Fairness Evaluation
   ↓
Bias Mitigation
   ↓
Retraining
   ↓
Fairness Re-evaluation
```

---

# Files

| File | Description |
|------|-------------|
| BIAS_AUDIT_REPORT.md | Main bias audit report |
| FAIRNESS_METRICS.md | Definitions and interpretation of fairness metrics |
| MITIGATION_STRATEGY.md | Description of mitigation approach |
| BEFORE_AFTER_COMPARISON.md | Comparative analysis before and after mitigation |

---

# Reproducibility

The project is designed to integrate with:

- Git
- GitHub
- DVC
- MLflow
- Python
- Scikit-learn
- Fairlearn

---

# References

- Bellamy et al. (2019). AI Fairness 360.
- Bird et al. (2020). Fairlearn.
- Mitchell et al. (2019). Model Cards for Model Reporting.
- Gebru et al. (2021). Datasheets for Datasets.
