from fastapi import FastAPI, HTTPException
from typing import List
from .models import User

app = FastAPI()

users: List[User] = []

@app.get("/users", response_model=List[User])
def list_users():
    return users

@app.post("/users", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for u in users:
        if u.id == user_id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated: User):
    for idx, u in enumerate(users):
        if u.id == user_id:
            users[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for idx, u in enumerate(users):
        if u.id == user_id:
            del users[idx]
            return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="User not found")
