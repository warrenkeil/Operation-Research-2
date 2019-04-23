#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 17:11:02 2019

@author: warrenkeil
"""


import numpy
import pdb
import sys
import os
import math
import numpy as np
import pandas as pd
import dionysus as d
import csv
import matplotlib.pyplot as plt
import random 

#import pickle


print('hi')

os.getcwd()
os.chdir('/Users/warrenkeil/documents/OR2') # enter working directory 


A = np.array([[0, 13, 8, 15, 7, 16, 19, 21],[13, 0, 5, 7, 14, 22, 11, 14],[8, 5, 0, 15, 17, 9, 13, 12],[15, 7, 15, 0, 8, 7, 9, 10],              [7, 14, 17, 8, 0, 12, 18, 11],              [16, 22, 9, 7, 12, 0, 8, 14],              [19, 11, 13, 9, 18, 8, 0, 15],              [21, 14, 12, 10, 11, 14, 15,0]])


# 15.1 Run a simulated annealing algorithm on the TSP problem in matrix A. 

t0 = list(range(0, A.shape[1])) # initial solution

def cost(t0):
    s = 0
    for i in range(0,len(t0)):
        s = s + A[t0[i],t0[(i+1)%len(t0)]]
        
    return s




cost(t0)


t0 = [7,6,5,3,1,4,0,2]

#    TSP Simulated Annealing With k-opt Neighborhood  or TABU
t0 = list(range(0, A.shape[1])) # initial solution
x = t0.copy()
currentcost = cost(x)
iterr = 0
k = 4  # Tenure length. 
bestcost = cost(x).copy()
bestpath = t0.copy()
noimprov = 0
tabu = [None]*k
iterr = 0

def available(t0,tabu):
    avails = []
    for el in t0:
        if el not in tabu:
            avails = avails + [el]
    return avails


while noimprov < 2500:
    iterr = iterr + 1
    noimprov = noimprov + 1
    
    avail = available(t0,tabu)
    
    k1, k2= random.sample(avail,2) 
   
    xbar = x.copy()
    #xbar[min(k1,k2):max(k1,k2)+1] = list(reversed(xbar[min(k1,k2):max(k1,k2)+1]))
    
    ind1 = xbar.index(k1)
    ind2 = xbar.index(k2)
    
    val1 = xbar[ind1]
    val2 = xbar[ind2]

    xbar[ind1]=val2
    xbar[ind2]=val1
    
    newcost = cost(xbar)
    
    if newcost < bestcost:
        bestcost = newcost.copy()
        bestpath = xbar.copy()
        noimprov =0
    
        
    temp = tabu.copy()    # update tabu list
    
    
    tabu[3]=tabu[1]
    tabu[2]=tabu[0]
    tabu[1]=k2
    tabu[0]=k1
  
    x = xbar.copy()
    
        

# Results, After running many times, it appears as if the best cost i can get is 67. 
    # Even when running for longer time it does not always give best cost of 67. 