import logging
import time
import uuid

import joblib
import pandas as pd
from fastapi import APIRouter, FastAPI, Header, HTTPException, Response
from pydantic import BaseModel, ConfigDict, Field

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("house-api")

# ---------- 5a: load the model ONCE, at the top of the file ----------
model = joblib.load("HousePrice_prediction.joblib")
COLUMNS = ["area_sqft", "bedrooms", "bathrooms", "age_years", "distance_city_km"]
MODEL_VERSION = "v1"

app = FastAPI(title="House Price API", version="1.0.0")


# ---------- input and output classes ----------
class House(BaseModel):
    model_config = ConfigDict(extra="forbid")

    area_sqft: float = Field(ge=200, le=10000)
    bedrooms: int = Field(ge=1, le=10)
    bathrooms: int = Field(ge=1, le=10)
    age_years: float = Field(ge=0, le=100)
    distance_city_km: float = Field(ge=0, le=100)


class BatchIn(BaseModel):
    items: list[House] = Field(min_length=1, max_length=100)


class PredictionOut(BaseModel):  # 5c: prediction + metadata
    model_config = ConfigDict(protected_namespaces=())

    predicted_price_lakhs: float
    model_version: str
    request_id: str
    latency_ms: float


# ---------- 5e: router = a group of endpoints under /v1 ----------
router = APIRouter(prefix="/v1", tags=["Prediction"])


@router.post("/predict", response_model=PredictionOut)  # 5a: the prediction endpoint
def predict(
    data: House,                                       # 5b: body
    response: Response,
    round_to: int = 2,                                 # 5b: query parameter  ?round_to=1
    x_request_id: str | None = Header(default=None),   # 5b: header  X-Request-ID
):
    start = time.perf_counter()
    try:
        row = pd.DataFrame([data.model_dump()], columns=COLUMNS)
        price = float(model.predict(row)[0])
    except Exception:
        logger.exception("Prediction failed")  # 5d: full details only in the server log
        raise HTTPException(status_code=500, detail="Prediction failed. Please try again later.")

    response.headers["X-Model-Version"] = MODEL_VERSION  # 5c: metadata in a header
    return {
        "predicted_price_lakhs": round(price, round_to),
        "model_version": MODEL_VERSION,
        "request_id": x_request_id or str(uuid.uuid4()),
        "latency_ms": round((time.perf_counter() - start) * 1000, 2),
    }


@router.post("/predict/batch")  # 5b: many houses in one request
def predict_batch(data: BatchIn, round_to: int = 2):
    try:
        frame = pd.DataFrame([item.model_dump() for item in data.items], columns=COLUMNS)
        prices = model.predict(frame)
    except Exception:
        logger.exception("Batch prediction failed")
        raise HTTPException(status_code=500, detail="Prediction failed. Please try again later.")
    return {"predictions": [round(float(p), round_to) for p in prices], "model_version": MODEL_VERSION}


app.include_router(router)


@app.get("/health", tags=["System"])
def health():
    return {"status": "ok"}


# ---------- 5d: error handling, a clean 404 ----------
MODEL_REGISTRY = {"house_linear": {"version": MODEL_VERSION, "task": "regression"}}


@app.get("/models/{name}", tags=["Models"])
def get_model_info(name: str):
    if name not in MODEL_REGISTRY:
        raise HTTPException(status_code=404, detail=f"Model '{name}' not found")  # client error
    return MODEL_REGISTRY[name]