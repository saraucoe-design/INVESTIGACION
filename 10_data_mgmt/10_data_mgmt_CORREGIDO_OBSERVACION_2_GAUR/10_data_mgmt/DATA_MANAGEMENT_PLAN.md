# Data Management Plan

## Project
Digital Transformation and Its Relationship with the Quality and Efficiency of Higher Education: An Explanatory and Comparative Case Study of the Universidad Nacional Mayor de San Marcos.

## Scope
This plan describes the collection, documentation, storage, versioning, sharing, preservation, and disposal of research data. It also establishes traceability between the study constructs, empirical measures, and analytical pipeline variables.

## Core Constructs and Measurement Traceability
The study operationalizes three central constructs: **Digital Transformation Maturity**, **Educational Quality**, and **Institutional Efficiency**. Their dimensions, indicators, planned measures, and pipeline linkages are documented in `CONSTRUCT_OPERATIONALIZATION.md` and `DATA_DICTIONARY.md`.

The required traceability chain is:

**Construct -> Dimension -> Indicator -> Survey/Institutional Measure -> Dataset Feature -> Analysis**

The exact validated instrument or maturity model, item wording, scoring procedure, coding rules, and variable names will be documented after instrument selection, expert validation, and pilot testing.

## Data Types
- Public institutional indicators (UNMSM/SUNEDU)
- Synthetic dataset for the reproducibility proof-of-concept ML pipeline
- Future anonymized survey/interview and authorized institutional data (subject to ethics approval)

## Synthetic vs. Empirical Data
The current pipeline features, including `digital_infrastructure_score`, `governance_score`, and `automation_score`, are synthetic proof-of-concept variables aligned conceptually with the research constructs. They are not validated empirical measurements and their demonstration metrics must not be interpreted as research findings. Once authorized and anonymized institutional/research data are available, empirical variables will be derived from the approved instruments and documented indicators using the mapping in the data dictionary.

## Storage
GitHub (documentation), DVC (datasets), MLflow (experiments), encrypted local backup.

## Documentation and Versioning
Each dataset version will include provenance, variable definitions, construct/dimension mapping, coding and scoring rules, missing-data handling, and the instrument or institutional source from which each empirical variable is derived. Dataset versions will be tracked with DVC and analytical experiments with MLflow.

## Retention
Research records will be retained according to institutional policy; identifiable data will not be stored in the demonstration dataset.
