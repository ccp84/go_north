# Go North - A Text Based Adventure Game

## Concept
Users will follow onscreen prompts to select an option to progress to the next stage of their adventure. The correct option will promote them along through the game, the wrong choice could lead them backwards, or worse. 

Overview of gameplay
![Gameplay Flowchart](documentation/gameplay.png)

## User Stories

* 

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
        User input response - verify response ( check for a, b, c, d then run Handle response() )
        Handle response ( Check response type advance - display next set of options and increment game level counter / hold - re display same set of responses calls display opt())
        While game level counter < 5
            User input response - verify response()
            Handle response()
    End game( Display end of game message and option to re start or quit )
```
## Project Development

### 


















![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome ccp84,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!