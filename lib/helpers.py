import re, sys
from tabulate import tabulate
from db.models import User_library

def create_user(session, User):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    name_pattern = r'[A-Za-z][A-Za-z-]{2,}$'
    username_pattern = r'[a-zA-Z0-9]{6,}$'
    
    def add_user(session, user):
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
            break
        elif confirm.lower() == "y":
            add_user(session, User(first_name=first_name, last_name=last_name, email=email, username=username))
            menu_return = input("User profile created! Would you like to return to the main menu? (y/n) >>> ")
            if menu_return.lower() == "y":
                break
            else:
                print(">>> Thank you for using Vapor Game Library! <<<")
                sys.exit()    

def view_user_library(User):
    while User:
        if User.user_library:
            user_games = []
            headers = ["ID", "Name", "Genre", "Platform", "Release Date", "Publisher"]
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
            return_input = input("Press Y to return to User Interface, or press Q to quit >>> ")
            if return_input.lower() == "y":
                return True
            elif return_input.lower() == "q":
                print(" ")
                print(">>> Thank you for using Vapor Game Library! <<<")
                print(" ")
                sys.exit()
            else:
                print("Invalid Input: Returning to User Interface...")
                print(" ")
                return True
        else:
            print(" ")
            print("---------------------------------------")
            print("User Library is empty: Please add games to your library to access this feature.")
            print("---------------------------------------")
            print(" ")
            return_input = input("Press Y to return to User Interface, or press Q to quit >>> ")
            if return_input.lower() == "y":
                return True
            elif return_input.lower() == "q":
                print(" ")
                print(">>> Thank you for using Vapor Game Library! <<<")
                print(" ")
                sys.exit()
            else:
                print("Invalid Input: Returning to User Interface...")
                print(" ")
                return True
            

# The below function is COMPLETED and TESTED
def view_available_games(session, User, Game):
    while User:
        print(" ")
        print("Searching game catalogue...")
        print("---------------------------------------")
        print("1. Display all games")
        print("2. Display games by platform")
        print("3. Return to User Interface")
        print("---------------------------------------")
        print(" ")
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
            print(" ")
            print(tabulate(game_data, headers=headers, tablefmt="pretty"))
            print(" ")
            return_input = input("Press Y to return to User Interface, or press Q to quit >>> ")
            if return_input.lower() == "y":
                return True
            elif return_input.lower() == "q":
                print(" ")
                print(">>> Thank you for using Vapor Game Library! <<<")
                print(" ")
                sys.exit()
            else:
                print(" ")
                print("Invalid Input: Returning to User Interface...")
                return True
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
            print(" ")
            print(tabulate(game_data, headers=headers, tablefmt="pretty"))
            print(" ")
            return_input = input("Press Y to return to User Interface, or press Q to quit >>> ")
            if return_input.lower() == "y":
                return True
            elif return_input.lower() == "q":
                print(" ")
                print(">>> Thank you for using Vapor Game Library! <<<")
                print(" ")
                sys.exit()
            else:
                print(" ")
                print("Invalid Input: Returning to User Interface...")
                return True
        elif search_input == "3":
            print(" ")
            print("Returning to User Interface...")
            return True
        else:
            print(" ")
            print("Invalid Entry: Returning to User Interface...")
            return True

def add_game_to_user_library(session, User, Game):
    while User:
        game_data = []
        headers = ["ID", "Name", "Genre", "Platform", "Release Date", "Publisher"]
        print(" ")
        print("Please choose from the options below...")
        print(" ")
        print("1. Search for game by ID")
        print("2. Search for game by Title")
        print("3. Return to User Interface")
        print(" ")
        user_input = input("Please select the desired search option, or press 3 to return to the user menu >>> ")
        if user_input == "1":
            print(" ")
            search_input = input("Please enter a valid game ID >>> ")
            game = session.query(Game).filter(Game.id == int(search_input)).first()
            if game:
                game_data.append([
                    game.name,
                    game.genre,
                    game.platform,
                    game.release_date,
                    game.publisher
                ])
                print(" ")
                print(tabulate(game_data, headers=headers, tablefmt="pretty"))
                print(" ")
                comfirm_input = input("Would you like to add this game to your library? (y/n) >>> ")
                if comfirm_input.lower() == "y":
                    print(" ")
                    print("Adding game to library...")
                    print(" ")
                    session.add(User_library(user=User, game=game))
                    session.commit()
                    print("Game successfully added to library!")
                    print(" ")
                    repeat_input = input("Would you like to add another game? (y/n) >>> ")
                    if repeat_input.lower() == "y":
                        continue
                    elif repeat_input.lower() == "n":
                        print(" ")
                        print("Returning to User Interface...")
                        print(" ")
                        return True
                    else:
                        print(" ")
                        print("Invalid Entry: Returning to User Interface...")
                        print(" ")
                        return True
                else:
                    print(" ")
                    print("Cancelling...")
                    continue
            else:
                print(" ")
                print("Unable to locate game: Returning to selection menu...")
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
                print(" ")
                print(tabulate(game_data, headers=headers, tablefmt="pretty"))
                print(" ")
                comfirm_input = input("Would you like to add this game to your library? (y/n) >>> ")
                if comfirm_input.lower() == "y":
                    print(" ")
                    print("Adding game to library...")
                    print(" ")
                    session.add(User_library(user=User, game=game))
                    session.commit()
                    print("Game successfully added to library!")
                    print(" ")
                    repeat_input = input("Would you like to add another game? (y/n) >>> ")
                    if repeat_input.lower() == "y":
                        continue
                    elif repeat_input.lower() == "n":
                        print(" ")
                        print("Returning to User Interface...")
                        print(" ")
                        return True
                    else:
                        print(" ")
                        print("Invalid Entry: Returning to User Interface...")
                        print(" ")
                        return True
                else:
                    print(" ")
                    print("Cancelling...")
                    continue
            else:
                print(" ")
                print("Unable to locate game: Returning to selection menu...")
                print(" ")
                continue
        elif user_input == "3":
            print(" ")
            print("Returning to User Interface")
            print(" ")
            return True
        else:
            print("Invalid Entry: Please select an option 1-3")
            continue

# The below function is COMPLETE and TESTED
def view_user_profile(self, User):
    from cli import Main
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
        return_input = input("Press Y to return to User Interface, or press Q to quit >>> ")
        if return_input.lower() == "y":
            return True
        elif return_input.lower() == "q":
            print(" ")
            print(">>> Thank you for using Vapor Game Library! <<<")
            print(" ")
            sys.exit()
        else:
            print("Invalid Input: Returning to main menu...")
            print(" ")
            Main.main_menu(self)