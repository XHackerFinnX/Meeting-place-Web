from jinja2 import Template
from typing import Annotated, Literal
from fastapi import APIRouter, Query, Request, UploadFile, File, HTTPException, Depends, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse
from db.session import DataBaseUsers, UserPay

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


@router.get("/edit_profile/{id}", response_class=HTMLResponse)
async def get_edit_profile_place(id: int, profile: Annotated[ProfileUsers, Query()], request: Request):
    
    if 'user' not in request.session:
        print(HTTPException(status_code=403, detail="Необходима аутентификация"))
        return templates_p.TemplateResponse(r"authorization.html", {"request": request})
    
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


@router.post("/save/{id}", response_class=HTMLResponse)
async def post_edit_profile_place(id: int, request: Request, profile: Annotated[ProfileUsers, Form(...)]):

    if 'user' not in request.session:
        print(HTTPException(status_code=403, detail="Необходима аутентификация"))
        return templates_p.TemplateResponse(r"authorization.html", {"request": request})

    users_profile = {
        "id": id,
        "name": profile.name,
        "age": profile.age,
        "gender": profile.gender,
        "city": profile.city,
        "about_me": profile.about,
        "hobbies": profile.hobbies
    }
    
    balance_user = await UserPay.user_balance(UserPay, int(request.session['user']))

    users_profile.update(balance_user)
    
    await DataBaseUsers.user_full_add(DataBaseUsers, int(users_profile['id']), users_profile['name'], int(users_profile['age']), users_profile['gender'], users_profile['city'], users_profile['about_me'], users_profile['hobbies'])
    
    url_photo = f"static/{id}.jpg"

    return templates_p.TemplateResponse(r"profile.html", {"request": request,
                                                        "image_url": url_photo,
                                                        "profile_info": users_profile})
    
@router.get("/save/static/{photo}", response_class=HTMLResponse)
async def get_static_photo(request: Request, photo: str):

    if 'user' not in request.session:
        print(HTTPException(status_code=403, detail="Необходима аутентификация"))
        return templates_p.TemplateResponse(r"authorization.html", {"request": request})

    url_photo = f"static/{photo}"

    return url_photo