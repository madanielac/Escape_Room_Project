#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:42:57 2019

@author: danielacamacho
"""
import loginFP
from graphics import *

turn = 0
text_name = ''
icon_color = Circle(Point(60, 600), 10)

def player_turn(window):
    
    '''
    Function that makes sure turns rotate between players. There are 7 objects to 
    interact with in the game and seven correponding rounds. This function assigns each of
    the three players a round, in order.
    
    For Example:
    round = 1,2,3,4,5,6,7 players = 1,2,3
    turns = 1,2,3,1,2,3,1
    So because of the inherent structure of the game player one plays on rounds 1, 4, and 7, player two on rounds 2 and 5,
    player three on rounds 3 and 6.
    
    returns an ordered list called character_order with the assignment of each of the three players for seven total rounds
    '''
    
    '''
    get_characters()
    character_order = []
    roundcount = 0
    while roundcount < 7:
        if roundcount == (1 or 4 or 7):
            student == characters[0]
            character_order.append(student)
        if roundcount == (2 or 5):
            student == characters[1]
            character_order.append(student)
        else:
            student == characters[2]
            character_order.append(student)
        
        roundcount += 1
    return character_order

    '''


    global turn
    global color_icon
    global text_name
 
    profiles = loginFP.get_characters()

    if turn == 2:
        turn = 0
        name = profiles[turn][0]
        color = profiles[turn][1]
    else:
        name = profiles[turn][0]
        color = profiles[turn][1]
        turn += 1
        
    

    text_name = Text(Point(120, 600), "It's " + name + "'s turn!" )
    #text_name = text_name.setSize(10)
    text_name.draw(window)
    
    
    icon_color.setFill(color)
    icon_color.draw(window)

    
def delete_profile():
    global icon_color
    global text_name
    
    icon_color.undraw()
    text_name.undraw()
    