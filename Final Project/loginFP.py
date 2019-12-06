#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:21:21 2019

@author: danielacamacho
"""

characters = [] #will eventually be a list of tuples with the profiles

def get_profiles():
    '''
    loginPF
    
    This is the login part of the program. Asks for names and color to 
    identify who is playing. Gives option of red, blue and green 
        Input: no input
        Output: no output, but it creates a list of tuples with the names and colors chosen
    
    '''
    
    color_options = ['green', 'blue', 'red']
    
    print("Welcome to Intro to Python. This is a 3 player game, where y'all have to find clues to be allowed to leave class")
    
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
    '''
    Function that returns the info entered in for the characters' profiles.
        Input: There are no inputs
        Outputs: characters (list of tuples). Each element is a profile. 
            The first item in the tuple is the name, and the second the color
    '''
    global characters
    return characters