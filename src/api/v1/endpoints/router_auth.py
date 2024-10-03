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
    

templates = Jinja2Templates(directory=r"./templates")


@router.get("/auth", response_class=HTMLResponse)
async def get_auth_place(request: Request, response: Response, session: str = Cookie(None)):
    
    return templates.TemplateResponse("authorization.html", {"request": request})


@router.post("/exit")
async def exit_user(request: Request, response: Response, session: str = Cookie(None)):
    
    if session:
        print(session)
        response.delete_cookie(key='session')
        print("Session cookie deleted")
    
    return {"Delete cookie": "ok"}