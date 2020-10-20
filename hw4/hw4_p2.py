#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:30:48 2019

@author: mintmsh
"""
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import random

'''
This data is from: United Nations DESA Population Division
Link: https://population.un.org/wpp/Download/Standard/CSV/

The original downloaded file 'WPP2017_PopulationByAgeSex_Medium.csv' is too
big to upload on CCLE, so I save all the row where 'Location' is China into
a new csv file named 'China_Population.csv'.
'''

# data = pd.read_csv('WPP2017_PopulationByAgeSex_Medium.csv')
# data_china = data[data['Location'] == 'China']
# data_china.to_csv('China_Population.csv')


data_china = pd.read_csv('China_Population.csv')

data_china_1990 = data_china[data_china['Time'] == 1990]
data_china_2018 = data_china[data_china['Time'] == 2018]

n_groups = 21

tup1 = tuple(data_china_1990['PopTotal'] / 1000)
tup2 = tuple(data_china_2018['PopTotal'] / 1000)
 
# create plot

fig, ax = plt.subplots()
index = np.arange(n_groups)
age = tuple(index * 5)
bar_width = 0.5
opacity = 0.8

plt.xlabel('Age')
plt.ylabel('Population (in millions)')
plt.title('Age Distribution in China')
plt.xticks(index + bar_width, age)

rects1 = plt.bar(index + bar_width, tup1, bar_width,
alpha=opacity, align = 'edge', color= 'slateblue', label='1990')
 
rects2 = plt.bar(index + 2 * bar_width, tup2, bar_width,
alpha=opacity, align = 'edge', color= 'salmon', label='2018')
 

plt.legend()
plt.tight_layout()
plt.show()


'''
EXPLAINATION:
    The plot is about the age distribution in China in 1990 and 2018.
    The x-axis is age range start from 0-4, 5-9, ... to 95-99 and 100+.
    The y-axis is the total population in millions of people.
    
OBSERVATIONS:
    We can see that in 2018 China hass less people from 0-24. It is probably
caused by the Single Child Policy start from the 1970s.
    Also, the elder people is much less in 1990 than in 2018. It is probably
because that we have more advanced medical technology in recent years.
'''