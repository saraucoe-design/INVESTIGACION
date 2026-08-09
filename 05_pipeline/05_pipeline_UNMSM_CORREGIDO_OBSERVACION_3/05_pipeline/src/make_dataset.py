from pathlib import Path
import pandas as pd
import yaml

def main() -> None:
    params = yaml.safe_load(Path("params.yaml").read_text(encoding="utf-8"))
    raw_path = Path(params["data"]["raw"])
    out_path = Path(params["data"]["processed"])
    df = pd.read_csv(raw_path)

    target = params["data"]["target"]
    if target not in df.columns:
        raise ValueError(f"Missing target column: {target}")

    # Basic reproducible validation and cleaning.
    df = df.drop_duplicates().copy()
    df = df.dropna(subset=[target])
    df[target] = df[target].astype(int)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Prepared {len(df)} records -> {out_path}")

if __name__ == "__main__":
    main()
