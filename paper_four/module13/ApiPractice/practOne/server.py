import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

model = joblib.load("HousePrice_prediction.joblib")

app = FastAPI(title="Demo Api")

class House(BaseModel):
    area_sqft: float = Field(..., gt=0, description="The area must be greter than zero")
    bedrooms: int = Field(..., gt=0, description="Number of bedrooms must be at least 1")
    bathrooms: int = Field(..., gt=0, description="Number of bathrooms must be at least 1")
    age_years: float = Field(..., ge=0, description="Age in years cannot be negative")
    distance_city_km: float = Field(..., ge=0, description="Distance cannot be negative")
    
@app.get("/")
def index():
    return {"message" : "House Api is running"}

@app.get("/welcome")
def welcome(name: str):
    return {"Welcome" : name}

@app.post("/predict")
def predict(data: House):

    features = [
        data.area_sqft,
        data.bedrooms,
        data.bathrooms,
        data.age_years,
        data.distance_city_km,
    ]

    prediction = model.predict([features])

    return {"prediction" : round(float(prediction[0]), 2)}