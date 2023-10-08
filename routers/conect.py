from fastapi import APIRouter
from fastapi.params import Depends
from models import Conection as ConectionModel
from config.database import SessionLocal,engine
from fastapi.responses import JSONResponse
import schemas
from typing import List
conect_router=APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


#index de tiempos
@conect_router.get('/conection',tags=['conection'],response_model=List[schemas.Time])
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
def create_conection(time:schemas.Time,db:SessionLocal=Depends(get_db)):
    conection=db.query(ConectionModel).count()
    #validar de que solo exista un tiempo almacenado
    if conection >=1:
      return JSONResponse(status_code=404,content={'message':"ya existe un time registrado"}) 
    new_time=ConectionModel(**time.model_dump()) 
    db.add(new_time)
    db.commit()
    return "time create"

#editar tiempo
@conect_router.put('/conection/{id}',status_code=200,tags=['conection'])
def update_conection(time:schemas.Time,db:SessionLocal=Depends(get_db),id:int=None):
    timeup=db.query(ConectionModel).filter(ConectionModel.id==id).first()
    if not timeup:
        return JSONResponse(status_code=404,content={'message':"time no encontrado"})  
    timeup.time=time.time
    db.commit()
    return JSONResponse(status_code=200,content={'message':"time actualizado"})  


#borrar tiempo
@conect_router.delete('/conection/{id}',tags=['conection'])
def delete_conection(db:SessionLocal=Depends(get_db),id:int=None):
    conection=db.query(ConectionModel).filter(ConectionModel.id==id).first()
    if not conection:
        return JSONResponse(status_code=404,content={'message':"time no encontrado"})
    db.delete(conection) 
    db.commit() 
    return JSONResponse(status_code=200,content={'message':"time delete"}) 