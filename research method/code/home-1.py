#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 18:24:46 2018

@author: liubowen
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as ss
#import csv
#import scipy.stats.poisson as poisson
#import scipy.optimize.curve_fit as curve_fit

#=======================================================
#def calProb(n):
#    if n <= 0:
#        return -1;
#        print "n is not allowed input 0 and minus!"
#    return n * 1.0/n * 1.0/n;
#
#def calExpec(n):
#    prob = calProb(6);
#    return n * prob;
#
#def calVar(n):
#    prob = calProb(6);
#    return n * prob * (1 - prob);
#
#print calExpec(50)
#
#
#def calValueForNthrows(n):
#    retValue = {};
#    retValue['ExpecValue'] = calExpec(n);
#    retValue['Variance'] = calVar(n);
#    return retValue;
#
#times_of_throw = 50;
#print calValueForNthrows(times_of_throw)
#
#def plotFigure():
#    times = [1000, 10000, 100000];
#    for i in range(3):
#        testTimes = times[i];
#        n, p = testTimes, 1/6.0
#        s = np.random.binomial(n, p, testTimes)
#        plt.figure()
#        plt.xlabel('Occurrence')
#        plt.ylabel('Probability')
#        plt.hist(s, color='red', edgecolor='black', density=True, bins='auto')
#        
#plotFigure();
#=======================================================

#def factorial(x):  
#    int_x= int(round(x))
#    fact=1
#    for i in range(int_x+1)[1:]:
#        fact=fact*i
#    return fact
#
#
#
#def probFunc(x, mean):
#    return np.power(mean, x) * 1.0 / np.exp(mean) / np.math.factorial(x);
#
#
#mean_value = 6.5 / 2;
#print 'Problem-2 result:', probFunc(0,mean_value)+probFunc(1, mean_value)+probFunc(2, mean_value)
#
#for the mean is known
#def calUncert(n, p):
#    var = n * p * (1-p);
#    return var;
#
#def standardVar(n, p):
#    variance = calUncert(n, p);
#    return np.sqrt(variance);
#
#
#n_sample = 752 + 283
#p_sample = 752.0 / n_sample
#def calstandVarWed(n, p):
#    return standardVar(n, p);
#
#print 'Problem 3-3 results:', calstandVarWed(n_sample, p_sample)
#
#
#
#def calFarProb(p, number, sample_mean):
#    mean = p * number;
#    variance = standardVar(number, p);
#    return 2 * ss.norm(mean, variance).cdf(sample_mean);
#    
#n_sample = 752 + 283
#p = 0.75
#mean_wedn = 752
#print 'Problem 3-4 results:', calFarProb(p, n_sample, mean_wedn)

#========================================================
#A=[176, 191, 214, 220, 205, 192, 201, 190, 183, 185]
#def linefunc(x, m, c): #define function to fit return m*x + c
#    return m*x + c;
#
#def r2(meas_data , model_data): #compute R-squared 
#    avg = np.mean(meas_data)
#    print "The mean is", avg
#    i=0
#    ST =[]
#    SE =[]
#    for line in meas_data:
#        ST.append((line-avg)**2) # Square spread
#        SE.append((line- model_data[i])**2)
#        i=i+1 #counter
#    SST=sum(ST) 
#    SSE=sum(SE)
#    return (1-(SSE/SST))
#
#ranked=np.sort(A)
#Z_stat =[]
#for i in range(len(ranked)):
#    score=((i+1) -0.5)/len(ranked) #i
#    Z_stat.append(ss.norm(0,1).ppf(score))
#    
#params = sp.optimize.curve_fit(linefunc, Z_stat, ranked)
#[m, c] = params[0]
#fit=[]#creat the fit data
#for z in Z_stat:
#    fit.append(linefunc(z,m,c));
#
#plt.figure()
#plt.plot(Z_stat, ranked, marker='o', markerfacecolor='None') 
#plt.plot(Z_stat, fit) 
#plt.xlabel('z-statistic') 
#plt.ylabel('Ordered lifetimes')
#print r2(ranked, Z_stat)
#print ss.poisson(6).rvs(100)

sample = ss.poisson(50).rvs(10)
#sample = ss.norm.rvs(1)
#print sample
def destinationFunc(x, m, c): 
    return m * x + c;
def calR2(sorted_sample, destination_linear): #compute R-squared 
    counter = 0
    SStot =[]
    SSres =[]
    for _sample in sorted_sample:
        SStot.append((_sample - np.mean(sorted_sample)) ** 2)
        SSres.append((_sample - destination_linear[counter]) ** 2)
        counter = counter + 1
        return (1-(sum(SSres)/sum(SStot)))
    
    
sorted_sample = np.sort(sample)
std_norm_dis =[]
for i in range(len(sorted_sample)):
    score=((i + 1) - 0.5) / len(sorted_sample)
    std_norm_dis.append(ss.norm(0,1).ppf(score))
[m, c] = sp.optimize.curve_fit(destinationFunc, std_norm_dis, sorted_sample)[0]
dest_fit = []
for z in std_norm_dis:
    dest_fit.append(destinationFunc(z,m,c));
plt.figure()
plt.plot(std_norm_dis, sorted_sample, color='red', marker='+', markerfacecolor='None') 
plt.plot(std_norm_dis, dest_fit, color='black') 
plt.xlabel('z-statistic mean=30') 
plt.ylabel('Value')
#print (calR2(sorted_sample, dest_fit))
print ss.f.cdf(1.21, 3,16)
##================================================





