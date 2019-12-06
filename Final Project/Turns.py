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
    Displays current player name and icon (color) to window.
        No inputs. No outputs
    '''


    global turn
    global color_icon
    global text_name
 
    profiles = loginFP.get_characters()

    if turn == 2:
        name = profiles[turn][0]
        color = profiles[turn][1]
        turn = 0
        
    else:
        name = profiles[turn][0]
        color = profiles[turn][1]
        turn += 1
        
    

    text_name = Text(Point(240, 600), "It's " + name + "'s turn!  Click on the object you want to check for clues" )
    #text_name = text_name.setSize(10)
    text_name.draw(window)
    
    
    icon_color.setFill(color)
    icon_color.draw(window)

    
def delete_profile():
    '''
    Undraws profile (name and icon) from window
        No input. No output
    '''
    global icon_color
    global text_name
    
    icon_color.undraw()
    text_name.undraw()
    