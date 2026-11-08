from fastapi import FastAPI

app = FastAPI(title="Demo API")

@app.get("/")
def home():
    return{"message" : "Hello, FastAPI"}

@app.get("/health")
def health():
    return{"status": "ok"}