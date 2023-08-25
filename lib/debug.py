from db.models import User, Game, User_library
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import ipdb

if __name__=='__main__':
    engine = create_engine('sqlite:///db/vapor_store.db')
    
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()