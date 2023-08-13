# Build out already existing data to test methods

from models import Game, User
from datetime import datetime
from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker

print("Seeding Database...")
engine = create_engine('sqlite:///vapor_store.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()
session.query(Game).delete()

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

session.bulk_save_objects(games)
session.bulk_save_objects(users)
session.commit()

print("Seeding Complete!")
