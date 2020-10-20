#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 19:51:13 2019

@author: mintmsh
"""

# Source: Pajek datasets
# Link: http://vlado.fmf.uni-lj.si/pub/networks/data/sport/football.htm

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import pandas as pd

def network_plot_circle(N, continent):
    n = len(N)
    x = [np.cos(2*np.pi*i/n) for i in range(n)]
    y = [np.sin(2*np.pi*i/n) for i in range(n)]
    plt.axis([-1.1, 2.05, -1.1, 1.1])
    for i in range(n):
        for j in range(i):
            if N[i][j] > 9:
                #plt.plot([x[i],x[j]],[y[i],y[j]],'b')
                plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], head_width=0.05, head_length=0.1, 
                          fc='midnightblue', ec='midnightblue',length_includes_head = True)
            elif N[i][j] > 6:
                plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], head_width=0.05, head_length=0.1, 
                          fc='blue', ec='blue',length_includes_head = True)
            elif N[i][j] > 3:
                plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], head_width=0.05, head_length=0.1, 
                          fc='dodgerblue', ec='dodgerblue',length_includes_head = True)
            elif N[i][j] > 0:
                plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], head_width=0.05, head_length=0.1, 
                          fc='lightblue', ec='lightblue',length_includes_head = True)
   
        if continent['Continent'][i] == 'S America':
            plt.plot(x[i], y[i], 'o', color = 'green')
        elif continent['Continent'][i] == 'N America':
            plt.plot(x[i], y[i], 'o', color = 'purple')
        elif continent['Continent'][i] == 'Europe':
            plt.plot(x[i], y[i], 'o', color = 'orange')
        elif continent['Continent'][i] == 'Africa':
            plt.plot(x[i], y[i], 'o', color = 'red')
        elif continent['Continent'][i] == 'Asia':
            plt.plot(x[i], y[i], 'o', color = 'brown')
    
    #plt.plot(x,y,'ro')
    lightblue_line = mlines.Line2D([], [], color='lightblue',
                          label='1-3 players')
    dodgerblue_line = mlines.Line2D([], [], color='dodgerblue',
                          label='4-6 players')
    blue_line = mlines.Line2D([], [], color='blue',
                          label='7-9 players')
    midnightblue_line = mlines.Line2D([], [], color='midnightblue',
                          label='10+ players')
    green = mlines.Line2D([], [], color='green', marker = 'o', linestyle=' ',
                           markersize=8, label='S America')
    purple = mlines.Line2D([], [], color='purple', marker = 'o', linestyle=' ',
                          markersize=8, label='N America')
    orange = mlines.Line2D([], [], color='orange', marker = 'o', linestyle=' ',
                           markersize=8, label='Europe')
    red = mlines.Line2D([], [], color='red', marker = 'o', linestyle=' ',
                           markersize=8, label='Africa')
    brown = mlines.Line2D([], [], color='brown', marker = 'o', linestyle=' ',
                           markersize=8, label='Asia')
    plt.legend(handles=[lightblue_line, dodgerblue_line, blue_line, midnightblue_line,
                        green, purple, orange, red, brown])
    
    
    plt.title('Soccor Player Exportation Network between Countries (1998)')
    plt.show()   
    
export = open("football.txt").read()
continent = pd.read_csv('continent.csv')

pairs = [s.split() for s in export.splitlines()]
pairs = [[int(i) for i in j]for j in pairs]
n = max(max(j for j in pairs))
adjMatrix = [[0]*n for _ in range(n)]
for p in pairs:
    adjMatrix[p[0]-1][p[1]-1] = p[2]

network_plot_circle(adjMatrix, continent)

