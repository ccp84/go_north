def display_title_screen():
    """
    Prints out the title screen of the game
    """
    print("Title screen function running")


def verify_username():
    """
    Take in username and check contents
    """
    username = input("What is your name?\n ")
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
    choice = input("Start Game - 1   How to play - 2\n ")
    if choice == '1':
        start_game(username)
    elif choice == '2':
        display_instructions(username)
    else:
        print("ERROR please enter 1 or 2")
        verify_first_choice(username)


def display_instructions(name):
    """
    Prints game instructions to screen
    """
    print("""
    Game instructions
    as a big long string
    go in here
    """)
    verify_first_choice(name)


def start_game(username):
    """
    Builds game object and game path
    """
    print("New game building...")
    new_game = Game(username)
    print(new_game)

    while new_game.game_level < 5:
        display_option(new_game)
        handle_response(new_game)
        print(f"Game level is currently{new_game.game_level}")
    print("End of game flow logic")


def display_option(current_game):
    """
    Displays the current options from the Pathway object
    """
    display_level = current_game.game_level
    game_path = current_game.gamepath.options
    print(game_path[display_level])


def verify_response():
    """
    Verify user response is a b c or d
    """
    option = input("a, b, c, d \n")
    if option == "a" or option == "b" or option == "c" or option == "d":
        return option
    else:
        print("Error please enter a b c or d")
        verify_response()


def handle_response(current_game):
    """
    Handles the logic of game advancement
    Call verification
    If response is advance display next set of options
    If response is hold display remaining options
    """
    choice = verify_response()
    current_path = current_game.gamepath
    current_options_set = path.option[current_game.game_level]
    selected_option = "current_options_set get the response that goes with the letter selected"
    
        
    print("Handling gameflow")
    print("Advancing level")
    current_game.game_level += 1


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
        return f"Welcome to the game {self.name}"


class Pathway:
    """
    Builds a new path through the game
    Contains a list of 5 lists with 4 sets of options in each
    Pulls options from pathway file to build option sets at random
    """
    def __init__(self):
        self.options = {
            {1 : {"a" : [1, True], "b" : [2, False], "c" : [3, True], "d" : [4, True]}}
            {2 : {"a" : [1, False], "b" : [2, True], "c" : [3, True], "d" : [4, True]}}
            {3 : {"a" : [1, False], "b" : [2, True], "c" : [3, False], "d" : [4, True]}}
            {4 : {"a" : [1, True], "b" : [2, True], "c" : [3, True], "d" : [4, False]}}
            {5 : {"a" : [1, True], "b" : [2, False], "c" : [3, True], "d" : [4, True]}}
        }
    # Method here to build the options dict from a file


main()
