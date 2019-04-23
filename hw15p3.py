#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 10:47:35 2019

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



print('hi')

os.getcwd()
os.chdir('/Users/warrenkeil/documents/OR2') # enter working directory 

# Homework Problem 15.3   Simulated annealing on single machine tardiness

dat = pd.DataFrame(index_col=0)

dat['Job'] = range(1,10)
dat['ProcTime'] = [33,17,6,40,22,8,27,19,30]
dat['DueDate'] = [35,90,43,85,60,23, 76,59,99]

x0 = [0,1,2,3,4,5,6,7,8]

x0 = [2,1,0,3,6,4,5,8,7]

def comptime(x0):
    c = [0]*len(x0)
    
    for i in range(0,len(x0)):
        ind = x0.index(i)
        for j in range(0,ind+1):
            c[i] = c[i]+ dat.iloc[x0[j],1]
            
    return c

c = comptime(x0)
        

def tardy(x0,c):
    t=[0]*len(x0)
    
    for i in range(0,len(x0)):
        t[i]= max(c[i]-dat.iloc[i,2],0)
        
    return t

t=tardy(x0,c)
    
def cost(t):
    sum(t)
    
    
###### sim annealing algo with 2-opt n-hood, I am running until cooled
    ##  problem says to run just 5 iterations. 
    
x = [0,1,2,3,4,5,6,7,8]  # initial solution
c =comptime(x)
t = tardy(x,c)
currentcost = sum(t)


iterr = 0
T= 75
cool = .000004
alpha = .8
bestcost = cos.copy()
bestsol = x.copy()

while T > cool:
    iterr = iterr + 1
    k1 = random.randint(0,7)
    k2 = random.randint(0,7)
    
    xbar = x.copy()
    xbar[min(k1,k2):max(k1,k2)+1] = list(reversed(xbar[min(k1,k2):max(k1,k2)+1]))
    
    
    newcost = sum(tardy(xbar,comptime(xbar)))
    if newcost < bestcost:
        bestcost = newcost.copy()
        bestsol = xbar.copy()
    
    if newcost < currentcost:
        x = xbar.copy()
    else:
        p = random.random()
        
        if p<= math.exp(-abs(newcost-currentcost)/T):
            x=xbar.copy()
    
    T = alpha*T
        
        

### Answer when running for high alph and high T and low cooling, 
    # we get the best cost is 302 total tardiness. 
    
    # for using book's parameters, we get around 340
    # Note i did not run for 5 iterations because that was not 
    #interesting. 


    
    