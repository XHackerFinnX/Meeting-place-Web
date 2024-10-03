from fastapi import Depends, HTTPException, Form, APIRouter, Request, Cookie, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Optional
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from db.session import UserAuth
from core.config import config


router = APIRouter(
    prefix="",
    tags=["Place"]
)

class User(BaseModel):
    username: str
    password: str


templates = Jinja2Templates(directory=r"./templates")

@router.post("/login")
async def login(user: User, request: Request):
    
    try:
        flag = await UserAuth.check_auth_user(UserAuth, int(user.username), user.password)
        
        if flag:
            request.session['user'] = user.username
            
            return {"message": "Успешная аутентификация"}
        
        raise HTTPException(status_code=401, detail="Неверное имя пользователя или пароль")
    except:
        raise HTTPException(status_code=401, detail="Неверное имя пользователя или пароль")