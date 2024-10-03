from fastapi import APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="",
    tags=["Place"]
)

templates = Jinja2Templates(directory=r"./templates")

@router.get("/info", response_class=HTMLResponse)
async def get_profile_place(request: Request):
    
    if 'user' not in request.session:
        print(HTTPException(status_code=403, detail="Необходима аутентификация"))
        return templates.TemplateResponse(r"authorization.html", {"request": request})
    
    return templates.TemplateResponse(r"info.html", {"request": request})