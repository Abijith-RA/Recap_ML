from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("bankNote_model.joblib")

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float	
    entropy: float

@app.get("/")
def index():
    return {"message" : "Hello World"}

@app.get("/Welcome")
def get_name(name: str):
    return {"Welcome to the learing site": name }

@app.post("/predict")
def predict_banknote(data: BankNote):
    data = data.dict()
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]

    prediction = model.predict([[variance, skewness, curtosis, entropy]])

    if(prediction[0] > 0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        "prediction" : prediction
    }