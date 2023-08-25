import re, sys
from tabulate import tabulate
from db.models import User_library

# Look into using a dictionary to update table rows

def create_user(session, User):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    name_pattern = r'[A-Za-z][A-Za-z-]{2,}$'
    username_pattern = r'[a-zA-Z0-9]{6,}$'
    
    def add_user(session, user):
        session.add(user)
        session.commit()
    
    while User:
        print("Creating user profile...")
        print("Please enter Q at any time to return to main menu...")
        print(" ")

        first_name = input("Please enter your first name >>> ")
        if first_name.lower() == "q":
            return True
        
        while not re.match(name_pattern, first_name):
            print(" ")
            print("---------------------------------------")
            print("INVALID ENTRY: Please use only letters and hyphens...")
            print("---------------------------------------")
            print(" ")
            first_name = input("Please enter your first name >>> ")
            
        last_name = input("Please enter your last name >>> ")
        if last_name.lower() == "q":
            return True
        while not re.match(name_pattern, last_name):
            print(" ")
            print("---------------------------------------")
            print("INVALID ENTRY: Please use only letters and hyphens...")
            print("---------------------------------------")
            print(" ")
            last_name = input("Please enter your last name >>> ")    
        
        email = input("Please enter your email address >>> ")
        if email.lower() == "q":
            return True
        while session.query(User).filter(User.email == email).first():
            print(" ")
            print("---------------------------------------")
            print("ERROR: This email has already been used. Please use another email...")
            print("---------------------------------------")
            print(" ")
            email = input("Please enter your email address >>> ")
        
        while not re.match(email_pattern, email):
            print(" ")
            print("---------------------------------------")
            print("INVALID ENTRY: Please enter a valid email address...")
            print("---------------------------------------")
            print(" ")
            email = input("Please enter your email address >>> ")
        
        username = input("Please create a username >>> ")
        if username.lower() == "q":
            return True
        while session.query(User).filter(User.username == username).first():
            print(" ")
            print("---------------------------------------")
            print("ERROR: This username is already taken. Please choose another username...")
            print("---------------------------------------")
            print(" ")
            username = input("Please create a username >>> ")
            
        while not re.match(username_pattern, username):
            print(" ")
            print("---------------------------------------")
            print("INVALID ENTRY: Please use at least 6 characters, letters, and numbers...")
            print("---------------------------------------")
            print(" ")
            username = input("Please create a username >>> ")
        
        print(" ")
        print("---------------------------------------")
        print(f"First Name: {first_name}\nLast Name: {last_name}\nEmail: {email}\nUsername: {username}")
        print("---------------------------------------")
        print(" ")
        confirm = input("Is the information above correct? (y/n) >>> ")
        if confirm.lower() == "n":
            return handle_action_cancelled()
        elif confirm.lower() == "y":
            add_user(session, User(first_name=first_name, last_name=last_name, email=email, username=username))
            menu_return = input("User profile created! Would you like to return to the main menu? (y/n) >>> ")
            if menu_return.lower() == "y":
                return True
            else:
                handle_exit()

def view_user_library(User):
    while User:
        if User.user_library:
            user_games = []
            headers = ["Name", "Genre", "Platform", "Release Date", "Publisher"]
            print(" ")
            print(f"Current game library for {User.username}: ")
            print(" ")
            for game in User.user_library:
                user_games.append([
                    game.game.name,
                    game.game.genre,
                    game.game.platform,
                    game.game.release_date,
                    game.game.publisher
                ])
            print(tabulate(user_games, headers=headers, tablefmt="pretty"))
            print(" ")
            return return_to_user_interface()
        else:
            print(" ")
            print("---------------------------------------")
            print("ERROR: User Library is empty. Please add games to your library to access this feature.")
            print("---------------------------------------")
            print(" ")
            return return_to_user_interface()
            

# The below function is COMPLETED and TESTED
def view_available_games(session, User, Game):
    while User:
        print(" ")
        print("Available Display Options...")
        print("---------------------------------------")
        print("1. Display all games")
        print("2. Display games by platform")
        print("3. Return to User Interface")
        print("---------------------------------------")
        print(" ")
        search_input = input("Please select the desired display option >>> ")
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
            print(" ")
            print(tabulate(game_data, headers=headers, tablefmt="pretty"))
            print(" ")
            return return_to_user_interface()
        elif search_input == "2":
            games = session.query(Game).all()
            headers = ["ID", "Name", "Genre", "Platform", "Release Date", "Publisher"]
            game_data = []
            platform_input=input("Please enter the desired platform >>> ")
            platform_exists = session.query(Game).filter(Game.platform == platform_input).first()
            if platform_exists:
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
                print(" ")
                print(tabulate(game_data, headers=headers, tablefmt="pretty"))
                print(" ")
                return return_to_user_interface()
            else:
                print(" ")
                print("---------------------------------------")
                print("INVALID ENTRY: Please enter a valid platform...")
                print("---------------------------------------")
                print(" ")
                continue
        elif search_input == "3":
            return print_to_user_interface()
        else:
            return handle_invalid_entry_return()

def add_game_to_user_library(session, User, Game):
    while User:
        game_data = []
        headers = ["ID", "Name", "Genre", "Platform", "Release Date", "Publisher"]
        print(" ")
        print("Available Search Options...")
        print("---------------------------------------")
        print("1. Search for game by ID")
        print("2. Search for game by Title")
        print("3. Return to User Interface")
        print("---------------------------------------")
        print(" ")
        user_input = input("Please select the desired search option >>> ")
        if user_input == "1":
            print(" ")
            search_input = input("Please enter a valid game ID >>> ")
            game = session.query(Game).filter(Game.id == int(search_input)).first()
            if game:
                game_data.append([
                    game.id,
                    game.name,
                    game.genre,
                    game.platform,
                    game.release_date,
                    game.publisher
                ])
                user_game_exists = session.query(User_library).filter_by(user=User, game=game).first()
                if not user_game_exists:
                    print(" ")
                    print(tabulate(game_data, headers=headers, tablefmt="pretty"))
                    print(" ")
                    comfirm_input = input("Would you like to add this game to your library? (y/n) >>> ")
                    if comfirm_input.lower() == "y":
                        print(" ")
                        print("---------------------------------------")
                        print("Adding game to library...")
                        print("---------------------------------------")
                        print(" ")
                        session.add(User_library(user=User, game=game))
                        session.commit()
                        print("---------------------------------------")
                        print("Game successfully added to library!")
                        print("---------------------------------------")
                        print(" ")
                        repeat_input = input("Would you like to add another game? (y/n) >>> ")
                        if repeat_input.lower() == "y":
                            continue
                        elif repeat_input.lower() == "n":
                            return print_to_user_interface()
                        else:
                            return handle_invalid_entry_return()
                    else:
                        return handle_action_cancelled()
                else:
                    print(" ")
                    print("---------------------------------------")
                    print("This game is already in your game library!")
                    print("---------------------------------------")
                    print(" ")
                    continue
            else:
                print(" ")
                print("---------------------------------------")
                print("Unable to locate game: Returning to selection menu...")
                print("---------------------------------------")
                print(" ")
                continue
        elif user_input == "2":
            print(" ")
            search_input = input("Please enter a valid game title >>> ")
            game = session.query(Game).filter(Game.name == search_input).first()
            if game:
                game_data.append([
                    game.name,
                    game.genre,
                    game.platform,
                    game.release_date,
                    game.publisher
                ])
                user_game_exists = session.query(User_library).filter_by(user=User, game=game).first()
                if not user_game_exists:
                    print(" ")
                    print(tabulate(game_data, headers=headers, tablefmt="pretty"))
                    print(" ")
                    comfirm_input = input("Would you like to add this game to your library? (y/n) >>> ")
                    if comfirm_input.lower() == "y":
                        print(" ")
                        print("---------------------------------------")
                        print("Adding game to library...")
                        print("---------------------------------------")
                        print(" ")
                        session.add(User_library(user=User, game=game))
                        session.commit()
                        print("---------------------------------------")
                        print("Game successfully added to library!")
                        print("---------------------------------------")
                        print(" ")
                        repeat_input = input("Would you like to add another game? (y/n) >>> ")
                        if repeat_input.lower() == "y":
                            continue
                        elif repeat_input.lower() == "n":
                            return print_to_user_interface()
                        else:
                            return handle_invalid_entry_return()
                    else:
                        return handle_action_cancelled()
                else:
                    print(" ")
                    print("---------------------------------------")
                    print("This game is already in your game library!")
                    print("---------------------------------------")
                    print(" ")
                    continue
            else:
                print(" ")
                print("---------------------------------------")
                print("ERROR: Unable to locate game. Returning to selection menu...")
                print("---------------------------------------")
                print(" ")
                continue
        elif user_input == "3":
            return print_to_user_interface()
        else:
            print(" ")
            print("---------------------------------------")
            print("INVALID ENTRY: Please select an option 1-3")
            print("---------------------------------------")
            print(" ")
            continue

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
        print(" ")
        print(" ")
        print(f"*** Account information for {User.username} ***")
        print("---------------------------------------")
        print(" ")
        print(tabulate(user_data, headers=headers, tablefmt="pretty"))
        print(" ")
        return return_to_user_interface()
    
# *** DRY Code Functions Below *** #

def return_to_user_interface():
    while True:
        return_input = input("Press Y to return to User Interface, or press Q to quit >>> ")
        if return_input.lower() == "y":
            return True
        elif return_input.lower() == "q":
            print(" ")
            print("---------------------------------------")
            print(">>> Thank you for using Vapor Game Library! <<<")
            print("---------------------------------------")
            print(" ")
            sys.exit()
        else:
            print(" ")
            print("---------------------------------------")
            print("INVALID INPUT: Returning to User Interface...")
            print("---------------------------------------")
            print(" ")
            return True

def handle_exit():
    print(" ")
    print("---------------------------------------")
    print(">>> Thank you for using Vapor Game Library! <<<")
    print("---------------------------------------")
    print(" ")
    sys.exit()

def print_to_user_interface():
    print(" ")
    print("---------------------------------------")
    print("Returning to User Interface...")
    print("---------------------------------------")
    print(" ")
    return True

def handle_invalid_entry_return():
    print(" ")
    print("---------------------------------------")
    print("INVALID ENTRY: Returning to User Interface...")
    print("---------------------------------------")
    print(" ")
    return True

def handle_action_cancelled():
    print(" ")
    print("---------------------------------------")
    print("ACTION CANCELLED: Returning to User Interface...")
    print("---------------------------------------")
    print(" ")
    return True