def display_title_screen():
    """
    Prints out the title screen of the game
    """
    print("\n Title screen function running \n ")


def verify_username():
    """
    Take in username and check contents
    """
    username = input(" \nWhat is your name? \n ")
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
    choice = input("\n Start Game - 1   How to play - 2 \n:")
    if choice == '1':
        start_game(username)
    elif choice == '2':
        display_instructions(username)
    else:
        print("\n ERROR please enter 1 or 2 \n")
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
    print("\n New game building... \n")
    new_game = Game(username)
    print(new_game)

    while new_game.game_level < 5:
        display_option(new_game)
        handle_response(new_game)
    print("\n Glory and admiration \n")
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
        option = input("\n a, b, c, d \n")
        if option == "a" or option == "b" or option == "c" or option == "d":
            verified_option = True
        else:
            print("\n Error please enter a b c or d \n")
    return option


def handle_response(current_game):
    """
    Handles the logic of game advancement
    Call verification
    If response True is advance display next set of options
    If response is False. Game over. Take user back to start game screen.
    """
    choice = verify_response()
    current_path = current_game.gamepath.options[current_game.game_level+1]
    outcome = current_path[choice]
    print(f"This is the storyline response to your choice {outcome[1]}")
    if outcome[2]:
        current_game.game_level += 1
    else:
        print("\n You died. Game over. Better luck next time \n")
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
        return f"Welcome to the game {self.name}"


class Pathway:
    """
    Builds a new path through the game
    Contains a list of 5 lists with 4 sets of options in each
    Pulls options from pathway file to build option sets at random
    """
    def __init__(self):
        self.options = {
            1: {"a": ["Story a", "Response a", True], "b": ["Story b", "Response b", False], "c": ["Story c", "Response c", True], "d": ["Story d", "Response d ", True]},
            2: {"a": ["Story a", "Response a", True], "b": ["Story b", "Response b", False], "c": ["Story c", "Response c", True], "d": ["Story d", "Response d ", True]},
            3: {"a": ["Story a", "Response a", True], "b": ["Story b", "Response b", False], "c": ["Story c", "Response c", True], "d": ["Story d", "Response d ", True]},
            4: {"a": ["Story a", "Response a", True], "b": ["Story b", "Response b", False], "c": ["Story c", "Response c", True], "d": ["Story d", "Response d ", True]},
            5: {"a": ["Story a", "Response a", True], "b": ["Story b", "Response b", False], "c": ["Story c", "Response c", True], "d": ["Story d", "Response d ", True]}
        }
    # Method here to build the options dict from a file


main()
