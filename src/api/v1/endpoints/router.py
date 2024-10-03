from fastapi import APIRouter, Request, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from db.session import DataBaseUsers

router = APIRouter(
    prefix="",
    tags=["Place"]
)


templates = Jinja2Templates(directory=r"./templates")

@router.get("/", response_class=HTMLResponse)
async def get_main_place(request: Request):
    
    if 'user' not in request.session:
        print(HTTPException(status_code=403, detail="Необходима аутентификация"))
        return templates.TemplateResponse(r"authorization.html", {"request": request})

    if await DataBaseUsers.user_check(DataBaseUsers, int(request.session['user'])):
        await DataBaseUsers.user_add_login_id(DataBaseUsers, int(request.session['user']))
    
    return templates.TemplateResponse(r"index.html", {"request": request})
