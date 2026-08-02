# Session 6 — Reproducibility Audit

## Audit of a Published Machine Learning Paper

### Paper
**Title:** Evaluating Higher Education Performance via Machine Learning During Disruptive Times: A Case of Applied Education in Türkiye

- **Journal:** European Journal of Education
- **Publisher:** Wiley
- **Year:** 2024
- **DOI:** https://doi.org/10.1111/ejed.12805

---

# Objective

This reproducibility audit evaluates the transparency, completeness, and computational reproducibility of the selected Machine Learning study.

The audit considers:

- Research transparency
- Dataset availability
- Data preprocessing
- Machine Learning model
- Hyperparameter optimization
- Validation strategy
- Statistical reporting
- Confidence intervals
- Computational environment
- Source code availability

---

# Machine Learning Workflow

```text
Educational Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Min-Max Normalization
        │
        ▼
Feature Engineering
        │
        ▼
Random Forest
        │
        ▼
Grid Search
        │
        ▼
Leave-One-Out Cross Validation
        │
        ▼
Prediction
        │
        ▼
Performance Evaluation
```

---

# Reproducibility Checklist

| Criterion | Status | Assessment |
|-----------|:------:|------------|
| Research Question | ✅ | Complete |
| Dataset Description | ⚠️ | Partial |
| Public Dataset | ⚠️ | Available upon request |
| Data Cleaning | ✅ | Complete |
| Feature Engineering | ⚠️ | Partial |
| Normalization | ✅ | Complete |
| Machine Learning Model | ✅ | Random Forest |
| Hyperparameter Optimization | ✅ | Grid Search |
| Final Hyperparameters | ❌ | Missing |
| Random Seed | ❌ | Not Reported |
| Train/Test Split | ⚠️ | Leave-One-Out CV |
| Validation Strategy | ✅ | Complete |
| Performance Metrics | ✅ | Accuracy, Precision, Recall, F1 |
| Confusion Matrix | ✅ | Available |
| Statistical Tests | ❌ | Missing |
| Confidence Intervals | ❌ | Missing |
| Software Version | ❌ | Missing |
| Library Version | ❌ | Missing |
| Hardware | ❌ | Missing |
| Runtime | ❌ | Missing |
| Source Code | ❌ | Not Available |
| Ethical Approval | ✅ | Reported |

---

# Detailed Assessment

## Dataset

The dataset is described but is only available upon reasonable request to the corresponding author.

**Assessment:** Partially Reproducible.

## Data Preprocessing

The preprocessing stage is documented using Min–Max normalization.

**Assessment:** Reproducible.

## Machine Learning Model

The study employs a Random Forest classifier.

**Assessment:** Fully Reproducible.

## Hyperparameter Optimization

Grid Search is reported, but the final optimized hyperparameters are not published.

**Assessment:** Partially Reproducible.

## Validation Strategy

The evaluation uses Leave-One-Out Cross Validation (LOO-CV).

**Assessment:** Fully Reproducible.

## Performance Metrics

Reported metrics include Accuracy, Precision, Recall, F1-score, and the Confusion Matrix.

**Assessment:** Fully Reproducible.

## Statistical Reporting

The paper does not report inferential statistical tests (e.g., McNemar, Wilcoxon, Friedman, ANOVA).

**Assessment:** Not Reproducible.

## Confidence Intervals

Confidence intervals are not reported.

**Assessment:** Not Reproducible.

## Computational Environment

No information is provided regarding CPU, GPU, RAM, Python version, scikit-learn version, or operating system.

**Assessment:** Not Reproducible.

## Source Code

No public GitHub repository or executable package is provided.

**Assessment:** Not Reproducible.

---

# Reproducibility Score

| Dimension | Max | Score |
|-----------|----:|------:|
| Research Problem | 10 | 10 |
| Dataset | 10 | 7 |
| Data Preprocessing | 10 | 10 |
| Feature Engineering | 5 | 3 |
| Machine Learning Model | 10 | 10 |
| Hyperparameter Optimization | 10 | 8 |
| Validation Strategy | 10 | 10 |
| Performance Metrics | 10 | 10 |
| Statistical Analysis | 10 | 2 |
| Confidence Intervals | 5 | 0 |
| Computational Environment | 10 | 2 |
| Source Code | 10 | 0 |
| Documentation | 10 | 8 |

**Overall Score:** **80 / 120**

**Normalized Score:** **66.7 / 100**

**Overall Rating:** **Moderate Reproducibility**

---

# Strengths

- Clear research objective.
- Transparent ML workflow.
- Well-described preprocessing.
- Appropriate validation strategy.
- Suitable evaluation metrics.
- Ethical approval documented.

# Weaknesses

- No public source code.
- No random seed.
- No software versions.
- No hardware description.
- No runtime information.
- No confidence intervals.
- No statistical significance tests.
- Dataset not publicly downloadable.

---

# Recommendations

1. Publish the source code in GitHub.
2. Release an anonymized dataset.
3. Report the random seed.
4. Document software versions.
5. Describe the computational environment.
6. Report confidence intervals.
7. Include statistical significance tests.
8. Provide Docker or Conda environments.
9. Share trained models.
10. Follow ACM and NeurIPS reproducibility checklists.

---

# Conclusion

The article presents a clear Machine Learning workflow and sufficient methodological detail for partial replication. However, the absence of public code, random seeds, software versions, computational environment details, confidence intervals, and statistical significance tests prevents full computational reproducibility.

**Final Classification:** **Moderate Reproducibility (66.7/100)**

---

# Reference

> Evaluating Higher Education Performance via Machine Learning During Disruptive Times: A Case of Applied Education in Türkiye. *European Journal of Education* (2024). DOI: https://doi.org/10.1111/ejed.12805
