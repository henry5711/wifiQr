from typing import Any, Coroutine, Optional
from fastapi import FastAPI,requests
from starlette.requests import Request
from config.database import SessionLocal,engine
import models,schemas
from jwt_manager import create_token,validate_token
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from routers.time import time_router
from routers.conect import conect_router
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title= 'Qr wifi API example',
    description= 'Una API Para el manejo de una red wifi mediante qr',
    version= '0.0.1',)



# Configurar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
app.include_router(conect_router)