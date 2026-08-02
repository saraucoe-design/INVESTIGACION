# Dataset Datasheet

**Following:** Gebru et al. (2021) — *Datasheets for Datasets*  
**Version:** 1.0  
**Project:** Digital Transformation and Its Impact on the Quality and Efficiency of Higher Education: A Case Study of the Universidad Nacional Mayor de San Marcos

---

# 1. Motivation

## Purpose

This dataset supports the development and validation of a reproducible Machine Learning pipeline for studying the relationship between digital transformation, educational quality, and institutional efficiency in higher education.

## Intended Tasks

- Binary classification
- Educational analytics
- Digital transformation assessment
- Reproducible ML experiments
- Teaching and research

---

# 2. Composition

## Dataset Name

UNMSM Digital Transformation Demonstration Dataset

## Version

1.0

## Number of Records

600 synthetic observations.

## Number of Variables

14 variables (11 predictors, identifiers/context variables, and one target).

## Target Variable

`high_quality_efficiency`

## Feature Summary

| Variable | Type | Description |
|---|---|---|
| record_id | String | Synthetic unique identifier |
| year | Integer | Synthetic observation year |
| faculty | Categorical | Synthetic faculty code |
| role | Categorical | Student, faculty, administrative or manager |
| digital_infrastructure_score | Numeric | Digital infrastructure availability |
| digital_competence_score | Numeric | Digital capability |
| platform_reliability_score | Numeric | Platform reliability |
| digital_governance_score | Numeric | Governance maturity |
| process_automation_score | Numeric | Automation level |
| change_readiness_score | Numeric | Organizational readiness |
| student_service_access_score | Numeric | Accessibility of digital services |
| teaching_support_quality_score | Numeric | Teaching support quality |
| user_satisfaction_score | Numeric | Satisfaction with digital services |
| processing_time_hours | Numeric | Administrative processing time |
| error_rate_pct | Numeric | Administrative error rate |
| high_quality_efficiency | Binary | Target variable |

---

# 3. Data Collection Process

No personal information was collected.

The dataset combines:

- Public institutional context from UNMSM and SUNEDU.
- Synthetic records generated exclusively for demonstrating a reproducible ML workflow.

The synthetic records do **not** correspond to real students, faculty, or administrative staff.

---

# 4. Preprocessing

The pipeline performs:

- Duplicate removal
- Missing-value validation
- Target validation
- Numeric standardization (during training)
- One-hot encoding for categorical variables
- Median and mode imputation where applicable

---

# 5. Data Quality

| Aspect | Status |
|---|---|
| Missing values | Checked during preprocessing |
| Duplicate records | Removed |
| Personal identifiers | None |
| Confidential information | None |
| Synthetic records | Yes |
| Public institutional context | Yes |

---

# 6. Distribution

The dataset is distributed exclusively for:

- Research
- Reproducibility
- Teaching
- Demonstration of ML pipelines

It must **not** be interpreted as an official UNMSM operational dataset.

---

# 7. Uses

## Appropriate Uses

- Reproducible ML experiments
- Educational data science
- Teaching Git, DVC, and MLflow
- Pipeline validation

## Inappropriate Uses

- Institutional benchmarking
- Student evaluation
- Faculty assessment
- Administrative decisions
- Accreditation evidence

---

# 8. Ethical Considerations

The dataset follows responsible AI principles:

- No personally identifiable information.
- Synthetic observations prevent disclosure risks.
- Public institutional indicators are cited as contextual information.
- Human oversight is required when adapting the pipeline to real institutional data.

---

# 9. Limitations

- Synthetic data only.
- No causal interpretation.
- Limited external validity.
- Requires validation with anonymized empirical data.
- Institutional context values should be updated when newer official reports become available.

---

# 10. Maintenance

Future releases should include:

- Real anonymized institutional datasets (with authorization).
- Updated institutional indicators.
- Expanded metadata.
- Version history.
- Data quality reports.

---

# 11. Licensing

Recommended repository license:

- Code: MIT License
- Documentation: CC BY 4.0

Users are responsible for complying with institutional policies when replacing the synthetic dataset with real data.

---

# 12. Recommended Repository Structure

```text
07_model_card/
├── MODEL_CARD.md
├── DATASET_DATASHEET.md
├── DATA_DICTIONARY.md
├── README.md
└── references.bib
```

---

# 13. References

Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., & Crawford, K. (2021). *Datasheets for Datasets*. Communications of the ACM, 64(12), 86–92. https://doi.org/10.1145/3458723

Mitchell, M., Wu, S., Zaldivar, A., et al. (2019). *Model Cards for Model Reporting*. Proceedings of the ACM Conference on Fairness, Accountability, and Transparency. https://doi.org/10.1145/3287560.3287596
