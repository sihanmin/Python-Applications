#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:54:22 2019

@author: mintmsh
"""

import turtle as t
import math


def ngon(n):
    f = (n - 2) * 180 / n
    # compute each interior angle of the ngon
    
    l = 150 * math.cos(math.radians(f/2)) * 2
    # compute each side length for the ngon 
    # so that it fits into a circle of r = 150
    
    # draw n sides of the shape
    for i in range(n):
        t.fd(l)
        t.right(180-f)
        
    t.done()