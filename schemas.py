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
    #id:Optional[int]
    time:time
    init:Optional[datetime]

   