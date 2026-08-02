# Fairness Metrics

> **Disclaimer:** The numerical examples in this document are **synthetic demonstration values** included only to illustrate how fairness metrics are interpreted in a reproducible bias audit.

## Purpose

This document defines the fairness metrics used in the bias audit and explains how they should be interpreted before and after applying a bias mitigation strategy.

---

# Evaluation Context

- **Dataset:** Adult Census Income (benchmark reference)
- **Protected Attribute:** `sex`
- **Baseline Model:** Logistic Regression
- **Mitigation:** Fairlearn ExponentiatedGradient

---

# 1. Accuracy

Measures the proportion of correctly classified instances.

**Synthetic Example**

| Before | After |
|-------:|------:|
| 0.851 | 0.842 |

Interpretation: A slight reduction in accuracy is common after introducing fairness constraints.

---

# 2. Precision

Measures the proportion of positive predictions that are correct.

| Before | After |
|-------:|------:|
| 0.844 | 0.839 |

---

# 3. Recall

Measures the proportion of actual positives correctly identified.

| Before | After |
|-------:|------:|
| 0.812 | 0.825 |

---

# 4. F1-score

Harmonic mean of Precision and Recall.

| Before | After |
|-------:|------:|
| 0.828 | 0.832 |

---

# 5. ROC-AUC

Measures ranking performance independently of a decision threshold.

| Before | After |
|-------:|------:|
| 0.903 | 0.897 |

---

# 6. Disparate Impact

Ratio between favorable outcomes for the protected and reference groups.

**Ideal value:** 1.0

| Before | After |
|-------:|------:|
| 0.63 | 0.94 |

Interpretation: Values closer to 1 indicate fairer treatment across groups.

---

# 7. Demographic Parity Difference

Difference in positive prediction rates.

**Ideal value:** 0

| Before | After |
|-------:|------:|
| 0.24 | 0.06 |

---

# 8. Demographic Parity Ratio

Ratio of positive prediction rates.

**Ideal value:** 1

| Before | After |
|-------:|------:|
| 0.67 | 0.96 |

---

# 9. Equal Opportunity Difference

Difference in True Positive Rates.

**Ideal value:** 0

| Before | After |
|-------:|------:|
| 0.18 | 0.04 |

---

# 10. Equalized Odds Difference

Difference considering both True Positive and False Positive Rates.

**Ideal value:** 0

| Before | After |
|-------:|------:|
| 0.21 | 0.05 |

---

# Summary Table

| Metric | Ideal | Synthetic Before | Synthetic After |
|---|---:|---:|---:|
| Accuracy | ↑ | 0.851 | 0.842 |
| Precision | ↑ | 0.844 | 0.839 |
| Recall | ↑ | 0.812 | 0.825 |
| F1-score | ↑ | 0.828 | 0.832 |
| ROC-AUC | ↑ | 0.903 | 0.897 |
| Disparate Impact | 1.00 | 0.63 | 0.94 |
| Demographic Parity Difference | 0.00 | 0.24 | 0.06 |
| Demographic Parity Ratio | 1.00 | 0.67 | 0.96 |
| Equal Opportunity Difference | 0.00 | 0.18 | 0.04 |
| Equalized Odds Difference | 0.00 | 0.21 | 0.05 |

---

# Overall Interpretation

The synthetic demonstration indicates that the fairness mitigation strategy substantially improves fairness metrics while producing only a minor reduction in predictive accuracy. This illustrates the typical trade-off between predictive performance and algorithmic fairness.

---

# References

- Bellamy, R. K. E., et al. (2019). *AI Fairness 360*.
- Bird, S., et al. (2020). *Fairlearn*.
- Barocas, S., Hardt, M., & Narayanan, A. (2019). *Fairness and Machine Learning*.
