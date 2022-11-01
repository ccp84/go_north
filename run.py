"""
Go North
A text based adventure game for Code Institute PP3
"""


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
    Follow the story.
    Select a, b, c or d at each turn.
    Find the lightswitch.
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
        new_game.game_level += 1
    print("\n Glory and admiration is yours \n")
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
        option = input("\n Which path will you take? \n")
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
    print(outcome[1])
    if outcome[2]:
        return
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
        return "You awake to find yourself in a dark room..."


class Pathway:
    """
    Builds a new path through the game
    Contains a list of 5 lists with 4 sets of options in each
    Pulls options from pathway file to build option sets at random
    """
    def __init__(self):
        self.options = {
            1: {"a": ["Why?", "Because it's dark, and it's a room, and you're in it.", True], "b": ["Check Pockets", "You stand in the room with your hands in your pockets.", True], "c": ["Go North", "You proceed in a direction you assume to be North, how can you tell, you're in a dark room.", True], "d": ["Sleep", "You awake to find yourself in a dark room", True]},
            2: {"a": ["This is an option", "You continue your search", True], "b": ["This one will kill you", "I have no choice but to inform you...", False], "c": ["This is also an option", "You continue your search", True], "d": ["This is an option too", "You continue your search", True]},
            3: {"a": ["Touch the wall", "You cant find the wall, you're in a dark room", True], "b": ["Czech pockets", "Your pockets were made in the Czech republic, but that won't help you now.", False], "c": ["Turn on the light", "How can you find the lightswitch, you're in a dark room?", True], "d": ["Weep", "You stand in the dark and weep", True]},
            4: {"a": ["Go south", "In the darkness, you walk headfirst into the southern wall", False], "b": ["Enter cheat code", "Level Skip", True], "c": ["Talk to NPC", "Side Quest Activated", True], "d": ["Save Game", "The game is beyond saving really", True]},
            5: {"a": ["Kick Wall", "You broke the 4th wall", False], "b": ["Inventory", "Lightswitch", True], "c": ["Abandon Hope", "You lean on the wall and weep, knocking the lightswitch on as you do", True], "d": ["Lean on wall and weep", "You lean on the wall and weep, knocking the lightswitch on as you do", True]}
        }
    # Method here to build the options dict from a file


main()
