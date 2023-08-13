# Must be in lib directory and inside the shell to run app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Game
from helpers import create_user, login_user

class Main:
    def __init__(self):
        self.users = [user for user in session.query(User)]
        self.games = [game for game in session.query(Game)]
        self.session = session
        self.main_menu()
        
    def main_menu(self):
        print(">>> * Welcome to Vapor Game Library! * <<<")
        print(" ")
        print("1. Login")
        print("2. Exit")
        print(" ")
        user_choice = input("Please select from the above options: ")
        if user_choice == "1":
            Main.handle_login(self, session)
        elif user_choice == "2":
            print("Thank you for using Vapor Library!")
        else:
            print("Invalid Entry: Please login to continue, or choose 2 to exit.")
    
    def handle_login(self, session):
        while True:
            print(" ")
            user_username = input("Please enter your username >>> ")
            existing_user = session.query(User).filter(User.username == user_username).first()
            
            if existing_user is None:
                create_user()
            else:
                login_user(existing_user)
            
            retry = input("Do you want to retry logging in? (y/n): ")
            if retry.lower() != "y":
                break

if __name__=='__main__':
    engine = create_engine('sqlite:///db/vapor_store.db')
    
    Session = sessionmaker(bind=engine)
    session = Session()
    Main()
    