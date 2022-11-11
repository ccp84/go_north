"""
Go North
A text based adventure game for Code Institute PP3
"""
from story import build_story


def display_title_screen():
    """
    Prints out the title screen of the game
    """
    print("""
     GGG    OOO    N   N   OOO   RRRR   TTTTT  H   H
    G   G  O   O   NN  N  O   O  R   R    T    H   H
    G      O   O   N N N  O   O  R   R    T    H   H
    GGGGG  O   O   N  NN  O   O  RRRR     T    HHHHH
    G   G  O   O   N   N  O   O  R R      T    H   H
    G   G  O   O   N   N  O   O  R  R     T    H   H
     GGG    OOO    N   N   OOO   R   R    T    H   H
     """)


def verify_username():
    """
    Take in username and check contents
    """
    username = input("\nWhat is your name?\n:")
    if username.isalpha():
        print(f"Hi {username}")
    else:
        print("ERROR name must contain letters only")
        verify_username()
    return username


def verify_first_choice(name):
    """
    Check user selects 1 or 2 and then respond with action
    """
    username = name
    choice = input("\n Start Game - 1   How to play - 2\n:")
    if choice == '1':
        start_game(username)
    elif choice == '2':
        display_instructions(username)
    else:
        print(f"\nERROR {choice} is an invalid choice. Please enter 1 or 2\n")
        verify_first_choice(username)


def display_instructions(name):
    """
    Prints game instructions to screen
    """
    print("""
    Follow the story.
    Select a, b, c or d at each turn.
    The right choices will promote your adventurer level.
    The wrong choice will send you back a level.
    Become a level 5 adventurer to win the game!
    """)
    verify_first_choice(name)


def start_game(username):
    """
    Builds game object and game path
    """
    print("\n New game building... \n")
    new_game = Game(username)
    print(new_game)

    while new_game.game_level < 5:
        display_option(new_game)
        handle_response(new_game)
    print(f"""

    Congratulations {username}.
    You are promoted to a top rank adventurer.
    Glory and admiration are yours.

    """)
    verify_first_choice(username)


def display_option(current_game):
    """
    Displays the current options from the Pathway object
    """
    display_level = current_game.game_level + 1
    game_path = current_game.gamepath.options[display_level]
    print(f'a {game_path["a"][0]}')
    print(f'b {game_path["b"][0]}')
    print(f'c {game_path["c"][0]}')
    print(f'd {game_path["d"][0]}')


def verify_response():
    """
    Verify user response is a b c or d
    """
    verified_option = False
    while not verified_option:
        option = input("Which path will you take?\n").lower()
        if option == "a" or option == "b" or option == "c" or option == "d":
            verified_option = True
        else:
            print(f"\nError {option} is not valid. Please enter a b c or d\n")
    return option


def handle_response(current_game):
    """
    Handles the logic of game advancement
    Call verification
    If response True is advance display next set of options
    If response is False. Game over. Take user back to start game screen.
    """
    choice = verify_response()
    current_path = current_game.gamepath.options[current_game.game_level + 1]
    outcome = current_path[choice]
    if outcome[2]:
        current_game.game_level += 1
        if current_game.game_level < 5:
            print(f"""

            {outcome[1]}
            You have been promoted to a
            level {current_game.game_level} adventurer.
            You must continue on your quest {current_game.name}!

            """)
    elif (current_game.game_level - 1) >= 0:
        current_game.game_level -= 1
        print(f"""

        {outcome[1]}
        Take heed {current_game.name},
        your adventurer level is now {current_game.game_level}.
        Loosing too many lives will cost you the game.

        """)
    else:
        print(f"""

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
