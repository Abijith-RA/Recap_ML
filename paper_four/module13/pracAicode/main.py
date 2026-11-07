import os
import secrets
from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import pandas as pd
from fastapi import Depends, FastAPI, HTTPException, Request, Security
from fastapi.security import APIKeyHeader
from fastapi.testclient import TestClient
from pydantic import BaseModel, ConfigDict, Field
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

MODEL_PATH = Path("iris_model.joblib")
iris = load_iris(as_frame=True)

if not MODEL_PATH.exists():
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
    )
    pipe = Pipeline([
        ("scale", StandardScaler()),
        ("model", LogisticRegression(max_iter=200)),
    ])
    joblib.dump(pipe.fit(X_train, y_train), MODEL_PATH)

API_KEY = os.environ.get("IRIS_API_KEY", "demo-key-change-me")  # demo default only
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def require_api_key(key: str | None = Security(api_key_header)):
    if key is None or not secrets.compare_digest(key.encode(), API_KEY.encode()):
        raise HTTPException(status_code=401, detail="Invalid or missing API key")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = joblib.load(MODEL_PATH)
    yield


app = FastAPI(title="Iris API", lifespan=lifespan)


class IrisInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sepal_length: float = Field(gt=0, le=10)
    sepal_width: float = Field(gt=0, le=6)
    petal_length: float = Field(gt=0, le=8)
    petal_width: float = Field(gt=0, le=4)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", dependencies=[Depends(require_api_key)])
def predict(payload: IrisInput, request: Request):
    row = pd.DataFrame(
        [[payload.sepal_length, payload.sepal_width, payload.petal_length, payload.petal_width]],
        columns=iris.feature_names,
    )
    probs = request.app.state.model.predict_proba(row)[0]
    best = int(probs.argmax())
    return {"species": str(iris.target_names[best]), "confidence": round(float(probs[best]), 3)}


if __name__ == "__main__":
    body = {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}
    with TestClient(app) as client:
        print("health, no key ->", client.get("/health").status_code)
        print("predict, no key ->", client.post("/predict", json=body).status_code)
        print("predict, wrong key ->",
              client.post("/predict", json=body, headers={"X-API-Key": "nope"}).status_code)
        print("predict, right key ->",
              client.post("/predict", json=body, headers={"X-API-Key": API_KEY}).status_code)