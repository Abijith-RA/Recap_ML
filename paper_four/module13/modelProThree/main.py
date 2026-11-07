from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="House API")   # create the app


# ---------- MODELS (shape of data) ----------

class House(BaseModel):            # used for POST and PUT
    city: str                      # both fields are REQUIRED
    bedrooms: int


class HouseUpdate(BaseModel):      # used for PATCH
    city: str | None = None        # optional: may be missing
    bedrooms: int | None = None    # optional: may be missing


# ---------- FAKE DATABASE ----------

houses: dict[int, dict] = {1: {"city": "Kochi", "bedrooms": 3}}
# key = house id, value = house data

next_id = 2                        # the id the NEXT new house will get


# ---------- GET ALL ----------

@app.get("/houses")
def list_houses(limit: int = 10):  # limit comes from ?limit=5 (default 10)
    return list(houses.values())[:limit]
    # houses.values() = all house data
    # list(...)       = turn into a list
    # [:limit]        = take only the first `limit` items


# ---------- GET ONE ----------

@app.get("/houses/{house_id}")
def get_house(house_id: int):
    if house_id not in houses:     # check it EXISTS first
        raise HTTPException(status_code=404, detail="House not found")
    return houses[house_id]        # exists, so return it


# ---------- POST (create) ----------

@app.post("/houses", status_code=201)   # 201 = "created"
def create_house(house: House):         # JSON body must match House
    global next_id                      # we want to CHANGE the outer variable
    houses[next_id] = house.model_dump()    # save as dict under new id
    created = {"id": next_id, **houses[next_id]}   # response includes the id
    next_id += 1                        # next house gets a new id
    return created


# ---------- PUT (replace everything) ----------

@app.put("/houses/{house_id}")
def replace_house(house_id: int, house: House):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not found")
    houses[house_id] = house.model_dump()   # old data fully overwritten
    return houses[house_id]


# ---------- PATCH (change only some fields) ----------

@app.patch("/houses/{house_id}")
def update_house(house_id: int, changes: HouseUpdate):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not found")
    houses[house_id].update(changes.model_dump(exclude_unset=True))
    # exclude_unset=True -> include ONLY fields the client actually sent
    # .update(...)       -> change just those fields, keep the rest
    return houses[house_id]


# ---------- DELETE ----------

@app.delete("/houses/{house_id}", status_code=204)   # 204 = "done, no content"
def delete_house(house_id: int):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not found")
    del houses[house_id]           # remove it; nothing is returned