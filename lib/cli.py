# Must be in lib directory and inside the shell to run app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

if __name__=='__main__':
    print('Welcome to Vapor Game Shop!')
    
    