#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:14:40 2019

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
from heapq import nsmallest

#### Solve TSP using GRASP algorithm:  
#   GRASP - Greedy Randomized Adaptive Search Procedures


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


def intersec(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

cost(t0)
def which_switch(self):
    x = [self.states.index(i) for i in self.states if i == True]

#    TSP with GRASP: Greedy Randomized Adaptive Search Procedure. Rcl = restricted candidate list

t0 = list(range(0, A.shape[1])) # initial solution
x = t0.copy()
currentcost = cost(x)
iterr = 0
bestcost = cost(x).copy()
bestpath = t0.copy()
noimprov = 0 
avail = list(range(0, A.shape[1])) 
alpha = .35  # top percent of candidates to choose from 


while noimprov < 5000:
    iterr = iterr + 1
    noimprov = noimprov + 1
    
    
    avail = list(range(0, A.shape[1])) # list of available cities
    
    k1 = random.randint(0,len(x)-1) # pick random city
    
    avail.remove(k1)
    
    dist = list(A[:,k1][avail])
    
    rcl = list(nsmallest(math.floor(alpha*A.shape[1]),dist))
    
    if rcl[0]==rcl[1]:
        p=A[:,k1]==rcl[0]
        samp = random.choice(intersec([i for i, x in enumerate(p) if x],avail)) #index of A
        k2 = samp
        
    
    if rcl[0]!=rcl[1]:
        p0=A[:,k1]==rcl[0]
        p1=A[:,k1]==rcl[1]
        ##### flip coin
        flip = random.choice([0,1])
        if flip==0:
            samp = random.choice(intersec([i for i, x in enumerate(p0) if x],avail)) #index of A
        else:
            samp = random.choice(intersec([i for i, x in enumerate(p1) if x],avail)) 
        k2 = samp
                    
    avail.remove(k2)
    dist = list(A[:,k2][avail])
    rcl = list(nsmallest(math.floor(alpha*A.shape[1]),dist))

    if rcl[0]==rcl[1]:
        p=A[:,k2]==rcl[0]
        samp = random.choice(intersec([i for i, x in enumerate(p) if x],avail)) #index of A
        k3 = samp
    
    if rcl[0]!=rcl[1]:
        p0=A[:,k2]==rcl[0]
        p1=A[:,k2]==rcl[1]
        ##### flip coin
        flip = random.choice([0,1])
        if flip==0:
            samp = random.choice(intersec([i for i, x in enumerate(p0) if x],avail)) #index of A
        else:
            samp = random.choice(intersec([i for i, x in enumerate(p1) if x],avail)) 
        k3 = samp

                    
    avail.remove(k3)
    dist = list(A[:,k3][avail])
    rcl = list(nsmallest(math.floor(alpha*A.shape[1]),dist))

    if rcl[0]==rcl[1]:
        p=A[:,k3]==rcl[0]
        samp = random.choice(intersec([i for i, x in enumerate(p) if x],avail)) #index of A
        k4 = samp
        
    
    if rcl[0]!=rcl[1]:
        p0=A[:,k3]==rcl[0]
        p1=A[:,k3]==rcl[1]
        ##### flip coin
        flip = random.choice([0,1])
        if flip==0:
            samp = random.choice(intersec([i for i, x in enumerate(p0) if x],avail)) #index of A
        else:
            samp = random.choice(intersec([i for i, x in enumerate(p1) if x],avail)) 
        k4 = samp

                    
    avail.remove(k4)
    dist = list(A[:,k4][avail])
    rcl = list(nsmallest(math.floor(alpha*A.shape[1]),dist))

    if rcl[0]==rcl[1]:
        p=A[:,k4]==rcl[0]
        samp = random.choice(intersec([i for i, x in enumerate(p) if x],avail)) #index of A
        k5 = samp
        
    
    if rcl[0]!=rcl[1]:
        p0=A[:,k4]==rcl[0]
        p1=A[:,k4]==rcl[1]
        ##### flip coin
        flip = random.choice([0,1])
        if flip==0:
            samp = random.choice(intersec([i for i, x in enumerate(p0) if x],avail)) #index of A
        else:
            samp = random.choice(intersec([i for i, x in enumerate(p1) if x],avail)) 
        k5 = samp
        
    avail.remove(k5)
    dist = list(A[:,k5][avail])
    rcl = list(nsmallest(math.floor(alpha*A.shape[1]),dist))

    if rcl[0]==rcl[1]:
        p=A[:,k5]==rcl[0]
        samp = random.choice(intersec([i for i, x in enumerate(p) if x],avail)) #index of A
        k6 = samp
    
    if rcl[0]!=rcl[1]:
        p0=A[:,k5]==rcl[0]
        p1=A[:,k5]==rcl[1]
        ##### flip coin
        flip = random.choice([0,1])
        if flip==0:
            samp = random.choice(intersec([i for i, x in enumerate(p0) if x],avail)) #index of A
        else:
            samp = random.choice(intersec([i for i, x in enumerate(p1) if x],avail)) 
        k6 = samp
        
    avail.remove(k6)
    dist = list(A[:,k6][avail])
    rcl = list(nsmallest(math.floor(alpha*A.shape[1]),dist))

    if rcl[0]==rcl[1]:
        p=A[:,k6]==rcl[0]
        samp = random.choice(intersec([i for i, x in enumerate(p) if x],avail)) #index of A
        k7 = samp
        
    
    if rcl[0]!=rcl[1]:
        p0=A[:,k6]==rcl[0]
        p1=A[:,k6]==rcl[1]
        ##### flip coin
        flip = random.choice([0,1])
        if flip==0:
            samp = random.choice(intersec([i for i, x in enumerate(p0) if x],avail)) #index of A
        else:
            samp = random.choice(intersec([i for i, x in enumerate(p1) if x],avail)) 
        k7 = samp
     
    avail.remove(k7)
    
    k8 = avail[0]
    
    xbar = x.copy()
    xbar = [k1,k2,k3,k4,k5,k6,k7,k8]
    
    
    newcost = cost(xbar)
    if newcost < bestcost:
        bestcost = newcost.copy()
        bestpath = xbar.copy()
        noimprov = 0
    



    
        
        
# Note: we get bestcost = 67 every time we run it.
    # We get multiple solutions that give us this path. 
    
    
    
    