from sqlalchemy import create_engine, Table, Integer, String, Column, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
    
class Items(Base):
   __tablename__ = 'items'
   
   id = Column(Integer, primary_key = True)
   name = Column(String)
   price = Column(Float)
   description = Column(String)

print(Items.__table__)

# Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()
result = session.query(Items).all()

for row in result:
   print ("Name: ",row.name, "Price:",row.price, "Description:",row.description)