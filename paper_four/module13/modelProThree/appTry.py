from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="House Api learn")

houses = {1: {"city" : "Kochi", "bedroom" : 3}}
next_id = 2

class House(BaseModel):
    city: str
    bedroom: int

class HouseChnage(BaseModel):
    city: str | None = None
    bedroom: int | None = None    

@app.get("/houses")
def list_houses(limit: int = 10):
    return list(houses.values())[:limit]

@app.get("/houses{house_id}")
def house_details(house_id: int):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not Found")
    return houses[house_id]

@app.post("/houses", status_code=202)
def create_house(house: House):
    global next_id
    houses[next_id] = house.model_dump()
    create = {"id" : next_id, **houses[next_id]}
    next_id += 1
    return create

@app.put("/houses/{house_id}")
def replace_houses(house_id: int, house: House):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not Found")
    houses[house_id] = house.model_dump()
    return houses[house_id]

@app.patch("/houses/{house_id}")
def update_houses(house_id: int, change: HouseChnage):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not Found")
    houses[house_id].update(change.model_dump(exclude_unset=True))
    return houses[house_id]

@app.delete("/houses/{house_id}")
def delete_houses(house_id: int):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="house not found")
    del houses[house_id]