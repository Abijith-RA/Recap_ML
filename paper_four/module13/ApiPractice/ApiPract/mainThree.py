from fastapi import FastAPI

app = FastAPI()

items = ["pen", "Book", "Bag"]



@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items[item_id]

@app.post("/items")
def add_item(name: str):
    items.append(name)
    return items

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    items[item_id] = name
    return items

@app.delete("/items/{item_id}")
def delet_item(item_id: int):
    items.pop(item_id)
    return items