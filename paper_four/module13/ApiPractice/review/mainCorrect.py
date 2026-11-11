import pandas as pd
import joblib
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, HTTPException, requests
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field

model = joblib.load("salary_prediction_model.joblib")

app = FastAPI(title="Salary prediction Api")

class Salary(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    experience: int = Field(ge=0, le=100)

@app.exception_handler(RequestValidationError)
async def wrong_input(request: requests, exc: RequestValidationError):
    errors = [{"field": e["loc"][-1], "message": e["msg"]} for e in exc.errors()]
    return JSONResponse(status_code=400, content={"details": "invalid Input","error": errors})

@app.get("/health", tags=["system"])
def health():
    return {"Message" : "server Live"}

@app.post("/predict")
def predictionOut(data: Salary):
    
    features = pd.DataFrame([[data.experience]])
    prediction = model.predict(features)
    
    return {"predicted Salary" : round(float(prediction[0]), 2)}