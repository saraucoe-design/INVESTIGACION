# 05_pipeline — Reproducibility Proof-of-Concept (Git + DVC + MLflow)

## Purpose

This repository is a **reproducibility proof-of-concept**, not an empirical-results package. It demonstrates how the future analytical workflow can be versioned, reproduced, audited, and tracked for the research project:

**Digital Transformation and Its Impact on the Quality and Efficiency of Higher Education: A Case Study of the Universidad Nacional Mayor de San Marcos.**

For demonstration purposes only, the classifier predicts `high_quality_efficiency` from synthetic digital-transformation, service-quality, and operational-efficiency indicators. **Any accuracy, precision, recall, F1, ROC-AUC, confusion-matrix, or ROC-curve values produced by this pipeline are demonstration metrics and are NOT research findings about UNMSM.**

## Proof-of-concept status — read before interpreting outputs

**Current status: METHODOLOGICAL ARTIFACT / REPRODUCIBILITY PROOF-OF-CONCEPT.**

The purpose of this pipeline is to demonstrate that the proposed analysis **will be reproducible** once authorized, anonymized institutional data replace the synthetic demonstration microdata.

- Outputs under `reports/`, `models/`, and `mlruns/` are technical demonstration artifacts.
- Demo metrics must **not** be reported as empirical findings, institutional performance estimates, or evidence of an effect/association at UNMSM.
- The current model must **not** be used to rank faculties, students, staff, programs, or administrative units.
- Substantive interpretation begins only after ethics/institutional authorization, construct validation, anonymization, and replacement of the synthetic file with empirical data.

See `PROOF_OF_CONCEPT.md` for the interpretation boundary and transition to the empirical phase.

## Critical data statement

- `data/raw/unmsm_institutional_context.csv` contains **published aggregate UNMSM figures** with source URLs and reference years.
- `data/raw/unmsm_digital_transformation_demo.csv` is **synthetic demonstration microdata** generated for pipeline testing. It is not an official UNMSM respondent-level dataset and must not be interpreted as empirical findings.
- Replace the synthetic file with authorized, anonymized survey and institutional records before substantive analysis.

## Public sources represented

1. SUNEDU institutional licensing report: historical baseline on students, programs, faculty, infrastructure, research outputs and patents.
2. UNMSM official institutional portal: reports, regulations, PEI/POI monitoring and services.
3. UNMSM digital systems: research information, virtual education, quality assurance, telematics and digital document management.

## Structure

```text
05_pipeline/
├── data/
│   ├── raw/
│   │   ├── unmsm_institutional_context.csv
│   │   └── unmsm_digital_transformation_demo.csv
│   ├── processed/
│   └── source_catalog.csv
├── src/
│   ├── make_dataset.py
│   └── train.py
├── models/
├── reports/
├── tests/
├── dvc.yaml
├── params.yaml
├── requirements.txt
└── README.md
```

## Quick start

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
git init
dvc init
dvc repro
mlflow ui --backend-store-uri ./mlruns
```

Open the MLflow interface at `http://127.0.0.1:5000`.

## Manual execution without DVC

```bash
python src/make_dataset.py
python src/train.py
```

## DVC workflow

```bash
dvc add data/raw/unmsm_digital_transformation_demo.csv
git add data/raw/unmsm_digital_transformation_demo.csv.dvc .gitignore
git commit -m "Track demo dataset with DVC"

dvc repro
git add dvc.yaml dvc.lock params.yaml reports models
git commit -m "Run reproducible classifier pipeline"
```

## Replace demonstration data

Provide a CSV with the same target column:

```text
high_quality_efficiency
```

The training script automatically handles numeric and categorical predictors. Remove direct identifiers and obtain ethics/institutional authorization before using respondent-level records.
