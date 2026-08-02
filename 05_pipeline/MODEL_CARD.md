# Model card

## Model
Logistic regression with numeric standardization, missing-value imputation and one-hot encoding.

## Intended use
Demonstrate Git, DVC and MLflow reproducibility for a classifier linked to the proposed UNMSM digital-transformation study.

## Not intended for
- Ranking faculties, staff, students or programs.
- Institutional decisions using synthetic records.
- Claims about causal impact.
- Deployment before validation using authorized empirical data.

## Target
`high_quality_efficiency`: a binary demonstration outcome.

## Evaluation
Accuracy, precision, recall, F1 and ROC-AUC, plus confusion matrix and ROC curve artifacts.

## Risks
Synthetic-data artifacts, construct validity limitations, class imbalance, historical bias, omitted variables, privacy risks and inappropriate causal interpretation.
