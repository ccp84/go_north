def display_title_screen():
    """
    Prints out the title screen of the game
    """
    print("Title screen function running")


def verify_username():
    """
    Take in username and check contents
    """
    print("Username verification running")


def verify_first_choice():
    """
    Check user selects 1 or 2 and then respond with action
    """
    choice = input("Start Game - 1   How to play - 2\n ")
    if int(choice) == 1:
        start_game()
    elif int(choice) == 2:
        display_instructions()
    else:
        print("ERROR please enter 1 or 2")
        verify_first_choice()


def display_instructions():
    """
    Prints game instructions to screen
    """
    print("Game Instructions here")
    verify_first_choice()


def start_game():
    """
    Builds game object and game path
    """
    print("New game building...")
    new_game = Game()
    print(new_game)

    while new_game.game_level < 5:
        display_option()
        verify_response()
        handle_response(new_game)
        print(f"Game level is currently{new_game.game_level}")
    print("End of game flow logic")


def display_option():
    """
    Displays the current options from the Pathway object
    """
    print("Displaying current 4 options")


def verify_response():
    """
    Verify user response is a b c or d
    """
    print("Checking user response is a b c or d")


def handle_response(current_game):
    """
    Handles the logic of game advancement
    Call verification
    If response is advance display next set of options
    If response is hold display remaining options
    """
    verify_response()
    print("Handling gameflow")
    print("Advancing level")
    current_game.game_level += 1


def main():
    """
    Initiates main gameflow
    """
    display_title_screen()
    input("What is your name?\n ")
    verify_username()
    verify_first_choice()


class Game:
    """
    Builds a new Game
    """
    def __init__(self):
        self.username = "Username"
        self.game_level = 0
        self.gamepath = Pathway()

    def __repr__(self):
        return "Print the class string here"


class Pathway:
    """
    Builds a new path through the game
    Contains a dict of 5 sets of 4 pairs
    Pulls options from pathway file to build pairs at random
    """
    def __init__(self):
        self.options = {}
    # Method here to build the options dict from a file


main()
