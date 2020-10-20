#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 03:32:49 2018

"""

import tkinter as Tk
import random

WIDTH = 800
HEIGHT = 500
SIZE = 50
root = Tk.Tk()
canvas = Tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="grey")
canvas.pack()
color = "black"

class Ball:
    def __init__(self, master, pos_x, pos_y):
        self.shape = canvas.create_oval(pos_x, pos_y, 
                                        pos_x+SIZE, pos_y+SIZE, fill=color)
        self.speedx = random.uniform(1, 10)
        self.speedy = random.uniform(1, 10)
        self.active = True
        self.move_active()

    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self):
        if self.active:
            self.ball_update()
            root.after(40, self.move_active) 
    

ball = Ball(root,0,0)
ball2 = Ball(root,200,200)
ball3 = Ball(root,400,400)
root.mainloop()