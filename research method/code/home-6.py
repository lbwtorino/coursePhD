#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 08:01:28 2018

@author: liubowen
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as ss

#ex-1

#ex-2
print ss.t.ppf(0.025, 84), ss.t.ppf(0.975, 84)

#ex-5
def factorial(x):  
    int_x= int(round(x))
    fact=1
    for i in range(int_x+1)[1:]:
        fact=fact*i
    return fact

def probFunc(x, mean):
    return np.power(mean, x) * 1.0 / np.exp(mean) / np.math.factorial(x)

print probFunc(0, 6.5) + probFunc(1, 6.5) + probFunc(2, 6.5)+ probFunc(3, 6.5)+ probFunc(4, 6.5) + probFunc(5, 6.5)

def calPoE(N1, mean1, var1, mean2, var2):
    deriva1 = N1 / np.sin(mean2/180.0*np.pi) * np.cos(mean1/180.0*np.pi)
    deriva2 = (N1*np.sin(mean1/180.0*np.pi)) * (-np.cos(mean2/180.0*np.pi)) / np.sin(mean2/180.0*np.pi)**2
    poe = var1**2 * deriva1**2 + var2**2 * deriva2**2
    N2 = N1 * np.sin(mean1/180.0*np.pi) / np.sin(mean2/180.0*np.pi)
    return np.sqrt(poe)/180.0*np.pi, N2

N1 = 1.0
mean1 = 22.02
var1 = 0.02
mean2 = 14.45
var2 = 0.02
print calPoE(N1, mean1, var1, mean2, var2)