import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

model = joblib.load("salary_prediction_model.joblib")

app = FastAPI(title="Salary prediction Api")

class Salary(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    experience: int = Field(ge=0, le=100)
    

@app.get("/health", tags=["system"])
def health():
    return {"Message" : "server Live"}

@app.post("/predict")
def predictionOut(data: Salary):
    if data.experience != int:
        raise HTTPException(status_code=422, detail="Data type error")
    
    features = pd.DataFrame([[data.experience]])
    prediction = model.predict(features)
    
    return {"predicted Salary" : round(float(prediction[0]), 2)}