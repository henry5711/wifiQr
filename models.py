from config.database import Base
from sqlalchemy import Column, Integer, String,Boolean,Time,TIMESTAMP,ForeignKey,DateTime
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(20))
    password = Column(String(8))
    is_active = Column(Boolean, default=True)
    

class Time(Base):
    __tablename__ = 'Time'
    id = Column(Integer,primary_key=True,index=True)
    time=Column(Integer)
    init=Column(DateTime,server_default=func.now())
    

class Conection(Base):
    __tablename__ = 'Conection'
    id = Column(Integer,primary_key=True,index=True)
    ip=Column(String(255),nullable=True)
    mac=Column(String(255),nullable=True)
    time_id=Column(ForeignKey("Time.id"))
    is_active = Column(Boolean, default=True)
    fec_conection=Column(DateTime,server_default=func.now())
    

   