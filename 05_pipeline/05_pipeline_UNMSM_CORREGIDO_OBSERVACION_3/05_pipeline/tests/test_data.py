import pandas as pd

def test_demo_dataset_schema():
    df = pd.read_csv("data/raw/unmsm_digital_transformation_demo.csv")
    assert "high_quality_efficiency" in df.columns
    assert set(df["high_quality_efficiency"].unique()).issubset({0, 1})
    assert len(df) >= 100


def test_readme_declares_proof_of_concept():
    text = open("README.md", encoding="utf-8").read().lower()
    assert "reproducibility proof-of-concept" in text
    assert "not research findings" in text or "not an empirical-results" in text
