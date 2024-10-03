from jinja2 import Template
from typing import Annotated, Literal
from fastapi import APIRouter, Request, UploadFile, File, HTTPException, Depends, Cookie, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse
from db.session import DataBaseUsers

import shutil
import os

router = APIRouter(
    prefix="",
    tags=["Place"]
)

class ProfileUsers(BaseModel):
    name: str
    age: int = Field(ge=0, le=100)
    gender: Literal["Мужской", "Женский", "Другой"] = "Мужской"
    city: str
    about: str
    hobbies: str


UPLOAD_DIR = r"static"
os.makedirs(UPLOAD_DIR, exist_ok=True)

templates = Jinja2Templates(directory=r"./templates")


@router.get("/profile", response_class=HTMLResponse)
async def get_profile_place(request: Request):
    
    if 'user' not in request.session:
        print(HTTPException(status_code=403, detail="Необходима аутентификация"))
        return templates.TemplateResponse(r"authorization.html", {"request": request})
    
    profile_user = await DataBaseUsers.user_data(DataBaseUsers, int(request.session['user']))
    
    url_photo = f"static/{profile_user['id']}.jpg"
    
    return templates.TemplateResponse(r"profile.html", {"request": request,
                                                        "image_url": url_photo,
                                                        "profile_info": profile_user})
    

@router.post("/photo/{id}", response_class=HTMLResponse)
async def upload_file(id: int, request: Request, file: UploadFile = File(...)):

    if 'user' not in request.session:
        print(HTTPException(status_code=403, detail="Необходима аутентификация"))
        return templates.TemplateResponse(r"authorization.html", {"request": request})
    
    file_name = f"{id}.jpg"

    file_location = os.path.join(UPLOAD_DIR, file_name)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    profile_user = await DataBaseUsers.user_data(DataBaseUsers, int(request.session['user']))
    
    url_photo = f"static/{id}.jpg"

    return templates.TemplateResponse(r"profile.html", {"request": request,
                                                        "image_url": url_photo,
                                                        "profile_info": profile_user})
    
    
@router.get("/photo/static/{photo}", response_class=HTMLResponse)
async def get_static_photo(request: Request, photo: str):
    
    if 'user' not in request.session:
        print(HTTPException(status_code=403, detail="Необходима аутентификация"))
        return templates.TemplateResponse(r"authorization.html", {"request": request})
    
    profile_user = await DataBaseUsers.user_data(DataBaseUsers, int(request.session['user']))
        
    url_photo = f"static/{photo}"

    return templates.TemplateResponse(r"profile.html", {"request": request,
                                                        "image_url": url_photo,
                                                        "profile_info": profile_user})