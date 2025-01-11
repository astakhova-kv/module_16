from fastapi import FastAPI, Path, HTTPException
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_user_page() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def register_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                        age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> dict:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[str, Path(ge=1, le=100, description='Enter User ID')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> dict:
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} has been updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(min_length=1, max_length=100, description='Enter User ID')]) -> dict:
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    users.pop(user_id)
    return f'User {user_id} has been deleted'

