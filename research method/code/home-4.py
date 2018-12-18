#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:50:56 2018

@author: liubowen
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as ss
import math

#==================
#ex-1
#import math
#def time (x, b): 
#    return 1.0/b * math.exp (-x / b)
#
#def likelihood (trials, arrival):
#    problist =[]
#    for line in trials : 
#        prob = 1.
#        for l in arrival :
#            prob = prob * time(l, line)
#        problist.append(prob) 
#    return problist, trials[problist.index(max(problist))]
#
#arrive = [3.2, 2.1, 5.3, 4.2, 1.2, 2.8, 6.4, 1.5, 1.9, 3.0]
#expeTrials = np.linspace(0.0001, 10, 10000)
#likely, b = likelihood(expeTrials, arrive)
#print 'The max likelihood estimate beta is:', b
#plt.figure()
#plt.plot (expeTrials, likely)
#plt.xlabel ('beta lambda')
#plt.ylabel ('Likelihood')
#plt.savefig('likelihood.pdf')

#li = [13.1, 15.0, 14.0, 14.4, 14.0, 11.6]
#limean = np.mean(li)
#tmp=0
#for i in range(len(li)):
#    tmp += ((li[i]-limean)**2)
#print math.sqrt(tmp/5.0), math.sqrt(tmp/6.0)
#print (np.std(li)), np.mean(li)
H5 =[7, 8, 15, 11, 9, 10]
#print np.std(H5), np.mean(H5)
limean = np.mean(H5)
tmp=0
for i in range(len(H5)):
    tmp += ((H5[i]-limean)**2)
#print tmp/5.0, tmp/6.0
#print np.std(H5)**2, np.mean(H5), np.var(H5)
#H10 =[12 ,17 ,13 ,18 ,19 ,15]
#H15 =[14 ,18 ,19 ,17 ,16 ,18]
#H20 =[19 ,25 ,22 ,23 ,18 ,20]
##print np.std(H5), np.mean(H5)
##print np.std(H10), np.mean(H10)
##print np.std(H15), np.mean(H15)
##print np.std(H20), np.mean(H20)
#arr = [1.3, 1.6, 0.5, 2.2, 2.4 ,0.4, 1.8 ,1.7, 0.6, 3.9 ,4.4, 2.0,1.2, 1.1, 2.0 ,1.8, 1.5, 1.3, 4.1 ,3.4]
#res=0
#for i in range(len(arr)):
#    res += (arr[i]-1.96)**2
#
#result = 0
##aa=[13.1, 15.0, 14.0, 14.4, 14.0, 11.6]
#aa=[16.3, 15.7, 17.2, 14.9, 14.4, 17.2]
#aa=[13.9, 13.7, 12.4, 13.8, 14.9, 13.3]
#for i in range(len(aa)):
#    result += (aa[i]-13.66)**2
#print np.mean(aa), np.std(aa), math.sqrt(result/5.0), math.sqrt(result/6.0)
#
#two_res=0
#two = [10,14,18,14, 23,21,16,20, 31,27,21,25]
#print np.mean(two)
#for i in range(len(two)):
#    two_res += (two[i]-20.0)**2
#print math.sqrt(two_res/11.0)

#==================
#ex-2
def Ex2():
    meanMat = np.mat([60, 24, 161])
    print meanMat
    whole = np.mat([[65, 28, 175], [80, 26, 159], [70, 27, 180], [62, 29, 167], [74, 24, 170]]).T 
    C = np.cov(whole)
    sample1 = [65, 80, 70, 62,74]
    m1 = np.mean(sample1)
    sample2 = [28, 26,27,  29,  24]
    m2 = np.mean(sample2)
    sample3 = [175, 159, 180, 167, 170]
    m3 = np.mean(sample3)
    meanSample = np.mat([m1, m2, m3])
    #T 2 = n(X ¯ − µ)T C −1 (X ¯ − µ)
    T_square = 5.0 * (meanSample - meanMat) * np.matrix(C).I *  (np.mat([m1, m2, m3]).T-np.mat([60, 24, 161]).T)
    F = (5.0 - 3.0) / (3.0*(5-1)) * T_square
    Fc = ss.f.ppf(0.99, 3, 5-3)
    print T_square,  F,  Fc
Ex2()
#==================
#ex-3
#H1 =[98,97,99,96]
#H2 =[91,90,93,92]
#H3 =[96,95,97,95]
#H4 =[95,96,99,98]
#
#def SSW (*arg):
#    n= len(arg[0]) 
#    levels = len(arg)
#    ssw = 0
#    for i in range(levels):
#        var =np.var(arg[i], ddof=0)
#        ssw = ssw + var
#    df =(n*levels)-levels
#    return (n* ssw), df
#
#def SSB (*arg):
#    grandmean =0
#    levels = len(arg)
#    for i in range(len(arg)):
#        grandmean = grandmean +np.mean(arg[i])
#    grandmean = grandmean /len(arg)
#    ssb =0
#    for i in range (len(arg)):
#        temp =np.mean(arg[i])
#        ssb = ssb +(temp-grandmean) **2
#    ssb = len(arg[0])*ssb
#    df= levels-1
#    return ssb,df
#
#ssw, sswdf = SSW(H1 , H2 , H3, H4)
#ssb, ssbdf = SSB(H1 , H2 , H3, H4)
#sst1 = np.var(H1 + H2 + H3 + H4)* len(H1+ H2 +H3 + H4 )
#sst2 = ssw + ssb
#msw = ssw / sswdf
#msb = ssb / ssbdf
#F= msb / msw
#Fc=ss.f.ppf(0.95,3,12)
#print " SSW =", ssw
#print " MSW =", msw
#print " SSB =", ssb
#print " MSB =", msb
##print " SSTotal =", sst1
#print " F=", F
#print " Critical F=", Fc
#if F > Fc:
#    print "F>Fc , Reject H0"
#else :
#    print "F<Fc , Accept H0"
##F1, p1 = ss.f_oneway (H1, H2, H3, H4)
##print F1, p1
#    
#print "===================" 
#print "Hotelling␣T-squard" 
#print "===================" 
#import scipy.stats as ss
#x=np.array([[65, 80, 70, 62, 74],[28, 26, 27, 29, 24], [175 ,159 ,180 ,167 ,170]]) # the vector of observarions
#xbar=np.array([np.mean(x[0,:]),np.mean(x[1,:]), np.mean(x[2,:])])
##sample mean vector
#n=x.shape[1] #number of obersvations for each variable 
#k=x.shape[0]
#Cov=np.cov(x) # compute the covariance matrix of the observations
#mu=np.array([60,24,161])
#invCov=np.linalg.inv(Cov)
#Tsqd=n* np.matrix.transpose(np.array(xbar)-np.array(mu)) .dot(
#invCov) .dot(np.array(xbar)-np.array(mu))
#F=(n-k)*Tsqd/(k*(n-1))
#Fc=ss.f.ppf(0.99, k,(n-k)) # One right hand tail testsignifficance is 0.05, and 95% confidence
#print "T-squared=", Tsqd
#print "F-value", F
#print "Critical␣F=", Fc # One right hand tail test signifficance is 0.05, and 95% confidence
#if F>Fc:
#    print "F>Fc,␣Reject␣H0"
#else:
#    print "F<Fc,␣Accept␣H0"




