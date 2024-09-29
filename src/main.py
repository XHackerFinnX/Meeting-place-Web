import os

from typing import Annotated, Union, Literal
from fastapi.staticfiles import StaticFiles
from fastapi import Depends, FastAPI, Query, Path
from pydantic import BaseModel, Field

from api.v1.endpoints.router import router as router_main
from api.v1.endpoints.router_profile import router as router_profile

app = FastAPI(
    title='Место встречи'
)
app.mount(
    r"/templates/style",
    StaticFiles(directory=r"templates/style"),
    name="style_main",
)

app.mount(
    r"/templates/style",
    StaticFiles(directory=r"templates/style"),
    name="style_profile",
)

app.mount(
    "/upload", 
    StaticFiles(directory='upload'),
    name="upload"
)

app.include_router(router_main)
app.include_router(router_profile)
