from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def adm() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def user_ids(user_id: Annotated[int, Path(min_length=1, max_length=100, description='Enter User ID', example='1')]) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user/{username}/{age}')
async def users(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                age: Annotated[int, Path(min_length=18, max_length=120, description='Enter age', example='24')]) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}