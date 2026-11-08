import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message" : "Hello, stranger"}

@app.get("/Welcome")
def get_name(name : str):
    return {"welcome To my site" : f"{name}"}