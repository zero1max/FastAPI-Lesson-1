from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class UserType(str, Enum):
    admin = 'admin'
    superuser = 'superuser'
    user = 'user'

@app.get('/role/{user_type}') 
async def get_role(user_type: UserType):
    if user_type == UserType.admin:
        return {'text': "you have admin"}
    elif user_type == UserType.superuser:
        return {'text': "you have superuser"}
    else:
        return {'text': "you have user"}
        
          

@app.get('/')
async def index():
    return {"message": "Hello, world!"}

@app.get('/user/1')
async def get_user():
    return {'id': 'pre user'}

@app.get('/user/{user_id}')
async def get_user(user_id: int):
    return {'id': user_id}

