import re

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

def login_user(User):
    print(f"Welcome {User.username}!")
    print(" ")
    print("1. View Games Library")
    print("2. View Available Games")
    print("3. Add New Game to Library")
    print("4. View User Profile")
    print("5. Logout")
    print(" ")
    user_input = input('Please select from the options above >>> ')

def add_game_to_user_library():
    pass

def link_library_to_user():
    pass

