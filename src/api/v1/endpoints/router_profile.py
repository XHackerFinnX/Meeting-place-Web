from jinja2 import Template
from typing import Annotated
from fastapi import APIRouter, Request, UploadFile, File, HTTPException, Depends, Cookie
from fastapi.templating import Jinja2Templates

from db.models import data_users
import shutil
import os

router = APIRouter(
    prefix="",
    tags=["Place"]
)

UPLOAD_DIR = r"static"
os.makedirs(UPLOAD_DIR, exist_ok=True)

templates = Jinja2Templates(directory=r"./templates")


@router.get("/profile")
async def get_profile_place(request: Request, username: str = Cookie(None)):
    
    profile_info = data_users
    
    url_photo = "static/1.jpg"
    
    return templates.TemplateResponse(r"profile.html", {"request": request,
                                                        "image_url": url_photo,
                                                        "profile_info": profile_info})
    

@router.post("/picture/{id}")
async def upload_file(id: int, request: Request, file: UploadFile = File(...)):
    
    file_name = f"{id}.jpg"
    
    file_location = os.path.join(UPLOAD_DIR, file_name)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    profile_info = data_users
    
    url_photo = "static/1.jpg"
    
    return templates.TemplateResponse(r"profile.html", {"request": request,
                                                        "image_url": url_photo,
                                                        "profile_info": profile_info})


@router.get("/picture/style/style_profile.css")
async def get_style_place(request: Request):
    
    return True

@router.get("/picture/upload/{id}")
async def get_jpg_place(id: str):

    return {"id": id, "picture": "ok"}

@router.get("/style/style_profile.css")
async def get_style_place(request: Request):
    
    return True

@router.get("/static/{id}")
async def get_jpg_place(id: str):

    return {"id": id}