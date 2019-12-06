#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:52:09 2019

@author: danielacamacho
"""

import loginFP
from Classroom import *
from graphics import *
from Turns import *
import click
from Clues import *


icon_color = Circle(Point(60, 600), 10)
text_name = ''

loginFP.get_profiles()
win = GraphWin("Intro to Python", 1000, 650)
class_draw = Classroom(win)
class_draw.create_elements()


key = False
get_clue('initial').draw(win)
win.getMouse()

delete_clue()
player_turn(win)



while key == False:
    
    
    
    clicked_object = class_draw.click_object(win.getMouse())
    get_clue(clicked_object).draw(win) #prints clue for chosen object
    
    if clicked_object == 'door':
        keyphrase = input('Enter the keyphrase: _ _ _ _ _ _ _ : ')
        keyphrase = keyphrase.lower().strip()
        if keyphrase == 'boolean':
            key = True
            delete_profile()
            delete_clue()
            text = Text(Point(500, 540), 'Congrats! You found your way out. \nClick anywhere on the screen to leave the class.')
            text.draw(win)
            win.getMouse()
            win.close()
            break
        else:
            delete_clue()
            text = Text(Point(500, 540), "That ain't it chief. Double click anywhere on the screen to continue playing")
            text.draw(win)
            win.getMouse()
            text.undraw()
    
    
    win.getMouse()
    delete_profile()
    delete_clue()
    
    player_turn(win)
    
    
win.close()
    
    


#get_clue('front_board').draw(w)

#player_turn(win)
#win.getMouse()
#delete_profile()
#win.getMouse()
#win.close()