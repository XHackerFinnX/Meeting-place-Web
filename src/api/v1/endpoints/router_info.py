from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="",
    tags=["Place"]
)

templates = Jinja2Templates(directory=r"./templates")

@router.get("/info")
async def get_profile_place(request: Request):
    
    return templates.TemplateResponse(r"info.html", {"request": request})

@router.get("/style/style_info.css")
async def get_style_place(request: Request):
    
    return True