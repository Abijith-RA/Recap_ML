"""step2_server.py - Topic 2: API fundamentals. The smallest possible house API.
Run:  fastapi dev step2_server.py      (keep it running, then run step2_client.py in a 2nd terminal)
"""
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_PATH = Path(__file__).resolve().parent / "house_linear.joblib"
COLUMNS = ["area_sqft", "bedrooms", "bathrooms", "age_years", "distance_city_km"]  # same order as training

model = joblib.load(MODEL_PATH)  # load your trained model once

app = FastAPI()


class House(BaseModel):  # the JSON body we expect
    area_sqft: float
    bedrooms: int
    bathrooms: int
    age_years: float
    distance_city_km: float


@app.get("/")  # GET = read data
def index():
    return {"message": "House Price API is running"}


@app.get("/welcome")  # query parameter: /welcome?name=Asha
def welcome(name: str):
    return {"welcome": name}


@app.post("/predict")  # POST = send data in a JSON body
def predict(data: House):
    row = pd.DataFrame(
        [[data.area_sqft, data.bedrooms, data.bathrooms, data.age_years, data.distance_city_km]],
        columns=COLUMNS,
    )
    price = model.predict(row)[0]
    return {"predicted_price_lakhs": round(float(price), 2)}
