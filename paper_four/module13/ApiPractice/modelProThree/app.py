from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="House API")

class House(BaseModel):
    city: str
    bedrooms: int

class HouseChange(BaseModel):
    city: str | None = None
    bedrooms: int | None = None    

houses = {1: {"city": "Kochi", "bedrooms": 3}}
next_id = 2

@app.get("/houses")
def houses_details(limit: int = 10):
    return list(houses.values())[:limit]

@app.get("/houses/{house_id}")
def get_houses(house_id: int):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not found")
    return houses[house_id]

@app.post("/houses", status_code=202)
def create_house(house: House):
    global next_id
    houses[next_id] = house.model_dump()
    created = {"id": next_id, **houses[next_id]}
    next_id += 1
    return created

@app.put("/houses/{house_id}")
def replace_house(house_id: int, house: House):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not found")
    houses[house_id] = house.model_dump()
    return houses[house_id]

@app.patch("/houses/{house_id}")
def update_house(house_id : int, changes : HouseChange):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not Found")
    houses[house_id].update(changes.model_dump(exclude_unset=True))
    return houses[house_id]

@app.delete("/houses/{house_id}", status_code=204)
def delet_house(house_id: int):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not Found")
    del houses[house_id]