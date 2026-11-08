from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI(title="House API")


class HouseIn(BaseModel):
    city: str = Field(min_length=2, max_length=50)
    area_sqft: float = Field(gt=0)
    bedrooms: int = Field(ge=1, le=10)


class HouseOut(BaseModel):
    id: int
    city: str
    area_sqft: float
    bedrooms: int


@app.post("/houses", response_model=HouseOut, status_code=201)
def create_house(house: HouseIn):
    return {"id": 1, **house.model_dump(), "secret_note": "never sent out"}


@app.get("/houses/{house_id}", response_model=HouseOut)
def read_house(house_id: int = Path(gt=0)):
    return {"id": house_id, "city": "Kochi", "area_sqft": 1200.0, "bedrooms": 3}


@app.get("/search")
def search(city: str, limit: int = Query(default=10, ge=1, le=50)):
    return {"city": city, "limit": limit}