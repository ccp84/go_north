# Go North - A Text-Based Adventure Game

* [Play deployed game here](https://go-north.herokuapp.com/)

## Concept
Go North is aimed at Munckin and D&D players who are fans of the [John Robertsons live action text based adventure The Dark Room](https://www.thejohnrobertson.com/thedarkroom/).
Users begin as a level 0 adventurer. By selecting from on screen options as they go through the game, they can gain or loose levels on their quest to become a level 5 adventurer! 
'Loot' and 'Cheat Codes will gain levels. 'Monsters' or 'Curses' will loose levels.
Loose too many levels and it's game over.

Overview of gameplay
![Gameplay Flowchart](documentation/gameplay.png)

## User Stories

Users should be able to
* Understand what to enter at each prompt.
* Recieve clear feedback for incorrect text entries.
* Find out how to play the game.
* Exit back to the start point at any time. 


## Gameplay Logic
```
Call main()
    Display title screen( print to screen )
    Input username - verifyname( check input contains alpha chars only )
    Print Options 1 - Start 2 - How to play
                        Display instructions( print to screen then display input options again )
    start game()
        Build new Game object
        Display Game string representation
        Print initial game option
        User input response - verify response ( check for a, b, c, d, x then run Handle response() )
        Handle response: 
            (Check response type:
            x = exit back to game menu
            a,b,c,d = enter while loop
            other = display error and ask for re entry of response
        While game level counter < 5
            User input response - verify response()
            Handle response()
        If game level counter < 0
            Game over
            Return to start of game
        If game level counter > 5
            Display winning message
            Return to start of game
    End game
```
## Project Development

### verify_username() function:

This function gives the user a keyboard input and saves to the username variable. This is checked for alphabetic only characters using `isalpha()`. If this returns true, the user is welcomed to the game and the function returns the username to the main function to contiue running. If this returns false, an error message is displayed to prompt the user to enter only alpha characters and to try again. 

### verify_first_choice() function:

This function gives the user the first options within the game, to start the game or display the gameplay instructions. Logic is included to check which option is returned from the user, and an else catches "other" responses to display an error and prompt the user to enter a valid response either 1 or 2 in this case.

### display_current_option() function:

This function takes in the Game object from where it is called and uses the Pathway object, and the game level of the current game to determine which set of options to display to the user. 
The game path is a set of lists within the Pathway object, by using the current game level as an index for the list of lists, this function then gives the user the correct set of on screen options.

### verify_response() function:

This function asks for a choice from the available game path choices displayed by the `display_current_option()` function and then checks that the user response is valid. If the response is invalid, an error message is displayed on screen with a prompt of the 4 correct options to choose from and cycles back to the start of the input and checking sequence again. Once a valid option has been verified, this is returned back to the main game flow and stored to be used by other functions to continue game play.

### handle_response() function:

This function calls on the `verify_response()` function to gain the users next validated pathway choice. It then extracts the game's storyline response from the Pathway object's options dictionary and displays the next part of the story to the user. Using an if statement, the function then gets the `True` or `False` indicator attached to the choice made by the user to decide if `True` the game levels up and continues along the game path or if `False` .....
![Death](documentation/death.png)

### build_story() function

This function is called when building the Pathway object and contains a randomly generated storyline each game. It uses 3 text files to combine positive, negative and winning scenarios to make a replayable story. For each level, the positives are shuffled and 2 options are added to the level container followed by 2 options from a shuffled negatives list. This level list is shuffled, and then appended to the overall story dictionary. The final level is constructed from 2 choices from a shuffled winning choices list and 2 choices from the remaining negatives list before being shuffled and appended to the storyline dictionary. The full story dictionary is returned by the function as the options attribute of the Pathway object.

## Testing

[Link to testing carried out](TESTING.md)


## Future Features

Given more time and scope to develop this project, I would have liked to allow users to select the difficuly of the game allowing for shorter / longer game lengths. I would have also liked to work on developing the storyline to give better flow of responses and options, and build in a choice of pathways to take for further replayability. 

## Deployment
​
Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser. This is to improve the accessibility of the project to others.
​
The live deployed application can be found at [Go North](https://go-north.herokuapp.com/).
​
### Local Deployment
​
*Gitpod* IDE was used to write the code for this project.
​
To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/ccp84/go_north.git`
​
Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.
​
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ccp84/go_north)
​
### Heroku Deployment
​
This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
​
Deployment steps are as follows, after account setup:
​
- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select *Add Buildpack*.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)
​
Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile
​
You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`
​
The Procfile can be created with the following command: `echo web: node index.js > Procfile`
​
For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:
​
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`
​
The frontend terminal should now be connected and deployed to Heroku.

## Technologies Used
* Git - Version control and project flow management
* [GitHub Issues - For tracking and resolving bug fixes](https://github.com/ccp84/go_north/issues)
![GitHub Issues](documentation/issue_1.png)
* Code Institute Python Terminal Template
* [Heroku - Deployment of Python project](https://id.heroku.com/login)
* Python Class and Object Oriented Code

## Credits

* [Flowchart from Lucidchart](https://lucid.app/)
* [Isalpha for checking username from w3schools](https://www.w3schools.com/python/ref_string_isalpha.asp#:~:text=The%20isalpha()%20method%20returns,alphabet%20letters%3A%20(space)!)
* [Storyline and creative ideas based on John Robertsons live interactive show](https://www.thejohnrobertson.com/thedarkroom/)
* [Further storyline ideas from Steve Jackson's Munchkin](http://www.sjgames.com/)
* [Block letters formation from Codecademy](https://www.codecademy.com/courses/learn-python-3/projects/python-block-letters)
* [File handling method from Codecademy tutorial](https://www.codecademy.com/courses/learn-python-3/lessons/learn-python-files/)
* [How to shuffle from w3schools documentation](https://www.w3schools.com/python/ref_random_shuffle.asp)
* [String replace method learned in Codecademy tutorial](https://www.codecademy.com/courses/learn-python-3/lessons/string-methods/)
* [Fix for using ast / json to remove added aspostrophes when appending to a dictionary from StackOverflow](https://stackoverflow.com/questions/53052277/add-string-to-dictionary-without-quotes-in-python)
* [Clear terminal function from stack overflow](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
* Mentor, Tim Nelson, for assistance with Heroku deployment instructions.