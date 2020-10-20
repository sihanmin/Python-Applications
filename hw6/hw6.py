#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:51:44 2019

@author: mintmsh
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

def heart(im):
    X = im.shape[0]
    Y = im.shape[1]
    x, y = np.ogrid[0:X, 0:Y]
    
    X1 = 0.31 * X
    Y1 = 0.25 * Y
    Y2 = 0.75 * Y
    
    slope = 2 * (X - X1) / Y
    reshape = Y1 / X1
    r = Y1
    
    im1 = im.copy()
    
    mask1 = (x - slope * y) > X - Y/2 * slope
    mask2 = ((X - x) - slope * y) < (-1) * Y/2 * slope
    mask3 = ((reshape*(x - X1))**2 + (y - Y1)**2 > r**2) & ((reshape*(x - X1))**2 + (y - Y2)**2 > r**2) & (x < X1)
    
    im1[mask1 | mask2 | mask3] = [255/255.0 , 210/255.0 , 232/255.0]
    return im1


def blurring(im, method):
    if method != "uniform" and method != "Gaussian":
        print ("Wrong method argument!")
        return
    
    k = 5
    sigma = 1
    if method == "uniform":
        filter = np.array([[1.0/k**2]*k]*k)
    elif method == "Gaussian":
        k = 5
        filter=np.array([[0]*k]*k,dtype='float')
        for x in range(k):
            for y in range(k):
                filter[x,y]=np.exp(-((x-(k-1)*0.5)**2+(y-(k-1)*0.5)**2)/(2.0*sigma**2))
        filter_sum=np.sum(filter)
        filter=filter/filter_sum
        
    #print(filter)
    a = int(k / 2)
    b = int(k / 2) + 1
    im1 = im.copy()
    for i in range(b, im1.shape[0] - a):
        for j in range(b, im1.shape[1] - a):
            for p in range(im1.shape[2]):
                im1[i,j,p] = np.sum(im[i-a:i+b, j-a:j+b, p] * filter)
    
    return im1
    

def detect_edge(im, method):
    if method != "horizontal" and method != "vertical" and method != "both":
        print ("Wrong method argument!")
        return
    
    h_filter=np.array([[-1,-2,-1],[ 0, 0, 0],[ 1, 2, 1]])
    v_filter=np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])

    a = 1
    b = 2
    im1 = im.copy()
    for i in range(b, im1.shape[0] - a):
        for j in range(b, im1.shape[1] - a):
            for p in range(im1.shape[2]):
                if method == "horizontal":
                    Sh = np.sum(im[i-a:i+b, j-a:j+b, p] * h_filter)
                    im1[i,j,p] = (Sh + 4) / 8
                elif method == "vertical":
                    Sv = np.sum(im[i-a:i+b, j-a:j+b, p] * v_filter)
                    im1[i,j,p] = (Sv + 4) / 8
                elif method == "both":
                    Sh = np.sum(im[i-a:i+b, j-a:j+b, p] * h_filter)
                    Sv = np.sum(im[i-a:i+b, j-a:j+b, p] * v_filter)
                    im1[i,j,p] = math.sqrt(Sh**2 + Sv**2) / 4
    
    return im1
    
'''
def gauss_noise(im,p=0.5):
    im1=im[:,:,0].copy()
    n,m=im1.shape
    noise=np.random.normal(0,np.var(im1)**(0.5)*p,[n,m])
    noisy_im1=im1+noise
    for i in range(n):
        for j in range(m):
            if noisy_im1[i,j]>1:
                noisy_im1[i,j]=1
            elif noisy_im1[i,j]<0:
                noisy_im1[i,j]=0
    noisy_im=[[[noisy_im1[i,j]]*3 for j in range(m)] for i in range(n)]
    return noisy_im


if __name__ == '__main__':
    img=mpimg.imread('IMG_3688.JPG') 
    #print img.dtype
    img = img/255.0 #Convert to 64-bit floating point.
    heart_img = heart(img)
    plt.imshow(heart_img)
    plt.show()
    
    
    greyImg = img[:,:,0]*0.21+img[:,:,1]*0.72+img[:,:,2]*0.07
    greyImg = np.repeat(greyImg[:, :, np.newaxis], 3, axis=2)
    plt.imshow(greyImg)
    plt.show()
    
    noiseImg = np.array(gauss_noise(greyImg))
    plt.imshow(noiseImg)
    plt.show()
    
    blur_img0 = blurring(noiseImg, "uniform")
    plt.imshow(blur_img0)
    plt.show()
    
    blur_img1 = blurring(noiseImg, "Gaussian")
    plt.imshow(blur_img1)
    plt.show()
    
    
    plt.imshow(img)
    plt.show()
    
    edge0 = detect_edge(img, "horizontal")
    plt.imshow(edge0)
    plt.show()
    
    edge1 = detect_edge(img, "vertical")
    plt.imshow(edge1)
    plt.show()
    
    edge2 = detect_edge(img, "both")
    plt.imshow(edge2)
    plt.show()
'''