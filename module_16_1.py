from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def adm() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def user_ids(user_id: int = 1) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def users(username: str = 'Kris', age: int = 36) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
