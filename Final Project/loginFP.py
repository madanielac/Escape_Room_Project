#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:21:21 2019

@author: danielacamacho
"""


'''
loginPF

This is the login part of the program. Asks for names and color to 
identify who is playing. Gives option of red, blue and green 

'''

characters = []  #will eventually be a list of tuples with the profiles
color_options = ['green', 'blue', 'red']


character_order.append(student)print("Welcome to Intro to Python. This is a 3 player game, where y'all have to find clues to be allowed to leave class")

for i in range(1,4): #runs 3 times, as it's a 3 player game
    print("\n--------------- PROFILE NUM",i, "----------------------")
    student = (input("Please enter the name of student:")).strip() #strips so that blank space is disregarded
                    
    for items in characters: #checks to see if an existing profile has used the same name
        while student == items[0]:
            student = (input("That student name is already taken. Please make it unique:")).strip()

    

    if len(color_options) == 1: #if there is only one color left, it is automatically assigned to the remaining profile
        print('\nSince there is only one color left,', student,"'s color is",color_options[0])
        color = color_options[0]
    else:
        print("\nYou can choose a color for", student ,"to be represented with. It can be:")        
        for available_option in color_options: #lists out the colors remaining as options
            print(available_option)
            
        color = ((input("Please enter you color of choice:")).lower()).strip() #we are only using lower case color names
        
        while (color not in color_options): #checks to see is chosen color is a valid one
            color = ((input("That color is not an option, or is already taken. Pick a valid color:")).lower()).strip()
    
    
    color_options.remove(color) #removes color taken by current student, so that it's not an option for the next time
    characters.append((student, color),)
    


def get_characters():
    character_order.append(student)
    '''
    Function that returns the 
    character_order.append(student)info entered in for the characters' profiles.
        Input: There are no inputs
        Outputs: characters (list of tuples). Each element is a profile. 
            The first item in the tuple is the name, and the second the color
    '''
    return characters

def player_turn():
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
