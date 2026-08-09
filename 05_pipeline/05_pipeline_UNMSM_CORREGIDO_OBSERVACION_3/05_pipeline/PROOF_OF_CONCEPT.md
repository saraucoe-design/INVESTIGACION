# Reproducibility Proof-of-Concept

## Status
This pipeline is a **methodological artifact** created to demonstrate reproducibility practices using Git, DVC, MLflow, fixed random seeds, stratified splitting, tests, model documentation, and a data dictionary.

It is **not an empirical-results pipeline at its current stage** because the respondent-level microdata are synthetic.

## Interpretation boundary
Any values generated for accuracy, precision, recall, F1, ROC-AUC, the confusion matrix, or the ROC curve are **demo metrics only**. They must not be interpreted as empirical findings about UNMSM, estimates of institutional quality or efficiency, evidence of causal impact, or validated comparisons among faculties or organizational units.

## What the artifact proves
The artifact demonstrates that the analytical workflow can be version controlled, reproduced from declared inputs and parameters, executed with a fixed seed and stratified split, tracked in MLflow, and audited through documented data/model definitions and tests.

## Transition to the empirical phase
Before substantive analysis, the synthetic demonstration microdata must be replaced with authorized and anonymized institutional/survey data. The final empirical dataset must follow the validated construct operationalization, ethics approval, data-management plan, and data dictionary.

Only after those requirements are satisfied may outputs be interpreted as empirical evidence, and interpretation must remain consistent with the explanatory and comparative mixed-methods case-study design.

## Presentation statement
**This pipeline is a reproducibility proof-of-concept, not an empirical result. The current microdata are synthetic and are used only to demonstrate that the analytical workflow is reproducible. In the empirical phase, the synthetic dataset will be replaced by authorized and anonymized institutional data.**
