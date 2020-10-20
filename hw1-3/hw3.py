#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 16:56:50 2019

@author: mintmsh
"""
#import numpy as np

'''
Problem 1:
Write a function mytype(v) that performs the same action as type(), 
and can recog- nize integers, floats, strings, and lists. Do this by 
first using str(v), and then reading the string. Assume that lists 
can only contain numbers (not strings, other lists, etc...), and 
assume that strings can be anything that is not an integer, float or list.
'''
import re

def mytype(v):
    vstr = str(v)
    #reg = r'^[-+]?[0-9]+$'
    #print(vstr)
    
    # int: optional + or - sign, one or more numbers from start to end
    if bool(re.search( r'^[-+]?[0-9]+$',vstr)):
        return 'int'
    
    # float: optional + or - sign, zero or more numbers followed by '.' followed by
    # one or more numbers
    if bool(re.search( r'^[-+]?[0-9]*\.[0-9]+$', vstr)):
        return 'float'
    
    # list:'[' followed by zero or more space, followed by any int or float, followed
    # by any number of combination of spaces by ',' by int or float by ' ', lastly by
    # ']'
    reg = r'^\[ *([-+]?[0-9]+|[-+]?[0-9]*\.[0-9]+ *)(, *([-+]?[0-9]+|[-+]?[0-9]*\.[0-9]+) *)*\]$'
    if bool(re.search(reg, vstr)):
        return 'list'

    # else it is a string
    return 'str'
    
'''
Problem 2:
Write a function findpdfs(L) that takes as input a list L of filenames 
(such as “IMG2309.jpg”, “lecture1.pdf”, “homework.py”), and returns a 
list of the names of all PDF files, without extension (“lecture1”). Assume 
that filenames may contain only letters and numbers.
'''

def findpdfs(L):
    # put all file names into a string separated by space
    Lstr = ' '.join(L)
    # find all files ends with '.pdf' (case insensitive) using lookforwards
    # this removes the '.pdf' part
    Lpdf = re.findall(r'[a-zA-Z0-9]+(?=[.][p|P][d|D][f|F])', Lstr)
    return Lpdf

'''
Problem 3:
Write a function findemail(url) that takes as input a URL, and outputs any 
email addresses that look like “xxx@xxx.xxx.xxx” with any number of dots 
after the @-sign on this page. Your function should also get around tricks 
people use to hide their email addresses, such as

     hqcai@math.ucla.edu
     hqcai AT math DOT ucla DOT edu
     hqcai at math dot ucla dot edu
     hqcai[AT]ucla[DOT]edu
     hqcai[at]ucla[dot]edu
     
     hqcai@math.ucla.edu  hqcai AT math DOT ucla DOT edu  hqcai at math dot ucla dot edu  hqcai[AT]ucla[DOT]edu  hqcai[at]ucla[dot]edu
'''
import urllib2
#import urllib

def findemail(url):
    #page = urllib.request.urlopen(url).read()
    page = urllib2.urlopen(url).read()

    page = str(page)
    # else there is an error "TypeError: a bytes-like object is required, not 'str'"
    
    # replace all the tricks with original format “xxx@xxx.xxx.xxx”
    page = page.replace(r' AT ', '@').replace(r' at ', '@').replace(r'[AT]', '@').replace(r'[at]', '@')
    page = page.replace(r' DOT ', '.').replace(r' dot ', '.').replace(r'[DOT]', '.').replace(r'[dot]', '.')
    
    # find all emails with the pattern 
    emails = re.findall(r'[\w]+@[\w\.-]+', page)
    
    
    '''
    The spec says "any number of dots after the @-sign". However, when the number is 
    zero, it might be a problem:
        
    Since on the webpage, sentences like "research at UCLA" or "look at professor"
    are all matched taken as email addresses like 'research@UCLA' and 'look@professor'
    mistakenly, I remove those attributes by defining there should be at least one 
    dot after @ sign. In this way "whatever@com" would not be included in my email
    list.
    '''
    rm_emails = []
    for email in emails:
        if bool(re.search(r'^\w+@\w+$', email)):
            rm_emails.append(email)
    for email in rm_emails:
        emails.remove(email)
    '''
    If the sentences above like "research at UCLA" should be counted as email address,
    please comment out the codes between these two comments.
    '''
    
    return emails


'''
Problem 4:
Write a function happiness(text) that uses the Dodds et al [1] happiness dictionary to 
rate the happiness of a piece of english text (input as a single string). The happiness 
score is the average score over all words in the text that appear in the dictionary. 
For simplicity, you may neglect the words with special characters in the dictionary.
'''

from happiness_dictionary import happiness_dictionary

def happiness(text):
    # find all the words (without special characters)
    words = re.findall(r'[A-Za-z]+', text)
    low = []
    # turn them into lower case
    for word in words:
        low.append(word.lower())
    
    num = 0
    total = 0
    # count the total number of happy words and their total scores
    # if the same word appears twice, count it twice
    for word in low:
        if word in happiness_dictionary:
            num += 1
            total += happiness_dictionary[word]
            #print(word, happiness_dictionary[word])
    
    #print(total, num)
    # return average score       
    return total / num

'''
if __name__ == '__main__':
    
    ans = mytype('[0,    2,3.245  , -777 ]')
    print(ans)
    ans = findpdfs(['x444P.pdf', 'sdf', 'df.PdF', '423sodf.JPG'])
    print(ans)
    ans = findemail("https://www.math.ucla.edu/contact-us")
    print(ans)
    ans = happiness('Adfs happy asdfi, asdkFfewic,sad happy, happiness, proud')
    print(ans)

'''












