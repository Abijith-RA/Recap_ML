from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Api Practice")

users = {1 : {"Name" : "Abi"}}
next_id = 2

class userCreate(BaseModel):
    Name: str
 
@app.get("/")
def index():
    return {"message" : "Home page"}

@app.get("/users")
def users_list(limit : int = 10):
    return list(users.values())[:limit]

@app.get("/profile/{user_id}")
def get_user(user_id : int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User Not Found")
    user = users[user_id]
    return {"Welcome user" : user["Name"]}

@app.post("/users", status_code=201)
def create_user(user: userCreate):
    global next_id
    users[next_id] = user.model_dump()
    create = {"id": next_id, **users[next_id]}
    next_id += 1
    return create

