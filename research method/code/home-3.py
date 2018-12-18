#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 14:11:03 2018

@author: liubowen
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as ss   
import math
#===================================================
#problem 1-a
#print np.sin(45.0/180*np.pi)
#def calPoE(N1, mean1, var1, mean2, var2):
#    deriva1 = N1 / np.sin(mean2/180.0*np.pi) * np.cos(mean1/180.0*np.pi)
#    deriva2 = (N1*np.sin(mean1/180.0*np.pi)) * (-np.cos(mean2/180.0*np.pi)) / np.sin(mean2/180.0*np.pi)**2
#    poe = var1**2 * deriva1**2 + var2**2 * deriva2**2
#    N2 = N1 * np.sin(mean1/180.0*np.pi) / np.sin(mean2/180.0*np.pi)
#    return np.sqrt(poe)/180.0*np.pi, N2
#
#N1 = 1.0
#mean1 = 22.02
#var1 = 0.02
#mean2 = 14.45
#var2 = 0.02
#print calPoE(N1, mean1, var1, mean2, var2)
    

#1-c

#def tFunc(N1, rad1, rad2):
#    return N1 * np.sin(rad1/180.0*np.pi) / np.sin(rad2/180.0*np.pi)
#
#def MC(Num): 
#    t =[]
#    for sample in range(Num):
#        rad1 = ss.norm.rvs(22.02, 0.02) 
#        rad2 = ss.norm.rvs(14.45, 0.02) 
#        N1 = 1.0
#        t.append(tFunc(N1, rad1, rad2))
#    mean = np.mean(t)
#    stdDeviat = np.std(t, ddof=1)
#    return mean, stdDeviat, t
#
#Num = 1
#his = MC(Num)[2]
##print MC(Num)[0], MC(Num)[1]
#plt.figure()
#plt.hist(his, bins='auto',color='red', edgecolor='black', align='left') 
#plt.xlabel('n2') 
#plt.savefig('home-3.pdf')
#
#print ss.norm(0,1).ppf(1-0.025)

#================================================
#problem-2


#def chi():
#    obs = [352, 501, 371, 126, 150]
#    expe = [375, 525, 375, 150, 75]
#    return ss.chisquare(obs,expe)[0], ss.chisquare(obs,expe)[1]
#
#print chi()


#================================================
# problem-3b

#def conInterval(N, p, value):
#    minimum = p - value * np.sqrt(p*(1-p)/N)
#    maximum = p + value * np.sqrt(p*(1-p)/N)
#    return minimum, maximum
#N=85
#p=10/85.0
#value=ss.norm(0,1).ppf(1-0.025)
#print conInterval(N, p, value)
## problem-3c
#
#def calN(value, Est, p):
#    return (value/Est)**2 * p*(1-p)
#
#value=ss.norm(0,1).ppf(1-0.025)
#Est = 0.05
#p = 0.5
#print calN(value, Est, p)
    
#================================================