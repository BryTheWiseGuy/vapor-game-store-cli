# Vapor Game Store CLI

## Description

Vapor Game Store CLI is a command line interface made with Python and SQLAlchemy. The application is modeled as video game store. Users can create a profile, login to view currently available games, view their game library, add or remove games from their game library, and view their profile information. The application also incorporates administrative actions, where an administrative user can add or remove games from the list of available games in the database, delete or update a users profile in the database, or view a list of all user profiles that have been created.

## Visuals

## Installation

**NOTE:** Python v3.8 is required to use this application. Please see the official Python documentation for instructions on how to ensure Python v3.8 is installed and configured on your machine

To install and use this application, please follow the steps below:

    1. Fork this repository, and clone it to your own virtual environment
    2. Once cloning is complete, navigate to the directory and run `pipenv install`
        - This should install ipdb, alembic, sqlalchemy, and tabulate v0.9.0
    3. Once dependencies are installed open up the code in your preferred editor
    4. Run `pipenv shell` to enter into the Python shell
    5. The database should have a fresh seed already applied, but to run a new seed move down into lib/db by entering `cd lib/db` and run `python seed.py`
        - CAUTION: Running a new database seed will clear out any information added to the database since the last database seed
    6. Once confirmation of the database seed is received, enter `cd ..` to move back into the lib directory and run `python cli.py` to start the application

## Usage

**NOTE:** This section will be broken down by individual file, outlining the main purpose of each file and breaking down each individual function. If you decide to implement additional features and encounter any bugs, run the `debug.py` file while in the lib directory to enter into ipdb and begin debugging code. 

### What Goes into a README?

This README should serve as a template for your own- go through the important
files in your project and describe what they do. Each file that you edit
(you can ignore your Alembic files) should get at least a paragraph. Each
function should get a small blurb.

You should descibe your actual CLI script first, and with a good level of
detail. The rest should be ordered by importance to the user. (Probably
functions next, then models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

***

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you
off to a good start with your Phase 3 Project.

Happy coding!

***

## Resources

- [Setting up a respository - Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
