#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 16:20:27 2018

@author: liubowen
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:30:06 2018

@author: liubowen
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as ss   
import math

##=====================================================
#problem-1 permutation method
#def t_c(r, Q = 1.0e12):
#    p0 = 5.0e9
#    return math.log(Q*r/p0+1)/r
#
#def tdr(r, Q, p):
#    h = p*r;
#    return (t_c(r+h, Q)-t_c(r-h))/(2*h)
#
#def tdQ(r, Q, p):
#    h = Q*p;
#    return (t_c(r, Q+h)-t_c(r, Q-h))/(2*h)
#
#x = np.logspace(-6, -1, 1000)
#r = 0.027
#Q = 1.0e12
#t = []
#for i in x:
#    t2 = (0.002**2)*(tdr(r, Q, i))**2 + (1e11)**2*(tdQ(r, Q, i))**2
#    t.append(math.sqrt(t2))
#
#print (t_c(0.027))
#plt.plot(x, t)

#=======================================================
# problem-1 analytical method

#def tFunc(Q, r, P0):
#    return (np.log((Q*r/P0)+1)) / r
#
#def rDerivation(Q, r, P0):
#    return ((Q*r) / (Q*r + P0) - np.log(Q*r/P0 + 1)) / r**2
#
#def qDerivation(Q, r, P0):
#    return (1.0/r) * (1.0 / (Q*r/P0 + 1)) * (r/P0)
#
#def stdDeviat(Q, r, dQ, dr, P0):
#    analytical_ans = rDerivation(Q, r, P0)**2 * dr**2 + qDerivation(Q, r, P0)**2 * dQ**2
#    return np.sqrt(analytical_ans)
#
#Q, r, dQ, dr, P0 = 1000, 0.027, 100, 0.002, 5
#print 'Problem 1-a result:',  stdDeviat(Q, r, dQ, dr, P0)

#=======================================================        

#def tFunc(Q, r, P0):
#    return (np.log((Q*r/P0)+1)) / r
#
#def MC(Num): 
#    t =[]
#    for sample in range(Num):
#        Q = ss.norm.rvs(1000, 100) 
#        r = ss.norm.rvs(0.027, 0.002) 
#        P0 = 5.0
#        t.append(tFunc(Q, r, P0))
#    stdDeviat = np.std(t, ddof=1)
#    return stdDeviat
##
#Num = 1000000
#print MC(Num)
#
#x = np.arange(10000, 1000000, 100)
#std = []
#for i in x:
#    std.append(MC(i))
#plt.plot(x, std)

#
#def sampleDist(N_samples, NExpts): #creates a sample distribution (i.e . the distribution of means NExpts )
#    freq=[]
#    for sample in range(NExpts):
#        freq.append((OneSample(N_samples))[0])
#    mean = np.mean(freq) 
#    sigma = np.std(freq, ddof=1)
#    return freq, mean, sigma
##print sampleDist(36, 500)[1]
##print sampleDist(36, 500)[2]
#numofsamples =1000
#F = sampleDist(numofsamples, 50)[0] 
#plt.figure()
#plt.hist(F, bins='auto',edgecolor="black", align='left') 
#plt.xlabel('Freq_(Hz)') 
#plt.ylabel('Freq')
#print sampleDist(numofsamples, 500)[2] 

#======================================================
#Problem 2

#kb = 8.6173303e-5
#
#def xValue(Tc):
#    return (-1 / (kb * Tc))
#
#def yValue(phi, Tc):
#    return np.log(phi / Tc**2)
#
#def calculateC(Tc_array, pfi_array):
#    x_value = []
#    y_value = []
#    for i in range(len(Tc_array)):
#        x_value.append(xValue(Tc_array[i]))
#        y_value.append(yValue(pfi_array[i], Tc_array[i]))
#    gradient, C = np.polyfit(x_value, y_value, 1) 
#    x_mean = np.mean(x_value) 
#    y_mean = np.mean(y_value) 
#    return C, x_mean, y_mean
#
#Tc_array = [440.6, 440.3, 439.7, 438.2, 437.3, 434.4, 431.7, 429.7];
#pfi_array = [4.5, 3.4, 3.2, 2.7, 2.1, 1.0, 0.8, 0.5]   
#C, x_mean, y_mean = calculateC(Tc_array, pfi_array)
#print 'The intercept C:', C 
#
#def Ea(Tc, pfi, C):
#    return kb * Tc * (C - np.log(pfi / np.square(Tc)))
#
#meanTc = -1 / (x_mean*kb)
#meanpfi = math.exp(y_mean)* meanTc**2 
#print 'The Tc mean:', meanTc
#print 'The pfi mean:', meanpfi
#
#stdDeviatTc = 0.2
#stdDeviatpfi = 0.1
#num = 10000
#Ea_value = []
#
#def MCEa(Tc, stdTc, phi, stdphi, C, N_experiments):      
#    for i in range(N_experiments):
#        Tc_random = ss.norm.rvs(Tc, stdTc)
#        phi_random = ss.norm.rvs(phi, stdphi)
#        Ea_value.append(Ea(Tc_random, phi_random, C))
#    mean = np.mean(Ea_value)
#    stdDeviat = np.std(Ea_value)
#    stdError = stdDeviat / math.sqrt(N_experiments)
#    return mean, stdDeviat, stdError
#
#mean, stdDeviat, stdError = MCEa(meanTc, stdDeviatTc, meanpfi, stdDeviatpfi, C, num)
#print 'The Ea mean:', mean
#print 'The Ea standard deviation:', stdDeviat
#print 'The Ea standard error:', stdError
#num_bins = 100
#plt.hist(Ea_value, num_bins, facecolor='red', edgecolor='black')
#
#def EaBounds(meanEa, stdDeviaEa, confidence): 
#    z = ss.norm.ppf((1+confidence)/2) 
#    minEa = meanEa - stdDeviaEa * z
#    maxEa = meanEa + stdDeviaEa * z
#    return minEa, maxEa
#minEa, maxEa = EaBounds(mean, stdDeviat, 0.95)
#print 'The minimum Ea:', minEa
#print 'The maximal Ea:', maxEa
#=======================================================



