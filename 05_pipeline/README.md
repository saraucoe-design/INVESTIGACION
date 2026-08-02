# 05_pipeline — Reproducible ML pipeline (Git + DVC + MLflow)

## Purpose

This repository demonstrates a reproducible classifier for the research project:

**Digital Transformation and Its Impact on the Quality and Efficiency of Higher Education: A Case Study of the Universidad Nacional Mayor de San Marcos.**

The model predicts `high_quality_efficiency` from digital-transformation, service-quality, and operational-efficiency indicators.

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
