import os

from typing import Annotated, Union, Literal
from fastapi.staticfiles import StaticFiles
from fastapi import Depends, FastAPI, Query, Path, Request, HTTPException, Cookie, Response
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

from starlette.middleware.sessions import SessionMiddleware
from core.config import config
from api.v1.endpoints.router import router as router_main
from api.v1.endpoints.router_profile import router as router_profile
from api.v1.endpoints.router_info import router as router_info
from api.v1.endpoints.router_edit_profile import router as router_edit_profile
from api.v1.endpoints.router_authorization import router as router_login
from api.v1.endpoints.router_auth import router as router_auth


app = FastAPI(
    title='Место встречи'
)

app.mount(
    r"/static",
    StaticFiles(directory='static'),
    name="static"
)

app.include_router(router_auth)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def add_session_middleware(secret_key: str, cookie_name: str, max_age: int):
    app.add_middleware(
        SessionMiddleware,
        secret_key=secret_key,
        session_cookie=cookie_name,
        max_age=max_age
    )

add_session_middleware(config.SECRET_AUTH.get_secret_value(), "session", 3600)


app.include_router(router_login)
app.include_router(router_main)
app.include_router(router_profile)
app.include_router(router_edit_profile)
app.include_router(router_info)
