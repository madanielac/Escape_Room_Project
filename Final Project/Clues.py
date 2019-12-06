#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:43:39 2019

@author: danielacamacho
"""

from graphics import *

initial_instructions= 'Click on the item where you would like to begin! Here’s a hint: Jed would probably be the best place to start because Jed knows all. \nBe sure to keep track of the letters you are asked to remember at each object, as you will need to scramble these letters at the end when you reach the door in order to leave the classroom!'
jed = 'This type of scalar object represents real numbers (ex. 3.14, 7.29, etc.). You will want to keep the third letter from this term. Need more information? Go to the screen next!'
screen = 'This type of loop is used to work through a set of code repeatedly for an unknown number of times, given specified conditions are met. \nIt can also be thought of as repeating “if" statements. You will want to keep the fourth letter of this term. Take a look at the front whiteboard for more information!'
front_board = 'This type of method takes advantage of the fact that numbers are ordered. These types of searches require an initial low and high end, which gets updated with each guess. \nFor example, if the guess is too low, then that guess becomes the new low end. Same concept goes for the high end. \nTake the new guess to be the average of the low and the high points to get you a point exactly in the middle. Take the 2nd to last letter of this term, then move on to the window to find your next clue!'
win_drawing = 'This term is used to describe an unordered set of objects, that can not be indexed with a number, but can be indexed with keys. \nYou will want to keep the 7th letter of this term. Head over to the back whiteboard to find your next clue!'
back_board = 'This type of variable is defined at the outermost scope of the program, making it accessible to all functions in the program. You will want to take the 4th letter from this term. \nGo take a look at the table for your next set of hints!'
table = 'Anonymous functions can be written using ______ expressions. You will want to keep the 2nd letter of this term. Go to the door to get your final hint to leave the classroom!'
door = 'This non-scalar object holds the following properties: comprised of ordered smaller elements, immutable, delimited by parentheses. You will want to keep the last letter of this term.'



def get_clue(chosen_element):
    global initial_instructions
    global jed
    global screen
    global front_board
    global win_drawing
    global back_board
    global table
    global door
    
    if chosen_element == 'initial':
        text = Text(Point(500, 540), initial_instructions)
    elif chosen_element == 'jed':
        text = Text(Point(500, 540), jed)
    elif chosen_element == 'screen':
        text = Text(Point(500, 540), screen)
    elif chosen_element == 'front_board':
        text = Text(Point(500, 540), front_board)
    elif chosen_element == 'win_drawing':
        text = Text(Point(500, 540), win_drawing)
    elif chosen_element == 'back_board':
        text = Text(Point(500, 540), back_board)
    elif chosen_element == 'table':
        text = Text(Point(500, 540), table)
    elif chosen_element == 'door':
        Key()
        text = Text(Point(500, 540), door)
        
    return text
