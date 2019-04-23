#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:00:49 2019

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


A = np.array([[0, 13, 8, 15, 7, 16, 19, 21],[13, 0, 5, 7, 14, 22, 11, 14],[8, 5, 0, 15, 17, 9, 13, 12],[15, 7, 15, 0, 8, 7, 9, 10],[7, 14, 17, 8, 0, 12, 18, 11],[16, 22, 9, 7, 12, 0, 8, 14],[19, 11, 13, 9, 18, 8, 0, 15],[21, 14, 12, 10, 11, 14, 15,0]])


# 15.1 Run a simulated annealing algorithm on the TSP problem in matrix A. 

t0 = list(range(0, A.shape[1])) # initial solution

def cost(t0):
    s = 0
    for i in range(0,len(t0)):
        s = s + A[t0[i],t0[(i+1)%len(t0)]]
        
    return s

i=i+1


cost(t0)


t0 = [7,6,5,3,1,4,0,2]

#    TSP Simulated Annealing With k-opt Neighborhood

t0 = list(range(0, A.shape[1])) # initial solution
x = t0.copy()
currentcost = cost(x)
iterr = 0
T= 500
cool = .00004
alpha = .999
bestcost = cost(x).copy()
bestpath = t0.copy()

while T > cool:
    iterr = iterr + 1
    k1 = random.randint(0,7)
    k2 = random.randint(0,7)
    
    xbar = x.copy()
    xbar[min(k1,k2):max(k1,k2)+1] = list(reversed(xbar[min(k1,k2):max(k1,k2)+1]))
    
    
    newcost = cost(xbar)
    if newcost < bestcost:
        bestcost = newcost.copy()
        bestpath = xbar.copy()
    
    if newcost < currentcost:
        x = xbar.copy()
    else:
        p = random.random()
        
        if p<= math.exp(-abs(newcost-currentcost)/T):
            x=xbar.copy()
    
    T = alpha*T
        
        
        
# Note: we get bestcost = 67 every time we run it.
    # We get multiple solutions that give us this path. 
    
    
p1 = [4,3,6,5,1,2]
p2 = [1,5,2,3,6,4]  
c1 = 3
c2 = 6 
    


def cross2(p1,p2,c1,c2):
    domain = p1[min(c1,c2):max(c1,c2)]
    codomain = p2[min(c1,c2):max(c1,c2)] 
    
    #new1 = [0]*len(p1)
    #new2 = [0]*len(p2) 
    def eff(p1,domain,codomain):
        newp1 = [0]*len(p1)
        for i in range(0,len(p1)):
            if p1[i] in domain:
                ind1=domain.index(p1[i])
                newp1[i] = codomain[ind1]
            elif p1[i] in codomain:
                ind1 = codomain.index(p1[i])
                newp1[i] = domain[ind1] 
            else:
                newp1[i] = p1[i]
        return newp1
                
    new1 = eff(p1,domain,codomain)
    new2 = eff(p2,domain,codomain) 
                
    return new1, new2

    
cross2(p1,p2,c1,c2)



def cross3(p1,p2,c1,c2):
    
    k1 = p1[min(c1,c2):max(c1,c2)]
    k2 = p2[min(c1,c2):max(c1,c2)]
    
    ind1 = [0]*len(k2)
    ind2 = [0]*len(k1)
    
    new1 = [0]*len(p1)
    new2 = [0]*len(p2)
    

    for i in range(0,len(k2)):
        ind1[i] = p1.index(k2[i])
    
    for i in range(0,len(k1)):
        ind2[i] = p2.index(k1[i])
        
    ind1.sort()
    ind2.sort()
    
    for i in ind1:
        new1[ind1[i]] = k1[i]
    
    for i in ind2:
        new2[ind2[i]] = k2[i]
    
    for i in range(0,len(k1)):
        new1[i+c1] = k2[i]
        new2[i+c1] = k1[i]
    

    return new1,new2

cross3(p1,p2,c1,c2)


