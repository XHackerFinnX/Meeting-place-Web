from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from db.models import DataBaseUsers
router = APIRouter(
    prefix="",
    tags=["Place"]
)

templates = Jinja2Templates(directory=r"./templates")

@router.get("/")
async def get_main_place(request: Request):
    
    flag_users = await DataBaseUsers.sql_check_users(DataBaseUsers)
    
    return templates.TemplateResponse(r"index.html", {"request": request})


@router.get("/style/style.css")
async def get_style_place(request: Request):
    
    return True
