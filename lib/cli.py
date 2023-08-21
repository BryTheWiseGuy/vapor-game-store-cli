# Must be in lib directory and inside the shell to run app

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Game
from helpers import (
    create_user, 
    view_user_library, 
    view_user_profile, 
    view_available_games, 
    add_game_to_user_library)

class Main:
    def __init__(self):
        self.users = [user for user in session.query(User)]
        self.games = [game for game in session.query(Game)]
        self.session = session
        self.main_menu()
        
    def main_menu(self):
        print(" ")
        print(" ")
        print(">>> Welcome to Vapor Game Library! <<<")
        print("---------------------------------------")
        print("1. Login (completed/tested)")
        print("2. Create Profile (needs retested)")
        print("3. Exit (completed/tested)")
        print("---------------------------------------")
        print(" ")
        user_choice = input("Please select one of the above options: ")
        if user_choice == "1":
            Main.handle_login(self, session)
        elif user_choice == "2":
            create_user(session, User)
        elif user_choice == "3":
            print(">>> Thank you for using Vapor Game Library! <<<")
            print(" ")
            sys.exit()
        else:
            print("Invalid Entry: Please login to continue, or choose 3 to exit.")
    
    def handle_login(self, session):
        print(" ")
        user_username = input("Please enter your username >>> ")
        existing_user = session.query(User).filter(User.username == user_username).first()
        
        if existing_user is None:
            print("Sorry, the username provided was not able to be located.")
            print(" ")
            go_back = input("Would you like to return to the main menu? (y/n): ")
            if go_back.lower() == "y":
                Main.main_menu(self)
            else:
                print("Quitting program...")
                sys.exit()
        else:
            while existing_user:
                print(" ")
                print(" ")
                print(" ")
                print(f"*** Welcome to Vapor Game Library, {existing_user.username}! ***")
                print("---------------------------------------")
                print("1. View Games Library (completed/tested)")
                print("2. View Available Games (completed/tested)")
                print("3. Add New Game to Library (completed/tested)")
                print("4. View User Profile (completed/tested)")
                print("5. Logout (completed/tested)")
                print("---------------------------------------")
                print(" ")
                user_input = input('Please select from the options above >>> ')
                if user_input == "1":
                    # Completed
                    if view_user_library(existing_user):
                        continue
                elif user_input == "2":
                    # Completed
                    if view_available_games(session, existing_user, Game):
                        continue
                elif user_input == "3":
                    #Completed
                    if add_game_to_user_library(session, existing_user, Game):
                        continue
                elif user_input == "4":
                    # Completed
                    if view_user_profile(self, existing_user):
                        continue
                elif user_input == "5":
                    # Completed
                    print("Returning to main menu...")
                    Main.main_menu(self)
                else:
                    print(" ")
                    print("Invalid Entry: Please select from options 1-5...")

if __name__=='__main__':
    engine = create_engine('sqlite:///db/vapor_store.db')
    
    Session = sessionmaker(bind=engine)
    session = Session()
    Main()
    