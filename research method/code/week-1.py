#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 16:13:46 2018

@author: liubowen
"""

import math
import numpy as np #Scientific computing 
import matplotlib.pyplot as plt #Plotting 
import scipy as sp #Science, Maths, Stats The

print 'hello'

print 1/3

a = "italy"
b=1
c=1.1
print type(a)
print type(b)
print type(c)

def calculate():
    a = 3;
    b = 4;
    return math.sqrt(a**2+b**2);

print calculate()

print np.cos(0)

x=np.linspace(-1, 10, 21)
y=np.sin(x)
plt.plot(x,y, linewidth=1, color='r', marker='x')

print round(3.1)
print round()
