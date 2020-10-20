#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:33:43 2019

@author: mintmsh
"""
#import numpy as np

def solve(f, x_init, err):
    x = x_init
    #iteration = 0
    while (True):
        [fx, drv] = f(x)
        if (abs(fx) <= err):
            break
        x = x - fx/drv
        #iteration = iteration + 1
    
    #print(iteration)    
    return x
    
'''
if __name__ == '__main__':
    
    ans = solve(lambda x: [x**2-1, 2*x], 3, 0.0001)
    print(ans)
 '''
  
'''
    For:
        solve(lambda x: [x**2-1, 2*x], 3, 0.0001)
    My result is:
        1.0000305180437934
        
    For:
        solve(lambda x: [x**2-1, 2*x], -1, 0.0001)
    My result is:
        -1
        
    For:
        solve(lambda x: [np.exp(x)-1, np.exp(x)], 1, 0.0001)
    My result is:
        1.5641107898984284e-06
        
    For:
        solve(lambda x: [np.sin(x), np.cos(x)], 0.5, 0.0001)
    My result is:
        3.311802132639069e-05
        
'''

'''
    Bonus:
        for tolerance = 10^-3, iteration = 4, ans = 1.0000305180437934
        for tolerance = 10^-4, iteration = 4, ans = 1.0000305180437934
        for tolerance = 10^-5, iteration = 5, ans = 1.0000000004656613
        for tolerance = 10^-6, iteration = 5, ans = 1.0000000004656613
        for tolerance = 10^-7, iteration = 5, ans = 1.0000000004656613
        for tolerance = 10^-8, iteration = 5, ans = 1.0000000004656613
        for tolerance = 10^-9, iteration = 5, ans = 1.0000000004656613
        for tolerance = 10^-10, iteration = 6, ans = 1.0
        for any smaller tolerence, iteration = 6, ans = 1.0
        
        Summary:
            Generally, with larger tolerence, it takes less iteration to find
        the approximate solution. No obvious linear relation is between the
        power of the tolerence and the iteration needed.
'''