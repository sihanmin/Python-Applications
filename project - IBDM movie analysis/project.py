#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 00:19:45 2019

@author: mintmsh
"""

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from sklearn.svm import SVR
import math

from datetime import datetime
from matplotlib.pyplot import rcParams


def filter_movie(row):
    if type(row["titleType"]) is str and row["titleType"]=="movie":
        return True
    return False

def filter_genre(row, genre):
    if type(row["genres"]) is str and genre in row["genres"].split(","):
        return True
    return False

def filter_year(row):
    if type(row["startYear"]) is str and len(row["startYear"]) is 4 \
        and int(row["startYear"]) < 2019 and int(row["startYear"]) > 1905:
        return True
    return False

def rate(row):
    if math.isnan(row['averageRating']) or math.isnan(row['numVotes']):
        return 0
    return row['averageRating'] * row['numVotes']

def counting(movies):
    count = movies.groupby('startYear').count()
    count['startYear'] = count.index
    count = count[['startYear','tconst']]
    count.columns = ['startYear','count']
    
    count['startYear'] = pd.to_datetime(count['startYear'], infer_datetime_format = True)
    count = count.set_index(['startYear'])
    
    return count

def popular(movies):
    pop = movies.groupby('startYear').sum()
    pop['startYear'] = pop.index
    pop = pop[['startYear','Popularity']]
    
    pop['startYear'] = pd.to_datetime(pop['startYear'], infer_datetime_format = True)
    pop = pop.set_index(['startYear'])
    
    return pop


def process(movies, genre):
    if genre == "Total":
        genre_movies = movies
    else:
        genre_movies = movies[movies.apply(filter_genre, axis=1, args=[genre])]
    
    c = counting(genre_movies)
    c.columns = [genre]
    pop = popular(genre_movies)
    pop.columns = [genre]
    
    return genre_movies, c, pop
    
def percentage(data):
    df = data.copy()
    total = df["Total"].copy()
    
    for index,row in df.iterrows():
        t = total.loc[index]
        for genre,item in row.iteritems():
            df.set_value(index, genre, item*100.0/t)

    return df

def average(count, pop):
    df = pop.copy()
    
    for index,row in df.iterrows():
        for genre,item in row.iteritems():
            df.set_value(index, genre, item/count.loc[index][genre])

    return df
    

if __name__ == '__main__':

    basics = pd.read_table('title.basics.tsv','\t')
    ratings = pd.read_table('title.ratings.tsv','\t')
    
############################   DATA PREPROCESSING   ################################
    movie_basics = basics[basics["titleType"] =="movie"]
    movie_basics = movie_basics[['tconst', 'startYear', 'genres']]
    
    movie_basics = movie_basics[movie_basics.apply(filter_year, axis=1)]
    movies = pd.merge(movie_basics, ratings, on=['tconst'], how='left')
    
    movies['Popularity'] = movies.apply(rate, axis=1)
    movies = movies.drop(columns=["averageRating", "numVotes"])
    #movies.to_csv('movies.csv')
    

    
#############################   DATA AGGREGATION   #################################
    movies, count, pop = process(movies, "Total")
    rom_movies, rom_count, rom_pop = process(movies, "Romance")
    act_movies, act_count, act_pop = process(movies, "Action")
    sf_movies, sf_count, sf_pop = process(movies, "Sci-Fi")
    hor_movies, hor_count, hor_pop = process(movies, "Horror")


    all_count = count.join(rom_count, how='left').join(act_count, how='left').\
                join(sf_count, how='left').join(hor_count, how='left')
    
    #all_count.to_csv('all_count.csv')
    
    all_pop = pop.join(rom_pop, how='left').join(act_pop, how='left').\
            join(sf_pop, how='left').join(hor_pop, how='left')
        
    #all_pop.to_csv('all_pop.csv')


##############################   REGULARIZATION   ##################################
    pct_count = percentage(all_count)
    pct_count = pct_count.tail(107)
    #pct_count.to_csv('pct_count.csv')

    avg_pop = average(all_count, all_pop)
    avg_pop = avg_pop.tail(107)
    

#################################   PLOTTING   #####################################
    # COUNT
    #beingsaved = plt.figure()
    
    plt.plot(all_count["Action"], label="Action")
    plt.plot(all_count["Romance"], label="Romance")
    plt.plot(all_count["Sci-Fi"], label="Sci-Fi")
    plt.plot(all_count["Horror"], label="Horror")
    
    plt.xlabel('Year')
    plt.ylabel('Number')
    
    plt.title("Number of Movies in Each Genre")
    
    plt.legend()
    
    plt.show()
    #beingsaved.savefig('TEST1.jpg', format='jpg', dpi=1000)
    
    
    # POPULARITY
    #beingsaved = plt.figure()
    
    plt.plot(all_pop["Action"], label="Action")
    plt.plot(all_pop["Romance"], label="Romance")
    plt.plot(all_pop["Sci-Fi"], label="Sci-Fi")
    plt.plot(all_pop["Horror"], label="Horror")
    
    plt.xlabel('Year')
    plt.ylabel('Popularity')
    
    plt.title("Popularity of Movies in Each Genre")
    
    plt.legend()
    
    plt.show()
    #beingsaved.savefig('TEST2.jpg', format='jpg', dpi=1000)
    
    
    # INDUSTRY FRACTION
    #beingsaved = plt.figure()
    
    plt.plot(pct_count["Action"], label="Action")
    plt.plot(pct_count["Romance"], label="Romance")
    plt.plot(pct_count["Sci-Fi"], label="Sci-Fi")
    plt.plot(pct_count["Horror"], label="Horror")
    
    plt.xlabel('Year')
    plt.ylabel('Number in Percentage')
    
    plt.title("Number of Movies in Each Genre in Percentage")
    
    plt.legend()
    
    plt.show()
    #beingsaved.savefig('TEST3.jpg', format='jpg', dpi=1000)
    

    # AVERAGE POPULARITY
    #beingsaved = plt.figure()
    
    plt.plot(avg_pop["Action"], label="Action")
    plt.plot(avg_pop["Romance"], label="Romance")
    plt.plot(avg_pop["Sci-Fi"], label="Sci-Fi")
    plt.plot(avg_pop["Horror"], label="Horror")
    
    plt.ylim(0, 270000)
    plt.xlabel('Year')
    plt.ylabel('Average Popularity')
    
    plt.title("Average Popularity of Movies")
    plt.tight_layout()
    plt.legend()
    
    plt.show()
    #beingsaved.savefig('TEST4.jepg', format='jpeg', dpi=900)
    


    