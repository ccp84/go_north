# Testing

## User Stories

| Test  | Outcome | Proof |
|----|--------|--------|
|Understand what to enter at each prompt.| Every time the user is asked to enter text, the acceptable enteries are explained to them. | ![User input example](documentation/user_choice.png)|
|Recieve clear feedback for incorrect text entries.|Invalid entries are highlighted as incorrect with the correct choices repeated and the user prompted to select again.|![Invalid entry example](documentation/invalid_choice.png)|
|Find out how to play the game.| The user can select to display the rules at the start of each game.|![Rules](documentation/rules.png)|
Exit back to the start point at any time. | The user is given the option to quit the game during each selection point of the game. | ![Exit screenshot](documentation/exit.png)

## Bugs encountered and fixed during production

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

* Tests carried out revealed no remaining bugs to the best of my knowledge.

## Manual Testing

| Test | Expected Outcome | Outcome | Proof |
| ---  | -----------------| ------- | ----- |
|Username input| Only alpha characters accepted. | Tried entering : A number, a character, a space, just hitting enter - all returned an error message informing me this was an invalid entry and that the username must contain letters only. | ![Username verification testing](documentation/player_name_testing.png) |
| Choosing between 'Start Game', 'How to Play' and 'Exit' | Only '1', '2' or '3' is accepted | Tried entering : 5, a letter, a space, a character, and a blank entry. These all returned an error message stating to enter 1 or 2. Entering 2 displayed a test string in place of the full game rules, entering 1 started the game flow. Confirmed that 3 returns the user to the title screen. | ![Initial choice testing](documentation/initial_choice_testing.png) |
| Choosing a b c or d as the game path option | Only A, a, B, b, C, c, D, d, X, or x should be accepted. | Tests showed that entering e, /, space, blank, or 5 returned an error message that this was an invalid entry and to select from the given options. | ![User path testing](documentation/game_path_choice_test.png) |


## Code validation with CI validation app

Both python files pass through the Code Institute PEP8 validator with no errors:
![run.py screenshot](documentation/runpy_verify.png)
![story.py screenshot](documentation/storypy_verify.png)


* [Back to README](README.md)