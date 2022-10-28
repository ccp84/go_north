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
    choice = input("Start Game - 1   How to play - 2\n")
    if choice == 1:
        start_game()
    elif choice == 2:
        display_instructions()
    else:
        print("ERROR please enter 1 or 2")
        verify_first_choice()
