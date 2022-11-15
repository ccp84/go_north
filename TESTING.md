# Testing

## User Stories

| Test  | Outcome | Proof |
|----|--------|--------|
|Understand what to enter at each prompt.| Every time the user is asked to enter text, the acceptable enteries are explained to them. | ![User input example](documentation/user_choice.png)|
|Recieve clear feedback for incorrect text entries.|Invalid entries are highlighted as incorrect with the correct choices repeated and the user prompted to select again.|![Invalid entry example](documentation/invalid_choice.png)|
|Find out how to play the game.| The user can select to display the rules at the start of each game.|![Rules](documentation/rules.png)|
Exit back to the start point at any time. | The user is given the option to quit the game during each selection point of the game. | ![Exit screenshot](documentation/exit.png)

## Bug Fixes

* [verify_first_choice() if statement](https://github.com/ccp84/go_north/issues/1)
![Issue 1 screenshot](documentation/issue_1.png)

* [handle_response() game_level variable](https://github.com/ccp84/go_north/issues/2)
![Issue 2 screenshot](documentation/issue_2.png)

* [verify_first_choice() enter a letter](https://github.com/ccp84/go_north/issues/3)
![Issue 3 screenshot](documentation/issue_3.png)

* [display_option() runs twice in game play flow](https://github.com/ccp84/go_north/issues/4)
![Issue 4 screenshot](documentation/issue_4.png)

* [Issue appending to dictionary adding apostrophes](https://github.com/ccp84/go_north/issues/5)
![Issue 5 screenshot](documentation/issue_5.png)

## Bugs Remaining

* Tests carried out revealed no remaining bugs.

## Manual Testing

* Username input - an if statement checks that only alpha characters are entered and displays an error message if this check returns false. Tests proved to only accept alpha characters as below.
![Username verification testing](documentation/player_name_testing.png)

* Choosing between 'Start Game' and 'How to Play' - an input box takes the users choice for which action to perform and then checks the response. An if/elif/else statement handles the response. If an invalid option is entered, an error message is displayed and the user is prompted to try again. 
![Initial choice testing](documentation/initial_choice_testing.png)

* Choosing a b c or d as the game path option - the verify choice function checks `if` input matches a, b, c or d once converted to lowercase to account for entries of A, B, C or D. Otherwise an error message is displayed on screen and a prompt to the user to enter a valid option and another chance to input their choice again. 
![User path testing](documentation/game_path_choice_test.png)

## Code validation with CI validation app

Both python files pass through the Code Institute PEP8 validator with no errors:
![run.py screenshot](documentation/runpy_verify.png)
![story.py screenshot](documentation/storypy_verify.png)


* [Back to README](README.md)