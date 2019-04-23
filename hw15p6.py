#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 15:13:26 2019

@author: warrenkeil
"""

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


### 15.5  Run Tabu search for single machine tardy

dat = pd.DataFrame()

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
    return sum(t)
    
    
x = [0,1,2,3,4,5,6,7,8]  # initial solution
c =comptime(x)
t = tardy(x,c)
currentcost = sum(t)
noimprov = 0
k=4    #  this is tabu list size
tabu = [None]*k


iterr = 0


bestcost = cost(t)
bestsol = x.copy()



def available(t0,tabu):
    avails = []
    for el in t0:
        if el not in tabu:
            avails = avails + [el]
    return avails

t0 = x.copy()

while noimprov < 100000:
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
    
    c = comptime(xbar)
    
    t = tardy(xbar,c)

    
    newcost = cost(t)
    
    if newcost < bestcost:
        bestcost = newcost
        bestsol = xbar.copy()
        noimprov =0
    
        
    temp = tabu.copy()    # update tabu list
    
    
    tabu[3]=tabu[1]
    tabu[2]=tabu[0]
    tabu[1]=k2
    tabu[0]=k1
  
    x = xbar.copy()
    
        
#  Running multiple times, the best cost i have gotten is 289 while setting 
    # noimprov to 100000
    # bestsol = [5,7,2,4,6,1,8,0,3] 