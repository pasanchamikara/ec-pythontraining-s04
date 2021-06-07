from config.dbconfig import engine

from sqlalchemy import create_engine, Table, Integer, String, Column, Float
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()
    
class Items(Base):
   __tablename__ = 'items'
   
   id = Column(Integer, primary_key = True)
   name = Column(String(50))
   price = Column(Float)
   description = Column(String(50))

Base.metadata.create_all(engine)

