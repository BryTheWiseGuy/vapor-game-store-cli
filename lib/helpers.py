import re
from tabulate import tabulate
from cli import Main

def create_user(session, User, User_library):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    name_pattern = r'[A-Za-z][A-Za-z-]{2,}$'
    username_pattern = r'[a-zA-Z0-9]{6,}$'
    
    def add_user(session, user):
        new_library = User_library(user=user)
        user.library.append(new_library)
        session.add(user)
        session.commit()
    
    while User:
        print("Creating user profile...")
        print("Please enter Q to return to main menu...")
        print(" ")

        first_name = input("Please enter your first name >>> ")
        if first_name.lower() == "q":
            return True
        
        while not re.match(name_pattern, first_name):
            print("Invalid entry: Please use only letters and hyphens.")
            print(" ")
            first_name = input("Please enter your first name >>> ")

        last_name = input("Please enter your last name >>> ")
        while not re.match(name_pattern, last_name):
            print("Invalid Entry: Please use only letters and hyphens.")
            print(" ")
            last_name = input("Please enter your first name >>> ")    
        
        email = input("Please enter your email address >>> ")
        while not re.match(email_pattern, email):
            print("Invalid Entry: Please enter a valid email address.")
            print(" ")
            email = input("Please enter your email address >>> ")
        
        username = input("Please create a username >>> ")
        if session.query(User).filter(User.username == username).first():
            print("We're sorry, this username is already taken. Please choose another username.")
            print(" ")
            username = input("Please create a username >>> ")
            
        while not re.match(username_pattern, username):
            print("Invalid Entry: Please use at least 6 characters, letters, and numbers.")
            username = input("Please create a username >>> ")
        
        print(" ")
        print(f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nUsername: {username}")
        
        confirm = input("Is the information above correct? (y/n) >>> ")
        if confirm.lower() == "n":
            print("Profile was unable to be created. Returning to main menu...")
            return True
        elif confirm.lower() == "y":
            add_user(session, User(first_name=first_name, last_name=last_name, email=email, username=username))
            menu_return = input("User profile created! Would you like to return to the main menu? (y/n) >>> ")
            if menu_return.lower() == "y":
                return True
            else:
                print("Thank you for using Vapor Game Library!")
                return False      
       
# conditional statement if a use is already part of the user table

def login_user(session, User, Game):
    while User:
        print(f"Welcome {User.username}!")
        print(" ")
        print("1. View Games Library") #Incomplete
        print("2. View Available Games") # Complete
        print("3. Add New Game to Library") # Incomplete
        print("4. View User Profile") # Complete
        print("5. Logout")
        print(" ")
        user_input = input('Please select from the options above >>> ')
        if user_input == "1":
            view_user_library()
        elif user_input == "2":
            view_available_games(session, User, Game)
        elif user_input == "3":
            add_game_to_user_library()
        elif user_input == "4":
            view_user_profile(User)
        elif user_input == "5":
            print("Returning to main menu...")
            print(" ")
            Main.main_menu()
        else:
            print("Invalid Entry: Please select one of the following options: ")
            login_user(User)

def view_user_library(session, User):
    while User:
        print(" ")
        print(f"Current game library for {User.username}: ")

def view_available_games(session, User, Game):
    while User:
        print(" ")
        print("Searching game catalogue...")
        print(" ")
        print("1. Display all games")
        print("2. Display games by platform")
        print("3. Return to user menu")
        search_input = input("Please choose a search option >>> ")
        if search_input == "1":
            games = session.query(Game).all()
            headers = ["ID", "Name", "Genre", "Platform", "Release Date", "Publisher"]
            game_data = []
            for game in games:
                game_data.append([
                    game.id,
                    game.name,
                    game.genre,
                    game.platform,
                    game.release_date,
                    game.publisher
                ])
            print(tabulate(game_data, headers=headers, tablefmt="pretty"))
        elif search_input == "2":
            games = session.query(Game).all()
            headers = ["ID", "Name", "Genre", "Platform", "Release Date", "Publisher"]
            game_data = []
            platform_input=input("Please enter the desired platform >>> ")
            for game in games:
                if platform_input == game.platform:
                    game_data.append([
                        game.id,
                        game.name,
                        game.genre,
                        game.platform,
                        game.release_date,
                        game.publisher
                    ])
            print(tabulate(game_data, headers=headers, tablefmt="pretty"))
        elif search_input == "3":
            print("Returning to user menu...")
            login_user(User)
        else:
            print("Invalid Entry: Please select one of the following options: ")
            view_available_games(session, User, Game)

def add_game_to_user_library(session, User):
    print(" ")
    print("Please select a game by id number")

def view_user_profile(User):
    while User:
        headers = ["First Name", "Last Name", "Username", "Email"]
        user_data = []
        user_data.append([
            User.first_name,
            User.last_name,
            User.username,
            User.email
        ])
        print(" ")
        print(f"Account information for {User.username}: ")
        print(" ")
        print(tabulate(user_data, headers=headers, tablefmt="pretty"))
        print(" ")
        return_input = input("Press Y to return to user menu, or press Q to quit >>> ")
        if return_input.lower() == "y":
            login_user(User)
        elif return_input.lower() == "q":
            print(" ")
            print("Thank you for using Vapor Game Library!")
            break
        else:
            print("Invalid Input: Returning to main menu...")
            print(" ")
            Main.main_menu()