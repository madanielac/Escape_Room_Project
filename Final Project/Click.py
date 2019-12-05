# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:21:51 2019

@author: kmlee22
"""


def click_object(self):
    win = self.window
    coordinate = win.checkMouse()
    if coordinate in self.face:
        choose_element = jed
    if coordinate in self.projector:
        choose_element = screen
    if coordinate in self.board_front:
        choose_element = front_board
    if coordinate in self.win_draw:
        choose_element = win_drawing
    if coordinate in self.board_back:
        choose_element = back_board
    if coordinate in self.table:
        choose_element = table
    if coordinate in self.door:
        choose_element = door