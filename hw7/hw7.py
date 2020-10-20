#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:16:55 2019

@author: mintmsh
"""

from scipy.misc import imread # using scipy's imread
import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import resize
from sklearn import svm

N = 4

def boundaries(binarized,axis):
    # variables named assuming axis = 0; algorithm valid for axis=1
    # [1,0][axis] effectively swaps axes for summing
    rows = np.sum(binarized,axis = [1,0][axis]) > 0
    rows[1:] = np.logical_xor(rows[1:], rows[:-1])
    change = np.nonzero(rows)[0]
    ymin = change[::2]
    ymax = change[1::2]
    height = ymax-ymin
    too_small = 10 # real letters will be bigger than 10px by 10px
    ymin = ymin[height>too_small]
    ymax = ymax[height>too_small]
    return zip(ymin,ymax)

def separate(img):
    orig_img = img.copy()
    pure_white = 255.
    white = np.max(img)
    black = np.min(img)
    thresh = (white+black)/2.0
    binarized = img<thresh
    row_bounds = boundaries(binarized, axis = 0) 
    cropped = []
    for r1,r2 in row_bounds:
        img = binarized[r1:r2,:]
        col_bounds = boundaries(img,axis=1)
        rects = [r1,r2,col_bounds[0][0],col_bounds[0][1]]
        cropped.append(np.array(orig_img[rects[0]:rects[1],rects[2]:rects[3]]/pure_white))
    return cropped


def partition(data, target, p):
    if (p > 1 or p < 0):
        return "Invalid: p should be between 0 and 1"
    
    # the following commanded code partitioned each class
    # proportionately into test and train sets
    '''
    S = data.shape[1]
    data = data.reshape(N,-1, S)
    target = target.reshape(N,-1)
    size = target.shape[1]
    m = int(size * p)
    
    train_data = data[:,:m,:].reshape(-1, S)
    train_target = target[:,:m].reshape(-1)
    test_data = data[:,m:,:].reshape(-1, S)
    test_target = target[:,m:].reshape(-1)
    '''
    
    # the following code partitioned data set randomly into test and train sets
    # it does not gauranteed the proportion of each class 
    l = len(target)
    m = int(l * p)
    train_i = np.random.choice(l,m, False)
    all_i = np.arange(l)
    all_i[train_i] = -1
    test_i = all_i[all_i > -1]

    train_data = data[train_i]
    train_target = target[train_i]
    test_data = data[test_i]
    test_target = target[test_i]
    
    return train_data, train_target, test_data, test_target


if __name__ == '__main__':
    # Reads in one image, slice it into N columms
    # where N is the number of classes
    big_img = imread("all.jpeg", flatten = True) # flatten = True converts to grayscale
    #plt.imshow(big_img/255,cmap='gray')
    #plt.show()
    wid = (big_img.shape[1] - 15) / N
    imgs = []
    target = []
    
    # for each column of letters, seprates each instance and labels it
    for i in range(N):
        start = i * wid
        end = start + wid
        col_img = big_img[:, start:end]
        #plt.imshow(col_img/255,cmap='gray')
        #plt.show()
        
        temp_imgs = separate(col_img) # separates big_img (pure white = 255) into array of little images (pure white = 1.0)
        imgs.extend(temp_imgs)
        target.extend([i for j in range(len(temp_imgs))])
    
    # then resizes all images and flattens into 1-D array
    for i in range(len(imgs)):
        imgs[i] = resize(imgs[i], (10,10))
        #plt.imshow(imgs[i], cmap='gray')
        #plt.show()
        imgs[i] = imgs[i].ravel()
    
    # patition the data set into train and test sets
    imgs = np.array(imgs)
    target = np.array(target)
    train_data, train_target, test_data, test_target = partition(imgs, target, 0.8)
    
    # fits training data into SVM
    clf = svm.SVC(gamma = 0.001, C= 100) 
    clf.fit(train_data,train_target)
    
    # predicts test data with the model and calculate accuracy
    predict = clf.predict(test_data)
    accuracy = sum(predict == test_target) * 100.0 / len(predict) 
    
    # prints out result
    print 'Predicted: ', predict
    print 'Truth: ', test_target
    print 'Accuracy:  ', accuracy, '%'