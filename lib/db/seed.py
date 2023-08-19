# Build out already existing data to test methods

from models import Game, User, User_library
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print("Seeding Database...")
engine = create_engine('sqlite:///vapor_store.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()
session.query(Game).delete()
session.query(User_library).delete()

games = [
    Game(
        name="Hades",
        genre="Roguelike",
        platform="Multiple Platforms",
        release_date=datetime(
                year=2020,
                month=8,
                day=17
            ),
        publisher="Supergiant Games",
    ),
    Game(
        name="Animal Crossing: New Horizons",
        genre="Life Simulation",
        platform="Nintendo Switch",
        release_date=datetime(
                year=2020,
                month=3,
                day=20
            ),
        publisher="Nintendo",
    ),
    Game(
        name="Genshin Impact",
        genre="Gacha",
        platform="Multiple Platforms",
        release_date=datetime(
            year=2020,
            month=1,
            day=1
        ),
        publisher="Mihoyo"
    )
]

users = [
    User(
       first_name="John",
       last_name="Doe",
       username="jdoe123",
       email="johndoe22@models.com"
    ),
    User(
       first_name="Jane",
       last_name="Doe",
       username="jane123",
       email="janedoe22@models.com"
    )
]

user_libraries=[
    User_library(user=users[1], game=games[0]),
    User_library(user=users[0], game=games[1]),
    User_library(user=users[1], game=games[2])
]

session.add_all(games)
session.add_all(users)
session.add_all(user_libraries)
session.commit()

print("Seeding Complete!")
