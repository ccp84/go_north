# Testing

## Bug Fixes

* [verify_first_choice() if statement](https://github.com/ccp84/go_north/issues/1)
![Issue 1 screenshot](documentation/issue_1.png)

* [handle_response() game_level variable](https://github.com/ccp84/go_north/issues/2)
![Issue 2 screenshot](documentation/issue_2.png)

* [verify_first_choice() enter a letter](https://github.com/ccp84/go_north/issues/3)
![Issue 3 screenshot](documentation/issue_3.png)

## Manual Testing

* Username input - an if statement checks that only alpha characters are entered and displays an error message if this check returns false. Tests proved to only accept alpha characters as below.
![Username verification testing](documentation/player_name_testing.png)

* Choosing between 'Start Game' and 'How to Play' - an input box takes the users choice for which action to perform and then checks the response. An if/elif/else statement handles the response. If an invalid option is entered, an error message is displayed and the user is prompted to try again. 
![Initial choice testing](documentation/initial_choice_testing.png)