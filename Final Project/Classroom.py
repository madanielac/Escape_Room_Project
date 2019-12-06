#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:46:06 2019

@author: danielacamacho
"""


import loginFP
from graphics import *
import Turns

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
        # door @ (25,490) and (170, 500), so 25 to 170 on x and 490 to 500 on y
        self.door = Rectangle(Point(25, 490), Point(170, 500))
        self.door.setFill('#BB981E')
        
        self.door.draw(self.window)
        
        
    def click_object(self, location_clicked):
        '''
        Function to see what object is selected by the player.
            Input: self
            Output: choose_element (str) - element that is selected. 
                                            Will later be used as input for Clues function.
                    or (str) if an object without a clue was selected indicating that they didn't find a clue 
        '''
        
        
        coordinate = location_clicked
        print(type(coordinate))
        
        x_position = 20
        y_position = 0
        
        found = False
        choose_element = ''
        
        
        trial_list = []
        
        
        #to check for whole projector
        while x_position <= 400:
            y_position = 0
            
            while y_position <=20:
            
                trial_list.append((Point(float(x_position), float(y_position))))
                
                if coordinate in trial_list:
                    print('GOT HERE')
                    choose_element = 'screen'
                    found = True
                
                
                if coordinate == Point(float(x_position), float(y_position)):
                    print('GOT HERE')
                    choose_element = 'screen'
                    found = True
                
                
                y_position += 1
            x_position += 1
                
        if found == False:
            #to check for whole front whiteboard
            x_position = 600
            y_position = 0
            
            while x_position <= 970:
                while y_position <=20:
                    
                    if coordinate == Point(x_position, y_position):
                        choose_element = 'front_board'
                        found = True
                    
                    y_position += 1
                x_position += 1
                
        if found == False:
            #to check for whole window
            
            x_position = 990
            y_position = 30
            
            while x_position <= 1000:
                while y_position <=330:
                    
                    if coordinate == Point(x_position, y_position):
                        choose_element = 'win_drawing'
                        found = True
                    
                    y_position += 1
                x_position += 1
        
        if found == False:
            #to check for whole back whiteboard

            x_position = 600
            y_position = 480
            
            while x_position <= 970:
                while y_position <=500:
                    
                    if coordinate == Point(x_position, y_position):
                        choose_element = 'back_board'
                        found = True
                    
                    y_position += 1
                x_position += 1
                
        if found == False:
            #to check for table

            x_position = 200
            y_position = 150
            
            while x_position <= 800:
                while y_position <=220:
                    
                    if coordinate == Point(x_position, y_position):
                        choose_element = 'table'
                        found = True
                    
                    y_position += 1
                x_position += 1
                
        if found == False:
            #to check for door

            x_position = 25
            y_position = 490
            
            while x_position <= 170:
                while y_position <=500:
                    
                    if coordinate == Point(x_position, y_position):
                        choose_element = 'door'
                        found = True
                    
                    y_position += 1
                x_position += 1
        
        if found == False:
            choose_element = 'Object selected is not a clue'
        
        #if coordinate in self.face:
         #   choose_element = 'jed'
            

        
        print(choose_element)
        print('DANCING QUEEN')
        return choose_element
   
    
    
'''
#loginFP.get_profiles()     
w = GraphWin("Intro to Python", 1000, 650)
    
C = Classroom(w)
C.create_elements()
r = w.getMouse()

#print(type(r))
print(r)
C.click_object(r)
w.close()
'''


'''
loginFP.get_profiles()     
w = GraphWin("Intro to Python", 1000, 650)
    
C = Classroom(w)
C.create_elements()
get_clue('front_board').draw(w)
Turns.player_turn(w)

#w.getMouse()
#w.close()



#def gfg():
    #global C
    
    #C.window.close()
    
#timer = threading.Timer(5.0, gfg) 
#timer.start() 

'''


