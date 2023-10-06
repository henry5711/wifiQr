from typing import Any, Coroutine, Optional
from fastapi import FastAPI,requests
from starlette.requests import Request
from config.database import SessionLocal,engine
import models,schemas
from jwt_manager import create_token,validate_token
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from routers.time import time_router
from starlette.responses import RedirectResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title= 'Qr wifi API example',
    description= 'Una API Para el manejo de una red wifi mediante qr',
    version= '0.0.1',)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
@app.get("/")
def main():
    return RedirectResponse(url="/docs/")   
app.include_router(time_router)