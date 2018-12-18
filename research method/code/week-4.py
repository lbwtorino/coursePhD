#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 09:25:29 2018

@author: liubowen
"""

import matplotlib.pyplot as plt
import numpy as np
import csv
import scipy.stats as ss
#=========================================================================
def binomialCoeff(n, k): 
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result

NBalls = 100
Nlayers = 16
Prob = 0.5
Tmean = Prob* Nlayers 
Tstdv = np.sqrt(Nlayers*Prob**2)
print "Theoretical mean=", Tmean
print "Theoretical Standard Dev =", Tstdv 
print "Coefficient of Variation", Tstdv/Tmean
data =[]
for i in range(NBalls):
    data.append(np.random.binomial(Nlayers, Prob))

x = np.linspace(0,(Tmean + 4 * Tstdv),1000) 
y = ss.norm(Tmean, Tstdv).pdf(x)
plt.figure()
plt.hist(data, color='red',bins=(Nlayers+1), align='left', range=(0,Nlayers+1), normed
=1,edgecolor='black') 
plt.xlabel('balls=1000, layers=8') 
plt.plot(x,y)
#plt.savefig('1.jpg')
##============================================================================
def f0(l,c):
    return 1.0/(2*np.pi*np.sqrt(l*c))

def OneSample(Num): #returns the mean and standev of a sample containing Num random variables
    freq =[]
    for sample in range(Num):
        l = ss.norm.rvs(2.5e-3, 2.5e-4) 
        c = ss.norm.rvs(10e-6, 0.5e-6) 
        freq.append(f0(l,c))
    mean = np.mean(freq) 
    sigma = np.std(freq, ddof=1) #sample standard deviation #print mean , sigma
    return mean ,sigma , freq
###CASE PROBLEM 4.7(b) 
F = OneSample(1000)[2] #take a sample of 10000 random variables
plt.figure()
plt.hist(F, bins='auto',color='red', edgecolor='black', align='left') 
plt.xlabel('Freq_(Hz)') 
plt.ylabel('Freq') 
print OneSample(1000)[0]
print OneSample(1000)[1]
#plt.xlim(800,1300) 
#fname='cp4_7b'+str(1000)+'.pdf'
#plt.savefig(fname)
print OneSample(36)[0]
print OneSample(36)[1]

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
#numofsamples =1
#F = sampleDist(numofsamples ,5000) 
#plt.figure()
#plt.hist(F, bins='auto',edgecolor="black", align='left') 
#plt.xlabel('Freq_(Hz)') 
#plt.ylabel('Freq')
#plt.xlim(800,1200) 

#numofsamples =10 
#F = sampleDist(numofsamples ,5000)
#plt.figure()
#plt.hist(F, bins='auto',edgecolor="black", align='left') 
#plt.xlabel('Freq_(Hz)') 
#plt.ylabel('Freq')
#plt.xlim(800,1200) 
#
#numofsamples =100
#F = sampleDist(numofsamples ,5000)
#plt.figure()
#plt.hist(F, bins='auto',edgecolor="black", align='left') 
#plt.xlabel('Freq_(Hz)') 
#plt.ylabel('Freq')
#plt.xlim(800,1200) 
#
#fname='cp4_7d'+str(numofsamples)+'.pdf' 
#plt.savefig(fname)
#======================================================================
def boat_t(r,angle_rad ,v):
    return r*angle_rad*np.pi/(180*v)
def OneSample(r,theta,v,Er,Etheta,Ev,Num): 
    t=[]
    for sample in range(Num): 
        angle=ss.norm.rvs(theta,Etheta) 
        speed=ss.norm.rvs(v,Ev) 
        radius=ss.norm.rvs(r, Er) 
        t.append(boat_t(radius , angle , speed))
    mean=np.mean(t)
    sigma=np.std(t, ddof=1) #sample standard deviation #print "stats:", mean, sigma
    return mean, sigma

def sampleDist(N_samples,NExpts): #creates a sample distribution (i.e. the distribution of means NExpts)
    times =[]
    for sample in range(NExpts):
        times.append(OneSample(10,30,0.6,0.1,5,0.1,N_samples)[0]) 
    return times

boatimes=sampleDist(40,500)
plt.figure()
plt.hist(boatimes, bins='auto', edgecolor='black') 
plt.xlabel('times_(s)')
plt.ylabel('Freq')
plt.xlim(6,12)