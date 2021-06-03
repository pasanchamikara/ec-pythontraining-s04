from sqlalchemy import create_engine, Table, Integer, String, Column, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
    
class Items(Base):
   __tablename__ = 'items'
   
   id = Column(Integer, primary_key = True)
   name = Column(String)
   price = Column(Float)
   description = Column(String)

class Users(Base):
   __tablename__ = 'users'
   
   id = Column(Integer, primary_key = True)
   name = Column(String)
   address = Column(String)
   email = Column(String)
