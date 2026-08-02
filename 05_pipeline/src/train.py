from pathlib import Path
import json
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
import yaml
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, roc_curve
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def main() -> None:
    params = yaml.safe_load(Path("params.yaml").read_text(encoding="utf-8"))
    df = pd.read_csv(params["data"]["processed"])
    target = params["data"]["target"]
    id_columns = [c for c in params["data"].get("id_columns", []) if c in df.columns]

    X = df.drop(columns=[target] + id_columns)
    y = df[target].astype(int)

    categorical = X.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    numeric = [c for c in X.columns if c not in categorical]

    numeric_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])
    preprocessing = ColumnTransformer([
        ("num", numeric_pipe, numeric),
        ("cat", categorical_pipe, categorical),
    ])

    model = LogisticRegression(
        C=float(params["model"]["C"]),
        max_iter=int(params["model"]["max_iter"]),
        class_weight=params["model"]["class_weight"],
        random_state=int(params["split"]["random_state"]),
    )
    pipeline = Pipeline([("preprocess", preprocessing), ("classifier", model)])

    stratify = y if params["split"].get("stratify", True) else None
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=float(params["split"]["test_size"]),
        random_state=int(params["split"]["random_state"]),
        stratify=stratify,
    )

    mlflow.set_tracking_uri(params["mlflow"]["tracking_uri"])
    mlflow.set_experiment(params["mlflow"]["experiment_name"])

    with mlflow.start_run():
        pipeline.fit(X_train, y_train)
        pred = pipeline.predict(X_test)
        proba = pipeline.predict_proba(X_test)[:, 1]

        metrics = {
            "accuracy": float(accuracy_score(y_test, pred)),
            "precision": float(precision_score(y_test, pred, zero_division=0)),
            "recall": float(recall_score(y_test, pred, zero_division=0)),
            "f1": float(f1_score(y_test, pred, zero_division=0)),
            "roc_auc": float(roc_auc_score(y_test, proba)),
            "n_train": int(len(X_train)),
            "n_test": int(len(X_test)),
        }
        mlflow.log_params({
            "model_type": params["model"]["type"],
            "C": params["model"]["C"],
            "test_size": params["split"]["test_size"],
            "random_state": params["split"]["random_state"],
            "numeric_features": len(numeric),
            "categorical_features": len(categorical),
        })
        mlflow.log_metrics({k: v for k, v in metrics.items() if isinstance(v, float)})
        mlflow.sklearn.log_model(pipeline, artifact_path="model")

        Path("models").mkdir(exist_ok=True)
        Path("reports").mkdir(exist_ok=True)
        joblib.dump(pipeline, "models/model.joblib")
        Path("reports/metrics.json").write_text(
            json.dumps(metrics, indent=2), encoding="utf-8"
        )

        cm = confusion_matrix(y_test, pred)
        cm_rows = []
        for actual in [0, 1]:
            for predicted in [0, 1]:
                cm_rows.append({
                    "actual": actual,
                    "predicted": predicted,
                    "count": int(cm[actual, predicted])
                })
        pd.DataFrame(cm_rows).to_csv("reports/confusion_matrix.csv", index=False)

        fpr, tpr, thresholds = roc_curve(y_test, proba)
        pd.DataFrame({"fpr": fpr, "tpr": tpr, "threshold": thresholds}).to_csv(
            "reports/roc_curve.csv", index=False
        )

    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    main()
