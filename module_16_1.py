from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def adm() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def user_ids(user_id: int = 1) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user')
async def users(username: str = 'Kris', age: int = 36) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
