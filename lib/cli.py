# Must be in lib directory and inside the shell to run app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Game, User_library
from helpers import create_user, login_user

class Main:
    def __init__(self):
        self.users = [user for user in session.query(User)]
        self.games = [game for game in session.query(Game)]
        self.session = session
        self.main_menu()
        
    def main_menu(self):
        while True:
            print(">>> * Welcome to Vapor Game Library! * <<<")
            print(" ")
            print("1. Login")
            print("2. Create Profile")
            print("3. Exit")
            print(" ")
            user_choice = input("Please select one of the above options: ")
            if user_choice == "1":
                Main.handle_login(self, session)
            elif user_choice == "2":
                if create_user(session, User, User_library):
                    continue
            elif user_choice == "3":
                print("Thank you for using Vapor Library!")
                break
            else:
                print("Invalid Entry: Please login to continue, or choose 3 to exit.")
    
    def handle_login(self, session):
        while True:
            print(" ")
            user_username = input("Please enter your username >>> ")
            existing_user = session.query(User).filter(User.username == user_username).first()
            
            if existing_user is None:
                print("Sorry, the username provided was not able to be located.")
                print(" ")
                go_back = input("Would you like to return to the main menu? (y/n): ")
                if go_back.lower() == "y":
                    Main.main_menu(self, session)
                else:
                    break
            else:
                login_user(session, existing_user, Game)

if __name__=='__main__':
    engine = create_engine('sqlite:///db/vapor_store.db')
    
    Session = sessionmaker(bind=engine)
    session = Session()
    Main()
    