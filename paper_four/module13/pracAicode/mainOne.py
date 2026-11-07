from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, ConfigDict, Field

DESCRIPTION = """
Predicts iris species from flower measurements.

## Quick start

```bash
curl -X POST http://127.0.0.1:8000/v1/predict \\
  -H "Content-Type: application/json" \\
  -H "X-API-Key: YOUR_KEY" \\
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

## Errors

Every error has the shape `{"detail": "..."}`.
"""

app = FastAPI(
    title="Iris API",
    version="1.2.0",
    description=DESCRIPTION,
    docs_url="/docs",
    redoc_url="/reference",
)


class IrisInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    sepal_length: float = Field(gt=0, le=10)
    sepal_width: float = Field(gt=0, le=6)
    petal_length: float = Field(gt=0, le=8)
    petal_width: float = Field(gt=0, le=4)


class PredictionOut(BaseModel):
    species: str
    confidence: float


@app.post("/v1/predict", response_model=PredictionOut, tags=["Prediction"], summary="Predict species")
def predict_v1(payload: IrisInput):
    return PredictionOut(species="setosa", confidence=0.98)  # stub for the demo


@app.post(
    "/predict",
    response_model=PredictionOut,
    tags=["Prediction"],
    deprecated=True,
    summary="Predict species (old path, use /v1/predict)",
)
def predict_old(payload: IrisInput):
    return PredictionOut(species="setosa", confidence=0.98)  # stub for the demo


@app.get("/internal/metrics", include_in_schema=False)
def internal_metrics():
    return {"requests": 0}


if __name__ == "__main__":
    spec = app.openapi()

    print("API version:", spec["info"]["version"])
    print("Public paths:", list(spec["paths"].keys()))
    print("Internal route hidden:", "/internal/metrics" not in spec["paths"])
    print("Old route deprecated:", spec["paths"]["/predict"]["post"].get("deprecated"))
    print("Quick start in docs:", "curl -X POST" in spec["info"]["description"])

    with TestClient(app) as client:
        print("Reference page ->", client.get("/reference").status_code)
        print("Hidden route still works ->", client.get("/internal/metrics").status_code)