import re, sys
from tabulate import tabulate
from datetime import datetime
from user_functions import handle_exit

def add_to_available_games(session, Game):
    default_pattern = r'[A-Za-z0-9][A-Za-z0-9 -]{2,}$'
    genre_pattern = r'[A-Za-z][A-Za-z -]{2,}$'
    release_date_pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$"
    
    def add_game(session, game):
        session.add(game)
        session.commit()
    
    while Game:
        print("Adding Game to Store...")
        print("Please enter Q to return to main menu...")
        print(" ")

        # Game Title Entry/Validation
        
        game_title = input("Please enter the game title >>> ")
        if game_title.lower() == "q":
            return True
        while session.query(Game).filter(Game.name == game_title).first():
            print(" ")
            print("---------------------------------------")
            print("ERROR: This game is already in the store. Please enter a different game title...")
            print("---------------------------------------")
            print(" ")
            game_title = input("Please enter the game title >>> ")
            
        while not re.match(default_pattern, game_title):
            print(" ")
            print("---------------------------------------")
            print("INVALID ENTRY: Please use only letters, hyphens, or numbers...")
            print("---------------------------------------")
            print(" ")
            game_title = input("Please enter the game title >>> ")


        #Game Genre Entry/Validation
        
        game_genre = input("Please enter the game genre >>> ")
        while not re.match(genre_pattern, game_genre):
            print(" ")
            print("---------------------------------------")
            print("INVALID ENTRY: Please use only letters and hyphens...")
            print("---------------------------------------")
            print(" ")
            game_genre = input("Please enter the game genre >>> ")    
        
        
        # Game Platform Entry/Validation
        
        valid_platforms = ["NES", "SNES", "Nintendo 64", "Nintendo GameCube", 
                           "Nintendo Wii", "Nintendo Wii U", "Nintendo Switch", "Xbox",
                           "Xbox 360", "Xbox One S/X", "Xbox Series X/S", "PlayStation",
                           "PlayStation 2", "PlayStation 3", "PlayStation 4", "PlayStation 5",
                           "Windows PC", "Multiple Platforms"]
        print(" ")
        print("---------------------------------------")
        for platform in valid_platforms:
            print(f"{platform}")
        print("---------------------------------------")
        print(" ")
        game_platform = input("Please enter the game platform (select from the list above) >>> ")
        while game_platform not in valid_platforms:
            print(" ")
            print("---------------------------------------")
            print("INVALID ENTRY: Please enter a valid platform...")
            print("---------------------------------------")
            print(" ")
            game_platform = input("Please enter the game platform (select from the list above) >>> ")            
        while not re.match(default_pattern, game_platform):
            print(" ")
            print("---------------------------------------")
            print("INVALID ENTRY: Please use only letters, hyphens, or numbers...")
            print("---------------------------------------")
            print(" ")
            game_platform = input("Please enter your email address >>> ")
        
        
        # Game Release Date Entry/Validation
        
        game_release_date = input("Please enter the game's release date (mm/dd/yyyy) >>> ")
        while not re.match(release_date_pattern, game_release_date):
            print(" ")
            print("---------------------------------------")
            print("INVALID ENTRY: Please enter a date in the correct format...")
            print("---------------------------------------")
            print(" ")
            game_release_date = input("Please enter the game's release date (mm/dd/yyyy) >>> ")
        release_date = datetime.strptime(game_release_date, "%m/%d/%Y")
        
        
        # Game Publisher Entry/Validation
        
        game_publisher = input("Please enter the game's publisher >>> ")
        while not re.match(default_pattern, game_publisher):
            print(" ")
            print("---------------------------------------")
            print("INVALID ENTRY: Please use only letters, hyphens, or numbers...")
            print("---------------------------------------")
            print(" ")
            game_publisher = input("Please enter the game's publisher >>> ")
        
        print(" ")
        print("---------------------------------------")
        print(f"Game Title: {game_title}")
        print(f"Game Genre: {game_genre}")
        print(f"Game Platform: {game_platform}")
        print(f"Game Release Date: {release_date}")
        print(f"Game Publisher: {game_publisher}")
        print("---------------------------------------")
        print(" ")
        confirm = input("Is the information above correct? (y/n) >>> ")
        print(" ")
        if confirm.lower() == "n":
            print(" ")
            print("---------------------------------------")
            print("Game not added to store. Returning to admin menu...")
            print("---------------------------------------")
            print(" ")
            return True
        elif confirm.lower() == "y":
            add_game(session, Game(name=game_title, genre=game_genre, platform=game_platform, release_date=release_date, publisher=game_publisher))
            menu_return = input("Game successfully added to store! Would you like to return to the admin menu? (y/n) >>> ")
            if menu_return.lower() == "y":
                return True
            else:
                handle_exit()

def remove_from_available_games(session, Game):
    while Game:
        game_data = []
        headers = ["ID", "Name", "Genre", "Platform", "Release Date", "Publisher"]
        print(" ")
        print("Please choose from the options below...")
        print("---------------------------------------")
        print("1. Search for game by ID")
        print("2. Search for game by Title")
        print("3. Return to Admin Menu")
        print("---------------------------------------")
        print(" ")
        user_input = input("Please select the desired search option >>> ")
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
                confirm_input = input("Would you like to remove this game from the store? (y/n) >>> ")
                if confirm_input.lower() == "y":
                    print(" ")
                    print("---------------------------------------")
                    print("Removing game from store...")
                    print("---------------------------------------")
                    print(" ")
                    session.delete(game)
                    session.commit()
                    print("---------------------------------------")
                    print("Game successfully removed from the store!")
                    print("---------------------------------------")
                    print(" ")
                    return return_to_admin_menu()
                elif confirm_input.lower() == "n":
                    return handle_action_cancelled
                else:
                    return handle_invalid_entry_return
            else:
                print(" ")
                print("---------------------------------------")
                print("ERROR: Unable to locate game. Returning to admin menu...")
                print("---------------------------------------")
                print(" ")
                return True
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
                confirm_input = input("Would you like to remove this game from the store? (y/n) >>> ")
                if confirm_input.lower() == "y":
                    print(" ")
                    print("---------------------------------------")
                    print("Removing game from store...")
                    print("---------------------------------------")
                    print(" ")
                    session.delete(game)
                    session.commit()
                    print("---------------------------------------")
                    print("Game successfully removed from the store!")
                    print("---------------------------------------")
                    print(" ")
                    return return_to_admin_menu()
                elif confirm_input.lower() == "n":
                    return handle_action_cancelled
                else:
                    return handle_invalid_entry_return
            else:
                print(" ")
                print("---------------------------------------")
                print("ERROR: Unable to locate game. Returning to admin menu...")
                print("---------------------------------------")
                print(" ")
                return True
        elif user_input == "3":
            return print_to_admin_menu()
        else:
            print(" ")
            print("---------------------------------------")
            print("ERROR: Invalid Entry. Please select from options 1-3...")
            print("---------------------------------------")
            print(" ")
            continue
            
def delete_user_profile(session, User, User_library):
    while User:
        user_data = []
        headers = ["Username", "First Name", "Last Name", "Email"]
        print(" ")
        print("Please choose from the options below...")
        print("---------------------------------------")
        print("1. Search for User by Username")
        print("2. Search for User by Email")
        print("3. Return to Admin Menu")
        print("---------------------------------------")
        print(" ")
        user_input = input("Please select the desired search option >>> ")
        if user_input == "1":
            print(" ")
            search_input = input("Please enter a valid username >>> ")
            user = session.query(User).filter(User.username == search_input).first()
            if user:
                user_data.append([
                    user.username,
                    user.first_name,
                    user.last_name,
                    user.email,
                ])
                user_libraries = session.query(User_library).filter(User_library.user_id == user.id).all()
                print(" ")
                print(tabulate(user_data, headers=headers, tablefmt="pretty"))
                print(" ")
                confirm_input = input("Would you like to remove this user from the database? (y/n) >>> ")
                if confirm_input.lower() == "y":
                    print(" ")
                    print("---------------------------------------")
                    print("Removing user from the database...")
                    print("---------------------------------------")
                    print(" ")
                    for user_library in user_libraries:
                        session.delete(user_library)
                    session.delete(user)
                    session.commit()
                    print("---------------------------------------")
                    print("User successfully removed from the database!")
                    print("---------------------------------------")
                    print(" ")
                    return return_to_admin_menu()
                elif confirm_input.lower() == "n":
                    return handle_action_cancelled
                else:
                    return handle_invalid_entry_return
            else:
                print(" ")
                print("---------------------------------------")
                print("ERROR: Unable to locate user. Returning to admin menu...")
                print("---------------------------------------")
                print(" ")
                return True
        elif user_input == "2":
            print(" ")
            search_input = input("Please enter a valid email >>> ")
            user = session.query(User).filter(User.email == search_input).first()
            if user:
                user_data.append([
                    user.username,
                    user.first_name,
                    user.last_name,
                    user.email,
                ])
                print(" ")
                print(tabulate(user_data, headers=headers, tablefmt="pretty"))
                print(" ")
                confirm_input = input("Would you like to remove this user from the database? (y/n) >>> ")
                if confirm_input.lower() == "y":
                    print(" ")
                    print("---------------------------------------")
                    print("Removing user from the database...")
                    print("---------------------------------------")
                    print(" ")
                    session.delete(user)
                    session.commit()
                    print("---------------------------------------")
                    print("User successfully removed from the database!")
                    print("---------------------------------------")
                    print(" ")
                    return return_to_admin_menu()
                elif confirm_input.lower() == "n":
                    return handle_action_cancelled
                else:
                    return handle_invalid_entry_return
            else:
                print(" ")
                print("---------------------------------------")
                print("ERROR: Unable to locate user. Returning to admin menu...")
                print("---------------------------------------")
                print(" ")
                return True
        elif user_input == "3":
            return print_to_admin_menu()
        else:
            print(" ")
            print("---------------------------------------")
            print("ERROR: Invalid Entry. Please select from options 1-3...")
            print("---------------------------------------")
            print(" ")
            continue   

def update_user_profile_data(session, User):
    while User:
        user_data = []
        headers = ["Username", "First Name", "Last Name", "Email"]
        print(" ")
        print("Please choose from the options below...")
        print("---------------------------------------")
        print("1. Search for User by Username")
        print("2. Search for User by Email")
        print("3. Return to Admin Menu")
        print("---------------------------------------")
        print(" ")
        menu_input = input("Please select the desired search option >>> ")
        if menu_input == "1":
            while User:
                print(" ")
                username_pattern = r'[a-zA-Z0-9]{6,}$'
                search_input = input("Please enter a valid username >>> ")
                while not re.match(username_pattern, search_input):
                    print(" ")
                    print("---------------------------------------")
                    print("INVALID ENTRY: Please use at least 6 characters, letters, and numbers...")
                    print("---------------------------------------")
                    print(" ")
                    search_input = input("Please enter a valid username >>> ")
                user = session.query(User).filter(User.username == search_input).first()
                if user:
                    user_data.append([
                        user.username,
                        user.first_name,
                        user.last_name,
                        user.email,
                    ])
                    print(" ")
                    print(tabulate(user_data, headers=headers, tablefmt="pretty"))
                    print(" ")
                    print("Please choose from the options below...")
                    print("---------------------------------------")
                    print("1. Update Username")
                    print("2. Update Email")
                    print("3. Return to Admin Menu")
                    print("---------------------------------------")
                    print(" ")
                    submenu_input = input("Please select from the above options >>> ")
                    if submenu_input.lower() == "1":
                        while True:
                            username_pattern = r'[a-zA-Z0-9]{6,}$'
                            new_username = input("Please enter a new username >>> ")
                            while not re.match(username_pattern, new_username):
                                print(" ")
                                print("---------------------------------------")
                                print("INVALID ENTRY: Please use at least 6 characters, letters, and numbers...")
                                print("---------------------------------------")
                                print(" ")
                                new_username = input("Please enter a new username >>> ")
                            existing_user = session.query(User).filter(User.username == new_username).first()
                            if existing_user:
                                print(" ")
                                print("---------------------------------------")
                                print("ERROR: Username is unavailable. Please enter a different username...")
                                print("---------------------------------------")
                                print(" ")
                            else:
                                confirm_input = input(f"Updating username to {new_username}. Is this correct? (y/n) >>> ")
                                if confirm_input.lower() == "y":
                                    print(" ")
                                    print("---------------------------------------")
                                    print("Updating username...")
                                    print("---------------------------------------")
                                    print(" ")
                                    user.username = new_username
                                    session.commit()
                                    print("---------------------------------------")
                                    print("Username successfully updated!")
                                    print("---------------------------------------")
                                    print(" ")
                                    return return_to_admin_menu()
                                elif confirm_input.lower() == "n":
                                    return handle_action_cancelled()
                                else:
                                    return handle_invalid_entry_return()
                    elif submenu_input == "2":
                        while True:
                            email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                            new_email = input("Please enter new email address >>> ")
                            while not re.match(email_pattern, new_email):
                                print(" ")
                                print("---------------------------------------")
                                print("INVALID ENTRY: Please enter a valid email address...")
                                print("---------------------------------------")
                                print(" ")
                                new_email = input("Please enter new email address >>> ")
                            existing_user = session.query(User).filter(User.email == new_email).first()
                            if existing_user:
                                print(" ")
                                print("---------------------------------------")
                                print("ERROR: Email has already been used. Please use a different email...")
                                print("---------------------------------------")
                                print(" ")
                            else:
                                confirm_input = input(f"Updating email to {new_email}. Is this correct? (y/n) >>> ")
                                if confirm_input.lower() == "y":
                                    print(" ")
                                    print("---------------------------------------")
                                    print("Updating email...")
                                    print("---------------------------------------")
                                    print(" ")
                                    user.email = new_email
                                    session.commit()
                                    print("---------------------------------------")
                                    print("Email successfully updated!")
                                    print("---------------------------------------")
                                    print(" ")
                                    return return_to_admin_menu()
                                elif confirm_input.lower() == "n":
                                    return handle_action_cancelled()
                                else:
                                    return handle_invalid_entry_return()
                    elif submenu_input == "3":
                        return print_to_admin_menu()
                    else:
                        print(" ")
                        print("---------------------------------------")
                        print("ERROR: Invalid Entry. Please select from options 1-3...")
                        print("---------------------------------------")
                        print(" ")
                        continue
                else:
                    print(" ")
                    print("---------------------------------------")
                    print("ERROR: Unable to locate user. Returning to Admin Menu...")
                    print("---------------------------------------")
                    print(" ")
                    return True
        elif menu_input == "2":
            while User:
                print(" ")
                email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                search_input = input("Please enter a valid email address >>> ")
                while not re.match(email_pattern, search_input):
                    print(" ")
                    print("---------------------------------------")
                    print("INVALID ENTRY: Please enter a valid email address...")
                    print("---------------------------------------")
                    print(" ")
                    search_input = input("Please enter a valid email address >>> ")
                user = session.query(User).filter(User.email == search_input).first()
                if user:
                    user_data.append([
                        user.username,
                        user.first_name,
                        user.last_name,
                        user.email,
                    ])
                    print(" ")
                    print(tabulate(user_data, headers=headers, tablefmt="pretty"))
                    print(" ")
                    print("Please choose from the options below...")
                    print("---------------------------------------")
                    print("1. Update Username")
                    print("2. Update Email")
                    print("3. Return to Admin Menu")
                    print("---------------------------------------")
                    print(" ")
                    submenu_input = input("Please select from the above options >>> ")
                    if submenu_input.lower() == "1":
                        while True:
                            username_pattern = r'[a-zA-Z0-9]{6,}$'
                            new_username = input("Please enter a new username >>> ")
                            while not re.match(username_pattern, new_username):
                                print(" ")
                                print("---------------------------------------")
                                print("INVALID ENTRY: Please use at least 6 characters, letters, and numbers...")
                                print("---------------------------------------")
                                print(" ")
                                new_username = input("Please enter a new username >>> ")
                            existing_user = session.query(User).filter(User.username == new_username).first()
                            if existing_user:
                                print(" ")
                                print("---------------------------------------")
                                print("ERROR: Username is unavailable. Please enter a different username...")
                                print("---------------------------------------")
                                print(" ")
                            else:
                                confirm_input = input(f"Updating username to {new_username}. Is this correct? (y/n) >>> ")
                                if confirm_input.lower() == "y":
                                    print(" ")
                                    print("---------------------------------------")
                                    print("Updating username...")
                                    print("---------------------------------------")
                                    print(" ")
                                    user.username = new_username
                                    session.commit()
                                    print("---------------------------------------")
                                    print("Username successfully updated!")
                                    print("---------------------------------------")
                                    print(" ")
                                    return return_to_admin_menu()
                                elif confirm_input.lower() == "n":
                                    return handle_action_cancelled()
                                else:
                                    return handle_invalid_entry_return()
                    elif submenu_input == "2":
                        while True:
                            email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                            new_email = input("Please enter new email address >>> ")
                            while not re.match(email_pattern, new_email):
                                print(" ")
                                print("---------------------------------------")
                                print("INVALID ENTRY: Please enter a valid email address...")
                                print("---------------------------------------")
                                print(" ")
                                new_email = input("Please enter new email address >>> ")
                            existing_user = session.query(User).filter(User.email == new_email).first()
                            if existing_user:
                                print(" ")
                                print("---------------------------------------")
                                print("ERROR: Email has already been used. Please use a different email...")
                                print("---------------------------------------")
                                print(" ")
                            else:
                                confirm_input = input(f"Updating email to {new_email}. Is this correct? (y/n) >>> ")
                                if confirm_input.lower() == "y":
                                    print(" ")
                                    print("---------------------------------------")
                                    print("Updating email...")
                                    print("---------------------------------------")
                                    print(" ")
                                    user.email = new_email
                                    session.commit()
                                    print("---------------------------------------")
                                    print("Email successfully updated!")
                                    print("---------------------------------------")
                                    print(" ")
                                    return return_to_admin_menu()
                                elif confirm_input.lower() == "n":
                                    return handle_action_cancelled()
                                else:
                                    return handle_invalid_entry_return()
                    elif submenu_input == "3":
                        return print_to_admin_menu()
                    else:
                        print(" ")
                        print("---------------------------------------")
                        print("ERROR: Invalid Entry. Please select from options 1-3...")
                        print("---------------------------------------")
                        print(" ")
                        continue
                else:
                    print(" ")
                    print("---------------------------------------")
                    print("ERROR: Unable to locate user. Returning to Admin Menu...")
                    print("---------------------------------------")
                    print(" ")
                    return True
        elif menu_input == "3":
            return print_to_admin_menu()
        else:
            print(" ")
            print("---------------------------------------")
            print("ERROR: Invalid Entry. Please choose from options 1-3...")
            print("---------------------------------------")
            print(" ")
            continue

def view_all_users(session, User):
    users = session.query(User).all()
    headers = ["ID", "Username", "First Name", "Last Name", "Email"]
    user_data = []
    for user in users:
        user_data.append([
            user.id,
            user.username,
            user.first_name,
            user.last_name,
            user.email
        ])
    print(" ")
    print(tabulate(user_data, headers=headers, tablefmt="pretty"))
    print(" ")
    return return_to_admin_menu()

def return_to_admin_menu():
    while True:
        return_input = input("Press Y to return to Admin Menu, or press Q to quit >>> ")
        if return_input.lower() == "y":
            return True
        elif return_input.lower() == "q":
            handle_exit()
        else:
            print(" ")
            print("---------------------------------------")
            print("INVALID INPUT: Returning to Admin Menu...")
            print("---------------------------------------")
            print(" ")
            return True

def print_to_admin_menu():
    print(" ")
    print("---------------------------------------")
    print("Returning to Admin Menu...")
    print("---------------------------------------")
    print(" ")
    return True

def handle_invalid_entry_return():
    print(" ")
    print("---------------------------------------")
    print("INVALID ENTRY: Returning to Admin Menu...")
    print("---------------------------------------")
    print(" ")
    return True

def handle_action_cancelled():
    print(" ")
    print("---------------------------------------")
    print("ACTION CANCELLED: Returning to Admin Menu...")
    print("---------------------------------------")
    print(" ")
    return True