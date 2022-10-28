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
    if choice == 1:
        start_game()
    elif choice == 2:
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
