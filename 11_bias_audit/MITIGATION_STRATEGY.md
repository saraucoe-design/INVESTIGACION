# Mitigation Strategy

> **Disclaimer:** This document contains **synthetic demonstration results** created exclusively to illustrate a reproducible bias mitigation workflow. They are not empirical results obtained from Fairlearn or AI Fairness 360.

## Project

**Digital Transformation and Its Impact on the Quality and Efficiency of Higher Education: A Case Study of the Universidad Nacional Mayor de San Marcos**

---

# 1. Purpose

This document describes the bias mitigation strategy adopted for the fairness audit. The objective is to reduce algorithmic bias while preserving acceptable predictive performance.

---

# 2. Baseline Model

| Item | Description |
|------|-------------|
| Dataset | Adult Census Income (benchmark) |
| Protected Attribute | sex |
| Target Variable | income > 50K |
| Algorithm | Logistic Regression |
| Library | Scikit-learn |

---

# 3. Why Bias Mitigation?

Historical datasets may contain structural inequalities that can be learned by Machine Learning models. Bias mitigation seeks to reduce discriminatory outcomes while maintaining useful predictive performance.

Potential risks include:

- Gender bias
- Unequal treatment
- Reduced trust in AI systems
- Ethical and legal concerns

---

# 4. Selected Mitigation Technique

## Exponentiated Gradient (Fairlearn)

Classification: **In-processing**

The Exponentiated Gradient algorithm optimizes model parameters while enforcing fairness constraints during training.

### Advantages

- Integrates with Scikit-learn
- Reproducible
- Balances fairness and accuracy
- Recommended by Fairlearn documentation

---

# 5. Fairness Constraint

The demonstration uses **Demographic Parity** as the optimization constraint.

Goal:

- Increase Disparate Impact toward 1.0
- Reduce parity differences
- Improve equal treatment of protected groups

---

# 6. Mitigation Workflow

```text
Adult Census Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Train/Test Split
        │
        ▼
Baseline Logistic Regression
        │
        ▼
Fairness Evaluation
        │
        ▼
Exponentiated Gradient
        │
        ▼
Retraining
        │
        ▼
Fairness Re-evaluation
```

---

# 7. Synthetic Before–After Results

| Metric | Before | After |
|---------|-------:|------:|
| Accuracy | 0.851 | 0.842 |
| Precision | 0.844 | 0.839 |
| Recall | 0.812 | 0.825 |
| F1-score | 0.828 | 0.832 |
| ROC-AUC | 0.903 | 0.897 |
| Disparate Impact | 0.63 | 0.94 |
| Demographic Parity Difference | 0.24 | 0.06 |
| Demographic Parity Ratio | 0.67 | 0.96 |
| Equal Opportunity Difference | 0.18 | 0.04 |
| Equalized Odds Difference | 0.21 | 0.05 |

---

# 8. Interpretation

The synthetic example shows a substantial improvement in fairness after mitigation.

- Disparate Impact approaches the ideal value of **1.0**.
- Demographic Parity Difference decreases toward **0**.
- Equal Opportunity Difference is significantly reduced.
- Equalized Odds Difference also improves.

A small reduction in predictive accuracy is expected when fairness constraints are introduced.

---

# 9. Limitations

- Demonstration uses synthetic metrics.
- Only one protected attribute is evaluated.
- Only one mitigation strategy is illustrated.
- Real performance requires executing the Fairlearn pipeline.

---

# 10. Recommendations

Future work should:

1. Compare multiple mitigation algorithms.
2. Evaluate additional protected attributes.
3. Validate results using anonymized educational datasets.
4. Incorporate continuous fairness monitoring.
5. Combine fairness with explainability techniques.

---

# 11. Conclusion

The Exponentiated Gradient strategy provides an effective framework for reducing algorithmic bias while maintaining competitive predictive performance. Although the reported values are synthetic, the workflow reflects current Responsible AI best practices.

---

# References

- Agarwal, A., Dudík, M., Wu, Z. (2018). A Reductions Approach to Fair Classification.
- Bellamy, R. K. E., et al. (2019). AI Fairness 360.
- Bird, S., et al. (2020). Fairlearn.
- Mitchell, M., et al. (2019). Model Cards for Model Reporting.
- Barocas, S., Hardt, M., & Narayanan, A. (2019). Fairness and Machine Learning.
