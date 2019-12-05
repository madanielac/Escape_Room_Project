#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:46:06 2019

@author: danielacamacho
"""


#import loginFP
from graphics import *
from Key import *
from Click import *

import threading 


from Clues import get_clue


class Classroom:
    
    def __init__(self, window):
        self.window = window

    
    def create_elements(self):
        
        #draw background
        background_color = Rectangle(Point(0, 0), Point(1000, 500))
        background_color.setFill('#B8DFE9')
        background_color.draw(self.window)
        
        #draw JED!
            #face. dimensions: x= 470, y = 45. radius = 25
        self.face = Circle(Point(470, 45), 25)
        self.face.setFill('#FBFBF0')
            #glasses
        glasses_l = Rectangle(Point(453, 37), Point(467, 49))
        glasses_l.setFill('#FAFCFC')
        glasses_r = Rectangle(Point(472, 37), Point(486, 49))
        glasses_r.setFill('#FAFCFC')
                          
        self.face.draw(self.window)
        glasses_l.draw(self.window)
        glasses_r.draw(self.window)
        
        # drawing tables
        # table 1 @ (200,150) and (800, 220), so 200 to 800 on x and 150 to 220 on y
        # table 2 @ (200,270) and (800, 340), so 200 to 800 on x and 270 to 430 on y
        self.table_1 = Rectangle(Point(200, 150), Point(800, 220))
        self.table_1.setFill('#f5f5f5')
        self.table_2 = Rectangle(Point(200, 270), Point(800, 340))
        self.table_2.setFill('#f5f5f5')
        
        self.table_1.draw(self.window)
        self.table_2.draw(self.window)
        
        #drawing whiteboards. On in the front. One in back on in front 
        # front one @ (600,0) and (970, 20), so 600 to 970 on x and 0 to 20 on y
        # back one @ (600,480) and (970, 500), so 600 to 970 on x and 480 to 500 on y
        self.board_front = Rectangle(Point(600, 0), Point(970, 20))
        self.board_front.setFill('white')
        self.board_back = Rectangle(Point(600, 480), Point(970, 500))
        self.board_back.setFill('white')
        
        self.board_front.draw(self.window)
        self.board_back.draw(self.window)
        
        #drawing projector
        # projector @ (20,0) and (400, 20), so 20 to 400 on x and 0 to 20 on y
        self.projector = Rectangle(Point(20, 0), Point(400, 20))
        self.projector.setFill('#DFF3F8')
        
        self.projector.draw(self.window)
        
        #drawing window
        # drawinf of window @ (990,30) and (1000, 330), so 990 to 1000 on x and 30 to 330 on y
        self.win_draw = Rectangle(Point(990, 30), Point(1000, 330))
        self.win_draw.setFill('#F1F9FB')
        
        self.win_draw.draw(self.window)
        
        #drawing door
        self.door = Rectangle(Point(25, 490), Point(170, 500))
        self.door.setFill('#BB981E')
        
        self.door.draw(self.window)
        
        '''
        def draw_player_1(self):
            player_1_name = loginFP.get_characters()[0][0]
            plater_1_color = loginFP.get_characters()[0][1]
            player_1 = 
        '''


        
w = GraphWin("Intro to Python", 1000, 650)
    
C = Classroom(w)
C.create_elements()
get_clue('door').draw(w)



#def gfg():
    #global C
    
    #C.window.close()
    
#timer = threading.Timer(5.0, gfg) 
#timer.start() 




