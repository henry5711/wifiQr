from typing import Optional
from pydantic import BaseModel
from datetime import datetime, time, timedelta,date

class User(BaseModel):
    id:Optional[int]
    username:str
    nombre:str
    rol:str
    estado:int

class Time(BaseModel):
    id:Optional[int]
    time:int
    init:Optional[datetime]


class Conection(BaseModel):
    id:Optional[int]
    ip:Optional[str]
    mac:Optional[str]
    time_id:int
    is_active :Optional[bool] 
    fec_conection:Optional[datetime]