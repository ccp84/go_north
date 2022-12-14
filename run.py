"""
Go North
A text based adventure game for Code Institute PP3
"""
from story import build_story
import os


def display_title_screen():
    """
    Prints out the title screen of the game
    """
    print("""
     GGG    OOO    N   N   OOO   RRRR   TTTTT  H   H
    G   G  O   O   NN  N  O   O  R   R    T    H   H
    G      O   O   N N N  O   O  R   R    T    H   H
    G GGG  O   O   N  NN  O   O  RRRR     T    HHHHH
    G   G  O   O   N   N  O   O  R R      T    H   H
    G   G  O   O   N   N  O   O  R  R     T    H   H
     GGG    OOO    N   N   OOO   R   R    T    H   H
     """)
    print("""
    Welcome to the room Adventurer!
    Your challenge, should you accept, is to
    advance to a level 5 adventurer and escape.
    Choose your options carefully.
    Loot or cheat codes will advance your adventurer level.
    Monsters and curses will send you backwards...
    ... or worse.
     """)


def clear_terminal():
    """
    Function to clear previous terminal entries from the screen
    Code used from answer found on stack overflow here:
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python

    """
    os.system('cls' if os.name == 'nt' else 'clear')


def verify_username():
    """
    Takes in username
    Verifies input is a valid username,
    or returns an error and loops the user back to the input.
    Returns username once valid entry has been gained.
    """
    # Set check indicator to true while name is being verified
    name_check = True
    while name_check:
        username = input("\nWhat is your name?\n:")
        if username.isalpha():
            print(f"Hi {username}, welcome to the room")
            """
            Once name is verified as being valid,
            Set check indicator to false, this will
            break the loop and return the username
            allowing game flow to continue.
            """
            name_check = False
        else:
            print("ERROR name must contain letters only")
    return username


def verify_first_choice(name):
    """
    Check user selects 1 or 2 and then respond with action
    """
    username = name
    choice = input("\n Start Game - 1   How to play - 2   Exit - 3\n:")
    if choice == '1':
        start_game(username)
    elif choice == '2':
        display_instructions(username)
    elif choice == '3':
        main()
    else:
        # Handle invalid input if not 1, 2 or 3
        print(f"\nERROR {choice} is an invalid choice. Enter 1, 2 or 3\n")
        verify_first_choice(username)


def display_instructions(name):
    """
    Prints game instructions to screen
    """
    clear_terminal()
    print("""
    Your challenge is to escape the room.
    You start as a level 0 adventurer. Become a level 5
    adventurer to escape!
    There are 4 options each time you step forwards A, B, C or D.
    You should choose an option you think will help you progress.
    'Loot' and 'Cheat Codes' will move you up a level, 'Monsters and
    'Curses' will send you back a level.
    If you go below level 0 - all lives are lost.
    Disputes can be settled by loudly arguing,
    the game developer has the final word.
    """)
    verify_first_choice(name)


def start_game(username):
    """
    Builds game object and game path
    Handles game loop while user gains levels
    Returns user to the start game option once level 5 reached
    """
    clear_terminal()
    print("\n New game building... \n")
    # Build new game object
    new_game = Game(username)
    print(new_game)
    # Start main game loop up to level 5
    while new_game.game_level < 5:
        display_option(new_game)
        handle_response(new_game)
    # Display winning message once level 5 is hit
    print(f"""
    Congratulations {username}.
    You are promoted to a top rank adventurer.
    Glory and admiration are yours.

    """)
    # Return user to start menu
    verify_first_choice(username)


def display_option(current_game):
    """
    Displays the current options from the Pathway object
    """
    display_level = current_game.game_level + 1
    # Get the list of options at the index of the current display level
    game_path = current_game.gamepath.options[display_level]
    print("Which choice will you make?\n")
    print(f'A {game_path["a"][0]}')
    print(f'B {game_path["b"][0]}')
    print(f'C {game_path["c"][0]}')
    print(f'D {game_path["d"][0]}')
    print('\nX Exit to menu')


def verify_response():
    """
    Verify user response is a b c d or x
    """
    # Set check variable
    verified_option = False
    while not verified_option:
        # Accept upper or lower case by converting before verification
        option = input("\n:").lower()
        if (option == "a" or option == "b" or option == "c" or option == "d"
                or option == "x"):
            # Confirm verified input and break the loop
            verified_option = True
        else:
            # Display error and loop user back to input again
            print(f"\nError {option} not valid. Enter A, B, C, D or X only\n")
    return option


def handle_response(current_game):
    """
    Handles the logic of game advancement
    Call verification
    If response True is advance display next set of options
    If response is False go backwards a level.
    Game level -1 = break loop and return to start
    """
    # Get verified user response
    choice = verify_response()
    # Exit response - clear screen and return to start
    if choice == "x":
        clear_terminal()
        main()
    else:
        # Set path to the list indexed by current level +1
        path = current_game.gamepath.options[current_game.game_level + 1]
        # Set outcome to the key 'choice' in the path dictionary
        outcome = path[choice]
        # If the outcome = true go up a level
        if outcome[2]:
            current_game.game_level += 1
            # If level is less than 5, continue playing
            if current_game.game_level < 5:
                clear_terminal()
                print(f"""

{outcome[1]}
You have been promoted to a level {current_game.game_level} adventurer.
You must continue on your quest {current_game.name}!

                """)
            else:
                clear_terminal()
                print(f"""
{outcome[1]}
            """)
        # If outcome is false but lives remain, give a warning
        elif (current_game.game_level - 1) >= 0:
            current_game.game_level -= 1
            clear_terminal()
            print(f"""

{outcome[1]}
Take heed, your adventurer level is now {current_game.game_level}.
Loosing too many lives will cost you the game {current_game.name}.

        """)
        # Lives now <0 print end of game message and return to start
        else:
            clear_terminal()
            print(f"""
{outcome[1]}
Your adventurer level is reduced beyond 0, no lives remain.
Better luck next time {current_game.name}.

            """)
            verify_first_choice(current_game.name)


def main():
    """
    Initiates main gameflow
    """
    display_title_screen()
    username = verify_username()
    verify_first_choice(username)


class Game:
    """
    Builds a new Game
    """

    def __init__(self, name):
        self.name = name
        self.game_level = 0
        self.gamepath = Pathway()

    def __repr__(self):
        return "\nYou awake to find yourself in a dark room...\n"


class Pathway:
    """
    Builds a new path through the game
    Contains a list of 5 lists with 4 sets of options in each
    Pulls options from pathway file to build option sets at random
    """

    def __init__(self):
        self.options = build_story()


main()
