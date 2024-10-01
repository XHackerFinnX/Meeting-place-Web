from jinja2 import Template
from typing import Annotated, Literal
from fastapi import APIRouter, Query, Request, UploadFile, File, HTTPException, Depends, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

import shutil
import os

router = APIRouter(
    prefix="",
    tags=["Place"]
)

templates = Jinja2Templates(directory=r"./templates/menu_profile")
templates_p = Jinja2Templates(directory=r"./templates")


class ProfileUsers(BaseModel):
    name: str
    age: int = Field(ge=0, le=100)
    gender: Literal["Мужской", "Женский", "Другой"] = "Мужской"
    city: str
    about: str
    hobbies: str


@router.get("/edit_profile/{id}")
async def get_edit_profile_place(id: int, profile: Annotated[ProfileUsers, Query()], request: Request):
    
    users_profile = {
        "id": id,
        "name": profile.name,
        "age": profile.age,
        "gender": profile.gender,
        "city": profile.city,
        "about_me": profile.about,
        "hobbies": profile.hobbies
    }
    
    return templates.TemplateResponse(r"edit_profile.html", {"request": request,
                                                             "profile_info": users_profile})


@router.post("/profile/{id}")
async def post_edit_profile_place(id: int, profile: Annotated[ProfileUsers, Form(...)], request: Request):
    
    users_profile = {
        "id": id,
        "name": profile.name,
        "age": profile.age,
        "gender": profile.gender,
        "city": profile.city,
        "about_me": profile.about,
        "hobbies": profile.hobbies
    }
    
    url_photo = "static/1.jpg"
    
    return templates_p.TemplateResponse(r"profile.html", {"request": request,
                                                        "image_url": url_photo,
                                                        "profile_info": users_profile})


@router.get("/style/style_edit_profile.css")
async def get_style_place(request: Request):
    
    return True

@router.get("/profile/style/style_profile.css")
async def get_style_place(request: Request):
    
    return True

@router.get("/profile/src/upload/{id}")
async def get_style_place(id: str):
    
    return True