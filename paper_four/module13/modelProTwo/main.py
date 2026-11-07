from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("bankNote_Model.joblib")

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float

@app.get("/")
def index():
    return {"message" : "Home page"}

@app.get("/Welcome")
def welcome_page(name: str):
    return {"Welcome to the site" : name}

@app.post("/predict")
def prediction_bankNote(data: BankNote):
    
    prediction = model.predict([[data.variance, data.skewness, data.curtosis, data.entropy]])

    result = "Fake Note" if prediction[0] == 1 else "It's a Bank note"

    return {"prediction" : result}