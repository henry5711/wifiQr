from fastapi import APIRouter
from fastapi.params import Depends
from models import Time as TimeModel
from config.database import SessionLocal,engine
from fastapi.responses import JSONResponse
import schemas
from typing import List
time_router=APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
        
#index de tiempos
@time_router.get('/times',tags=['times'],response_model=List[schemas.Time])
def get_times(db:SessionLocal=Depends(get_db)):
    times=db.query(TimeModel).all()
    return times

#tiempo detail
@time_router.get('/times/{id}',tags=['times'])
def show_times(db:SessionLocal=Depends(get_db),id:int=None):
    times=db.query(TimeModel).filter(TimeModel.id==id).first()
    return times

#guardar tiempo
@time_router.post('/times/',status_code=201,tags=['times'])
def create_times(time:schemas.Time,db:SessionLocal=Depends(get_db)):
    new_time=TimeModel(**time.model_dump()) 
    db.add(new_time)
    db.commit()
    return "time create"

#editar tiempo
@time_router.put('/times/{id}',status_code=200,tags=['times'])
def update_times(time:schemas.Time,db:SessionLocal=Depends(get_db),id:int=None):
    timeup=db.query(TimeModel).filter(TimeModel.id==id).first()
    if not timeup:
        return JSONResponse(status_code=404,content={'message':"time no encontrado"})  
    timeup.time=time.time
    db.commit()
    return JSONResponse(status_code=200,content={'message':"time actualizado"})  


#borrar tiempo
@time_router.delete('/times/{id}',tags=['times'])
def delete_times(db:SessionLocal=Depends(get_db),id:int=None):
    times=db.query(TimeModel).filter(TimeModel.id==id).first()
    if not times:
        return JSONResponse(status_code=404,content={'message':"time no encontrado"})
    db.delete(times) 
    db.commit() 
    return JSONResponse(status_code=200,content={'message':"time delete"}) 