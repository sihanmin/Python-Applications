#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 03:32:49 2018

"""

import Tkinter as Tk
#import tkinter as Tk
import random

WIDTH = 600
HEIGHT = 600
SIZE = 60
#canvas.pack()
#color = "black"

class Knights_Tour_Game(object):
    def __init__(self, master, n):
        self.dim = n
        self.master = master
        self.canvas = Tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="grey")
        self.canvas.pack()
        self.size = SIZE
        if self.dim * SIZE > WIDTH:
            self.size = WIDTH / self.dim
        self.x = 0
        self.y = 0
        self.start = (WIDTH - self.dim * self.size) / 2
        self.draw_board()
        self.canvas.bind("<Button-1>", self.make_move)
        
    # this function draws the board
    def draw_board(self):
        for i in range(self.dim):
            for j in range(self.dim):
                self.canvas.create_rectangle(self.compute(i,j),fill="white")
    
        self.canvas.create_rectangle(self.compute(0,0), fill="orange")
    
    # this function is called at each click on the canvas
    # it makes the conditional move
    def make_move(self, event):
        size = self.size
        x = int((event.x - self.start) / size)
        y = int((event.y - self.start) / size)
        
        if (self.valid(x,y)):
            self.canvas.create_rectangle(self.compute(self.x, self.y), fill="blue")
            self.canvas.create_rectangle(self.compute(x, y), fill="orange")
            self.x = x
            self.y = y
    
    # this function checks if the coordinate passed in is a valid move
    def valid(self, x, y):
        if x < 0 or y < 0 or x >= self.dim or y >= self.dim:
            return False 
        if abs(x - self.x) == 2 and abs(y - self.y) == 1:
            return True
        if abs(x - self.x) == 1 and abs(y - self.y) == 2:
            return True
        return False
    
    # this function takes in a coordinate of x, y between 0 to (n-1)
    # it returns the starting and ending coordininates on the canvas
    def compute(self, x, y):
        x_cor = self.start + x * self.size
        y_cor = self.start + y * self.size
        return x_cor, y_cor, x_cor+self.size, y_cor+self.size
        
   
def knights_tour(n):
    root = Tk.Tk()
    game = Knights_Tour_Game(root, n)
    root.mainloop()

'''
if __name__ == '__main__':
    #root = Tk.Tk()
    #canvas = Tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="grey")
    #canvas.pack()
    #root.mainloop()
    knights_tour(5)

'''
    
    
