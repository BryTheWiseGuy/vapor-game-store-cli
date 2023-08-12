from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user_library = Table(
    'user_library',
    Base.metadata,
    Column('game_id', ForeignKey('games.id'), primary_key=True),
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    extend_existing=True
)

shopping_cart = Table(
    'shopping_cart',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('game_id', ForeignKey('games.id'), primary_key=True),
    extend_existing=True
)

# If multiple users are able to log into this app, would I need separate User and Users tables?
class User(Base):
    __tablename__='users'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    username = Column(String())
    email = Column(String(), unique=True)
    
    cart = relationship('Game', secondary=shopping_cart, back_populates='in_cart')
    library = relationship('Game', secondary=user_library, back_populates='in_library')
    
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
    
    in_cart = relationship('User', secondary=shopping_cart, back_populates='cart')
    in_library = relationship('User', secondary=user_library, back_populates='library')
    
    def __repr__(self):
        return f"Game id: {self.id}\n" \
            + f"Game info:\nName: {self.name}\nGenre: {self.genre}\n" \
            + f"Platform: {self.platform}\nRelease Date: {self.release_date}\n" \
            + f"Publisher: {self.publisher}\nPrice: {self.price}"