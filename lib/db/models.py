from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///vapor_store.db')

Base = declarative_base()

class User(Base):
    __tablename__='users'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    username = Column(String())
    email = Column(String(), unique=True)

class Game(Base):
    __tablename__='games'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    genre = Column(String())
    platform = Column(String())
    release_date = Column(DateTime())
    publisher = Column(String())
    price = Column(Integer())