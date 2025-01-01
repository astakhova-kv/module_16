from fastapi import FastAPI, Path, status, Body, HTTPException
from typing import Annotated
from typing import List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_user_page() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
def register_user(username: str, age: int) -> User:
    new_user = User(id=len(users) + 1, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int,  user: User) -> User:
    for index, item in enumerate(users):
        if item.id == user_id:
            users[index] = user
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
def delete_user(user_id: int):
    for index, item in enumerate(users):
        if item.id == user_id:
            users.pop(index)
            return
    raise HTTPException(status_code=404, detail="User was not found")
