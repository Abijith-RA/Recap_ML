import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict
import pandas as pd

model = joblib.load("HousePrice_prediction.joblib")
COLUMNS = ['area_sqft', 'bedrooms', 'bathrooms', 'age_years', 'distance_city_km']

app = FastAPI(title="House price Api", description="House price prediction in lakhs.", version="1.0.0")

@app.get("/")
def index():
    return {"Message" : "Home page"}

@app.get("/health", tags=["System"], summary="Health check")
def health():
    """return ok while the service is alive"""
    return {"return" : "ok"}

listing = {1: {"title": "2BHK near park", "sold": False}}
next_id = 2

@app.get("/listing", tags=["listings"])
def list_listing():
    return listing

@app.get("/listing", tags=["listings"])
def get_listing(listing_id: int):
    return listing[listing_id]

@app.post("/listing", tags=["listings"])
def create_listing(title: str):
    global next_id
    listing[next_id] = {"title": title, "sold" : False}
    next_id += 1
    return listing

@app.put("/listing/{listing_id}", tags=["listings"])
def replace_listing(listing_id: int, title: str, sold: bool):
    listing[listing_id] = {"title": title, "sold": sold}
    return listing[listing_id]

@app.patch("/listing/{listing_id}", tags=["listings"])
def update_listing(listing_id: int, sold: bool):
    listing[listing_id]["sold"] = sold
    return listing[listing_id]

@app.delete("/listing/{listing_id}", tags=["listings"])
def delete_listing(listing_id: int):
    listing.pop(listing_id)
    return listing

@app.get("/welcome", tags=["params"])
def welcome(name: str):
    return {"Welcome": name}

@app.get("/hello/{name}", tags=["params"])
def hello(name: str):
    return {"hello": name}

class House(BaseModel):
    
        model_config = ConfigDict(extra="forbid")
    
        area_sqft: float = Field(ge=200, le=10000)
        bedrooms: int = Field(ge=1)
        bathrooms: int = Field(ge=1)
        age_years: float = Field(ge=0, le=100)
        distance_city_km: float = Field(ge=0)

@app.post("/predict", tags=["prediction"], summary="predict house price")
def predict(data: House):
    """send 5 measurements, The replay get predicted price in lakh"""
    features = pd.DataFrame(
        [[data.area_sqft, data.bedrooms, data.bathrooms, data.age_years, data.distance_city_km]],
        columns=COLUMNS
    )
    predicted_value = model.predict(features)
    return {"prediction_price_lakhs": round(float(predicted_value[0]), 2)}