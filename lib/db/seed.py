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
        genre="Action RPG",
        platform="Multiple Platforms",
        release_date=datetime(
            year=2020,
            month=9,
            day=28
        ),
        publisher="MiHoyo"
    ),
    Game(
        name="Final Fantasy XVI",
        genre="Action RPG",
        platform="Playstation 5",
        release_date=datetime(
            year=2023,
            month=6,
            day=22
        ),
        publisher="Square Enix"
    ),
    Game(
        name="The Legend of Zelda: Tears of the Kingdom",
        genre="Action-Adventure",
        platform="Nintendo Switch",
        release_date=datetime(
            year=2023,
            month=5,
            day=12
        ),
        publisher="Nintendo"
    ),
    Game(
        name="Diablo IV",
        genre="ARPG Hack and Slash",
        platform="Multiple Platforms",
        release_date=datetime(
            year=2023,
            month=6,
            day=5
        ),
        publisher="Blizzard Entertainment"
    ),
    Game(
        name="Hogwarts Legacy",
        genre="Action RPG",
        platform="Multiple Platforms",
        release_date=datetime(
            year=2023,
            month=2,
            day=10
        ),
        publisher="Warner Bros. Games"
    ),
    Game(
        name="The Legend of Zelda: Breathe of the Wild",
        genre="Action-Adventure",
        platform="Nintendo Switch",
        release_date=datetime(
            year=2017,
            month=3,
            day=3
        ),
        publisher="Nintendo"
    ),
    Game(
        name="Elden Ring",
        genre="Action RPG",
        platform="Multiple Platforms",
        release_date=datetime(
            year=2022,
            month=2,
            day=25
        ),
        publisher="FromSoftware"
    ),
    Game(
        name="Horizon: Forbidden West",
        genre="Action RPG",
        platform="PlayStation 5",
        release_date=datetime(
            year=2022,
            month=2,
            day=18
        ),
        publisher="Sony Interactive Entertainment"
    ),
    Game(
        name="Baldur's Gate 3",
        genre="Role-Playing",
        platform="Windows PC",
        release_date=datetime(
            year=2023,
            month=8,
            day=3
        ),
        publisher="Larian Studios"
    ),
    Game(
        name="God of War: Ragnarok",
        genre="Action-Adventure",
        platform="Multiple Platforms",
        release_date=datetime(
            year=2022,
            month=11,
            day=9
        ),
        publisher="Sony Interactive Entertainment"
    ),
    Game(
        name="Valheim",
        genre="Survival Sandbox",
        platform="Windows PC",
        release_date=datetime(
            year=2021,
            month=2,
            day=2
        ),
        publisher="Mihoyo"
    ),
    Game(
        name="Returnal",
        genre="Roguelike Shooter",
        platform="PlayStation 5",
        release_date=datetime(
            year=2021,
            month=4,
            day=30
        ),
        publisher="Sony Interactive Entertainment"
    ),
    Game(
        name="Hollow Knight",
        genre="Metroidvania",
        platform="Multiple Platforms",
        release_date=datetime(
            year=2017,
            month=2,
            day=24
        ),
        publisher="Team Cherry"
    ),
    Game(
        name="Ori and the Will of the Wisps",
        genre="Metroidvania",
        platform="Multiple Platforms",
        release_date=datetime(
            year=2020,
            month=3,
            day=11
        ),
        publisher="Xbox Game Studios"
    ),
    Game(
        name="Cyberpunk 2077",
        genre="Action RPG",
        platform="Multiple Platforms",
        release_date=datetime(
            year=2020,
            month=12,
            day=10
        ),
        publisher="CD Projekt"
    ),
    Game(
        name="Doom Eternal",
        genre="First Person Shooter",
        platform="Multiple Platforms",
        release_date=datetime(
            year=2020,
            month=3,
            day=20
        ),
        publisher="Bethesda Softworks"
    ),
    Game(
        name="Final Fantasy VII Remake",
        genre="Action RPG",
        platform="PlayStation 5",
        release_date=datetime(
            year=2020,
            month=4,
            day=10
        ),
        publisher="Square Enix"
    ),
    Game(
        name="Valorant",
        genre="Tactical Shooter",
        platform="Windows PC",
        release_date=datetime(
            year=2020,
            month=6,
            day=2
        ),
        publisher="Riot Games"
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
    User_library(user=users[1], game=games[2]),
    User_library(user=users[0], game=games[2])
]

session.add_all(games)
session.add_all(users)
session.add_all(user_libraries)
session.commit()

print("Seeding Complete!")
