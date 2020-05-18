# Escape Room Game

## *How to play: ## 
Run Play.py. You are going to be prompted to enter player's information into the console to create their profiles. Then a graphics window is created with the scape room. Each player can click on an element to search for clues that ultimately will allow them to get the full password to be entered at the door. Once the door is selected the player can put in what they believe to be the password into the console.
Note: Letters collected from clues are not in order, so you need to collect them and then reorder them when you get to the door.*

Interactive multiplayer Escape Room game played through a graphics window.

## Files used are:##

- Clues.py Has a function that provides the text of the clue chosen and another one to delete text (clues) from screen

- Classroom.py Classroom class contains a function to draw all of the elements of the window and another one that checks what element was clicked/selected.

- Play.py operates the play of the game, starting and ending it. Incorporates classes and functions.

- Turns.py Has a function which controls the multiplayer asset of the game and makes sure that turns rotate between players (draws a profile to the screen), and another one that deletes the profile from the screen.

- loginFP.py allows different user profiles to be created. Information collected: name/username of players and their chosen color to identify themselves in the game. Has a function where profile data is collected and another one that returns a list of tuples with said info.

The user plays the game by clicking objects in the room and using the instructions given by each to proceed to the next clue and then ultimately the final clue which allows the user to escape the room. The final clue uses information from each of the other clues. 

This game was designed with the intent to incorporate basic Python knowledge into an easy and fun game that strengthens the players grasp of Python vocabulary. 
