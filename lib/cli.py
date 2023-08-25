# Must be in lib directory and inside the shell to run app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import User, Game, User_library
from user_functions import (
    create_user, 
    view_user_library, 
    view_user_profile, 
    view_available_games, 
    add_game_to_user_library,
    handle_exit)
from admin_functions import (
    add_to_available_games,
    remove_from_available_games,
    delete_user_profile,
    update_user_profile_data,
    view_all_users
)

class Main:
    def __init__(self):
        self.users = [user for user in session.query(User)]
        self.games = [game for game in session.query(Game)]
        self.session = session
        self.main_menu()
     
    def main_menu(self):
        main_menu_options = {
            "1":("Login", lambda: self.handle_login(self.session)),
            "2":("Create Profile", lambda: create_user(self.session, User)),
            "3":("Admin", lambda: self.handle_admin_login(self.session)),
            "4":("Exit", lambda: handle_exit())
        }
        
        while True:
            print(" ")
            print(" ")
            print(">>> Welcome to Vapor Game Library! <<<")
            print("---------------------------------------")
            for option, (description, _) in main_menu_options.items():
                print(f"{option}. {description}")
            print("---------------------------------------")
            print(" ")
            user_choice = input("Please select one of the above options: ")
            selected_choice = main_menu_options.get(user_choice)
            if selected_choice:
                selected_choice[1]()
            else:
                print(" ")
                print("---------------------------------------")
                print("INVALID ENTRY: Please select from options 1-4...")
                print("---------------------------------------")
                print(" ")
    
    def handle_login(self, session):
        print(" ")
        user_username = input("Please enter your username >>> ")
        existing_user = session.query(User).filter(User.username == user_username).first()
        
        if existing_user is None:
            print(" ")
            print("---------------------------------------")
            print("ERROR: The username provided was not able to be located.")
            print("---------------------------------------")
            print(" ")
            go_back = input("Would you like to return to the main menu? (y/n): ")
            if go_back.lower() == "y":
                Main.main_menu(self)
            else:
                handle_exit()
        else:
            user_interface_options = {
                "1": ("View Your Game Library", lambda: view_user_library(existing_user)),
                "2": ("View Available Games", lambda: view_available_games(session, existing_user, Game)),
                "3": ("Add New Game to Your Library", lambda: add_game_to_user_library(session, existing_user, Game)),
                "4": ("View Profile Information", lambda: view_user_profile(existing_user)),
                "5": ("Logout", lambda: Main.main_menu(self))    
            }
            
            while existing_user:
                print(" ")
                print(" ")
                print(" ")
                print(f"*** Welcome to Vapor Game Library, {existing_user.username}! ***")
                print("---------------------------------------")
                for option, (description, _) in user_interface_options.items():
                    print(f"{option}. {description}")
                print("---------------------------------------")
                print(" ")
                user_input = input('Please select from the options above >>> ')
                if user_input in user_interface_options:
                    selected_choice = user_interface_options[user_input]
                    if user_input == "5":
                        selected_choice[1]()
                    else:
                        selected_choice[1]()
                        continue   
                else:
                    print(" ")
                    print("---------------------------------------")
                    print("INVALID ENTRY: Please select from options 1-5...")
                    print("---------------------------------------")
                    print(" ")
    
    def handle_admin_login(self, session):
        admin_interface_options = {
            "1": ("Add a Game to Available Games", lambda: add_to_available_games(session, Game)),
            "2": ("Remove a Game from Available Games", lambda: remove_from_available_games(session, Game)),
            "3": ("Delete User Account", lambda: delete_user_profile(session, User, User_library)),
            "4": ("Update User Account Data", lambda: update_user_profile_data(session, User)),
            "5": ("View All Users", lambda: view_all_users(session, User)),
            "6": ("Return to Main Menu", lambda: Main.main_menu(self))    
        }
        print(" ")
        print("Please enter password for admin access.")
        admin_input = input("Hint: What is synonym for vapor? >>> ")
        while True:
            if admin_input.lower() == "steam":
                print(" ")
                print("*** Vapor Library Admin Menu ***")
                print("---------------------------------------")
                for option, (description, _) in admin_interface_options.items():
                    print(f"{option}. {description}")
                print("---------------------------------------")
                print("*** CAUTION: Actions in admin will permanently alter the vapor database! ***")
                print("---------------------------------------")
                print(" ")
                admin_menu_input = input("Please select from the options above >>> ")
                if admin_menu_input in admin_interface_options:
                    selected_choice = admin_interface_options[admin_menu_input]
                    if admin_menu_input == "6":
                        print(" ")
                        print("---------------------------------------")
                        print("Returning to Main Menu...")
                        print("---------------------------------------")
                        print(" ")
                        selected_choice[1]()
                    else:
                        selected_choice[1]()
                        continue
                else:
                    print(" ")
                    print("---------------------------------------")
                    print("INVALID ENTRY: Please choose from options 1-5...")
                    print("---------------------------------------")
                    print(" ")
                    continue
            else:
                print(" ")
                print("---------------------------------------")
                print("PASSWORD ENTRY INVALID: Returning to Main Menu...")
                print("---------------------------------------")
                print(" ")
                Main.main_menu(self)               

if __name__=='__main__':
    engine = create_engine('sqlite:///db/vapor_store.db')
    
    Session = sessionmaker(bind=engine)
    session = Session()
    Main()
    