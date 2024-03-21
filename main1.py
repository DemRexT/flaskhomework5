from fastapi import FastAPI, Request
from pydantic import BaseModel
# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


    
app = FastAPI()

templates = Jinja2Templates(directory="homework5/templates")


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str 


users = []
for i in range(1, 10):
    id = i
    name = 'name' + str(i)
    email = f'email{i}@example.com'
    password = 'ok'
    user = {'id': id, 'name': name, 'email': email, 'password': password}
    users.append(user)


@app.get('/users')
async def list_user(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/users/{id}')
async def user(id: int):
    for i in range(len(users)):
        if users[i]['id'] == id:
            return {'user': users[i]}


@app.post('/users')
async def post_user(user: User):
    users.append(user)


@app.put('/users/{id}')
async def put_user(id: int, user: User):
    for i in range(len(users)):
        if users[i]['id'] == id:
            users[i] = user


@app.delete('/users/{id}')
async def del_user(id: int):
    for i in range(len(users)):
        if users[i]['id'] == id:
            users.remove(users[i])
