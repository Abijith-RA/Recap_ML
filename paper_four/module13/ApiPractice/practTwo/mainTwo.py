import joblib
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field
import pandas as pd

model = joblib.load("HousePrice_prediction.joblib")

COLUMNS = ["area_sqft", "bedrooms", "bathrooms", "age_years", "distance_city_km"]

app = FastAPI(title="House price API")

class House(BaseModel):
    model_config = ConfigDict(extra="forbid")

    area_sqft: float = Field(ge=300, le=10000)
    bedrooms: int = Field(ge=1)
    bathrooms: int = Field(ge=1)
    age_years: float = Field(ge=0, le=100)
    distance_city_km: float = Field(ge=0)

class BatchIn(BaseModel):
    items: list[House] = Field(min_length=1, max_length=100)

class PredictionOut(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    predicted_price_lakhs: float
    unit: str
    model_version: str

def run_inference(items: list[House]) -> list[dict]:
    frame = pd.DataFrame([item.model_dump() for item in items])
    prices = model.predict(frame)
    return [
        {"predicted_price_lakhs": round(float(p), 2), "unit": "lakhs", "model_version" : "v1"}
        for p in prices
    ]

@app.post("/predict", response_model=PredictionOut)
def predict(data: House):
    return run_inference([data])[0]

@app.post("/predict/batch", response_model=list[PredictionOut])
def predict_batch(data: BatchIn):
    return run_inference(data.items)