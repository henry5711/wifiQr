from fastapi import APIRouter,Request
from fastapi.params import Depends
from models import Conection as ConectionModel
from config.database import SessionLocal,engine
from fastapi.responses import JSONResponse
import schemas
from typing import List
from requests import Session
from bs4 import BeautifulSoup
conect_router=APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


#index de tiempos
@conect_router.get('/conection',tags=['conection'],response_model=List[schemas.Conection],)
def get_conection(db:SessionLocal=Depends(get_db)):
    conection=db.query(ConectionModel).all()
    return conection

#tiempo detail
@conect_router.get('/conection/{id}',tags=['conection'])
def show_conection(db:SessionLocal=Depends(get_db),id:int=None):
    conection=db.query(ConectionModel).filter(ConectionModel.id==id).first()
    return conection

#guardar tiempo
@conect_router.post('/conection/',status_code=201,tags=['conection'])
def create_conection(request: Request,Conection:schemas.Conection,db:SessionLocal=Depends(get_db)):
    new_Conection=ConectionModel(**Conection.model_dump()) 
    db.add(new_Conection)
    db.commit()
    return "Conection create"

#editar tiempo
@conect_router.put('/conection/{id}',status_code=200,tags=['conection'])
def update_conection(Conection:schemas.Conection,db:SessionLocal=Depends(get_db),id:int=None):
    Conectionup=db.query(ConectionModel).filter(ConectionModel.id==id).first()
    if not Conectionup:
        return JSONResponse(status_code=404,content={'message':"Conection no encontrado"})  
    Conectionup.Conection=Conection.Conection
    db.commit()
    return JSONResponse(status_code=200,content={'message':"Conection actualizado"})  


#borrar tiempo
@conect_router.delete('/conection/{id}',tags=['conection'])
def delete_conection(db:SessionLocal=Depends(get_db),id:int=None):
    conection=db.query(ConectionModel).filter(ConectionModel.id==id).first()
    if not conection:
        return JSONResponse(status_code=404,content={'message':"Conection no encontrado"})
    db.delete(conection) 
    db.commit() 
    return JSONResponse(status_code=200,content={'message':"Conection delete"}) 


#desconectar tiempo
@conect_router.put('/conection/desactive/{id}',status_code=200,tags=['conection'])
def desactive_conection(db:SessionLocal=Depends(get_db),id:int=None):
    Conectionup=db.query(ConectionModel).filter(ConectionModel.id==id).first()
    if not Conectionup:
        return JSONResponse(status_code=404,content={'message':"Conection no encontrado"})  
    Conectionup.is_active=False
    db.commit()
    
    
    
    # Obtén la dirección IP del router
    router_ip = "192.168.0.1"

    # Inicializa una sesión con el router
    session = requests.Session()

    # Inicia sesión en el router
    login_url = "http://{}/login.html".format(router_ip)
    login_data = {
        "username": "admin",
        "password": "admin",
    }
    session.post(login_url, data=login_data)
    # Desconecta al usuario.
    url = f"http://{router_ip}/user/disconnect.cgi?mac=f6:d4:fe:82:40:9b"
    return url
    session.post(url)
    session.close()
    return JSONResponse(status_code=200,content={'message':"Conection actualizado"})






