import logging
import time

import joblib
from fastapi import FastAPI, HTTPException, APIRouter, response, Header
from pydantic import BaseModel, ConfigDict, Field
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("practTwo")

model = joblib.load("HousePrice_prediction.joblib")
MODEL_VERSION = "v1"

app = FastAPI(title="House price API", version="1.0.0")

class House(BaseModel):
    model_config = ConfigDict(extra="forbid")

    area_sqft: float = Field(ge=200, le=10000)
    bedrooms: int = Field(ge=1, le=10)
    bathrooms: int = Field(ge=1, le=10)
    age_years: float = Field(ge=0, le=100)
    distance_city_km: float = Field(ge=0, le=100)

class BatchIn(BaseModel):
    items: list[House] =Field(min_length=1, max_length=100)

class predictionOut(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    prediction_lakhs: float
    model_version: str
    request_id: str
    latency_ms: float

router = APIRouter(prefix="/v1", tags=["Prediction"])

@router.post("/predict", response_model=predictionOut)
def predict(
    data: House,
    response: response,
    round_to: int = 2,
    x_request_id: str | None = Header(default=None)
):
    start = time.pref_counter()
    try:
        row = pd.DataFrame([data.model_dump()])
        price = float(model.predict(row)[0])
    except Exception:
            logger.exception("prediction failed")
            raise HTTPException(status_code=500, detail="prediction failed , please try again later")