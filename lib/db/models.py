from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class User_library(Base):
#     __tablename__='user_library'
    
#     id = Column(Integer(), primary_key=True)
#     user_id = Column(Integer(), ForeignKey('users.id'), unique=True)
#     game_id = Column(Integer(), ForeignKey('games.id'), unique=True)
#     user = relationship('User', back_populates='library')

# If multiple users are able to log into this app, would I need separate User and Users tables?
class User(Base):
    __tablename__='users'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    username = Column(String(), unique=True, nullable=False)
    email = Column(String(), unique=True, nullable=False)
    # library = relationship('user_library', uselist=False, back_populates='users')
    
    def __repr__(self):
        return f"{self.id}:\n" \
            + f"{self.first_name} {self.last_name}\n" \
            + f"{self.username}\n" \
            + f"{self.email}\n" \
            + f"Games in shopping cart: {self.cart}\n" \
            + f"Games in library: {self.library}"

class Game(Base):
    __tablename__='games'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    genre = Column(String())
    platform = Column(String())
    release_date = Column(DateTime())
    publisher = Column(String())
    price = Column(Integer())
    
    def __repr__(self):
        return f"Game id: {self.id}\n" \
            + f"Game info:\nName: {self.name}\nGenre: {self.genre}\n" \
            + f"Platform: {self.platform}\nRelease Date: {self.release_date}\n" \
            + f"Publisher: {self.publisher}\nPrice: {self.price}"