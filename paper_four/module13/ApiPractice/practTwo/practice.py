import joblib
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field
import pandas as pd
model = joblib.load("HousePrice_prediction.joblib")
app =  FastAPI()

class House(BaseModel):
    model_config = ConfigDict(extra="forbid")

    area_sqft: float = Field(ge=100, le=30000)
    bedrooms: int = Field(ge=1)
    bathrooms: int = Field(ge=1)
    age_years: float = Field(ge=0, le=100)
    distance_city_km: float = Field(ge=0)

class BatchIn(BaseModel):
    items : list[House] = Field(min_length=1, max_length=100)

class predictionOut(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    prediction_lakhs: float
    unit: str
    model_version: str

def run_inferance(items: list[House]) -> list[dict]:
    frame = pd.DataFrame([item.model_dump() for item in items])
    price = model.predict(frame)

    return (
        {"prediction_lakhs" : round(float(p), 2), "unit" : "lakh", "model_version" : "v1"}
        for p in price
    )

@app.post("/predict", response_model=predictionOut)
def predict(data: House):
    return run_inferance(data)[0]

@app.post("/predict/batch", response_model=list[predictionOut])
def predict_batch(data: BatchIn):
    return run_inferance(data.items)