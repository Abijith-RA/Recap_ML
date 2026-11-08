from fastapi import FastAPI

app = FastAPI()

items = ["pen", "Book", "Bag"]

@app.get("/items")
def get_items():
    return items

