from fastapi import FastAPI

app = FastAPI()

products = {
    1: {"name": "pen", "price": 10},
    2: {"name": "Book", "price": 50},
}

@app.patch("/products/{product_id}")
def update_price(product_id: int, price: float):
    products[product_id]["price"] = price
    return products[product_id]