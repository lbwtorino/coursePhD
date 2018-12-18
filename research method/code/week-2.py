#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 14:06:24 2017

@author: robert_simpson
"""
import matplotlib.pyplot as plt
import numpy as np
import csv
import scipy.stats as ss

print ss.norm(0,1).pdf(10) 


###########################################################
#############       Preamble                  #############
###########################################################
#person = raw_input('What is your name?: ')
#age=raw_input('What is your age?: ')
#print 'Hello', rayperson,', you look much younger than', age,'years old!'

#
############################################################
##############       Quick Practice           #############
############################################################
#def f2c(F):
#    return (F-32)*5.0/9
#
#def position_velocity(v0, t):
#    g=9.81
#    yt=v0*t - ((g*(t**2.0))/2.0)
#    dydt=v0-(g*t)
#    return yt, dydt
#
#def savings(APR, monthlydeposit, month):
#    monthlyrate=(APR/100.0)/12.0
#    balance=0.0
#    factor=(1.0+monthlyrate)
#    #print factor
#    for i in range(month):
#        balance=(balance+monthlydeposit)*factor
#    return balance
##
###########################################################
############       Case Problem 2.5            #############
############################################################
#
def mean(mylist): # Compute the mean of values in a numerical list
    num_data = len(mylist)
    mysum = 0.0
    for line in mylist:
        mysum=mysum+line
    return mysum/num_data
#
#
def PopVar(mean, mylist):# Compute the pop variance of a numerical list
    num_data = len(mylist)
    myvar=0.0
    for line in mylist:
        myvar = myvar+((line-mean)**2)
    return myvar/num_data
#
def SampleVar(mean, mylist): # Compute the sample variance of a numerical list
    num_data = len(mylist)
    myvar = 0.0
    for line in mylist:
        myvar=myvar+((line-mean)**2)
    return myvar/(num_data-1)

#
#
############################################################
##############       Case Problem 2.6            #############
############################################################
#
#
with open('../HeightsandWeight.txt','r') as f:
    reader = csv.reader(f, delimiter='\t')
    mylist=list(reader)

weight=[]
for line in mylist[1:]: ##[1:] means start at line 1 rather than line 0
    weight.append(float(line[4]))

avgWeight=mean(weight)
varWeight=PopVar(avgWeight, weight)
stddevWeight=varWeight**0.5
print "The average weight:", avgWeight
print "The variance in Weight is:", varWeight
print "The standard devication in Weight is:", stddevWeight
plt.hist(weight, density=True, bins='auto')
#plt.hist(weight, normed=True, bins=28)
plt.xlabel('Weight, Lbs')
plt.ylabel('Probability')


#############################################################
###############       Case Problem 2.7            #############
###############       Binomial Distr            #############
############################################################

def factorial(x):  
    int_x= int(round(x))
    fact=1
    for i in range(int_x+1)[1:]:
        fact=fact*i
    return fact
#
def binomial(p,n,k):
    #print factorial(n)
    bino=(factorial(n)/(factorial(k)*factorial(n-k))) *(p**k) * ((1-p)**(n-k))
    return bino
#
### In Sept the mean number of rainy days is 14. The maximum number of rainy days is 30.
### The probability of rain in any given day is 14/30 if we assume the probability doesn't change with date
### Although the maximum number of rainy days is 30, it is also possible that there will be no rainy days. Therefore we need to make a list with 31 lines for all possible outcomes.
pdf=[]
for raindays in range(31):
    P_rain=binomial(14.0/30,30.0, raindays)
    pdf.append(P_rain)
cdf=[]
def rainCDF(mylist):
    mysum=0
    for line in mylist:
        mysum=line+mysum
        cdf.append(mysum)
    return cdf

plt.figure()
plt.plot(pdf)
plt.xlabel('Rainy Days')
plt.ylabel('PDF')

cdf=rainCDF(pdf)
plt.figure()
plt.plot(cdf)
plt.xlabel('Rainy Days')
plt.ylabel('CDF')

# less than 12 dry days means more than 18 rainy days
# the CDF shows the the probablity of at least X rain days
# We need the opposite, which means we calculate the 1-CDF for 18 days.
# CDF(18 days)=0.95. Therefore probability of 0.05 for more than 12 dry days
#
###############################################################
###############       Case Problem 2.8            #############
##############       Binomial Distributions      #############
###############################################################
#
#CP2.8(a)
def fact(x):
    factorialx=1
    for y in range(1,(x+1)):
        #print y
        factorialx=factorialx*y
    return factorialx

##CP2.8(b)
def binomialf(n,x):
    return fact(n)/(fact(x)*fact(n-x))

##CP2.8(c)
def x_coins(n,x,p):
    #calculates the probability for X coint tosses, p is the probability, p=0.5 for normal coin
    q=1.0-p  #Probability of tails (not heads) FLOAT
    return (binomialf(n,x)*p**(x)*q**(n-x))
    
my_x=np.linspace(0,5,6) #gnerate a list of x from 0 to 5 (beware this creates floats)
pdf=[]
for x in my_x:
    pdf.append(x_coins(5,int(x),0.5))
#plt.plot(my_x,pdf, marker="x")
plt.bar(my_x,pdf)
plt.xlabel("x, number of heads")
plt.ylabel("Probability")

##CP2.8(d)
my_x=np.linspace(0,50,51) #gnerate a list of x from 0 to 5 (beware this creates floats)
pdf=[]
for x in my_x:
    pdf.append(x_coins(50,int(x),0.5))
#plt.plot(my_x,pdf, marker="x")
plt.bar(my_x,pdf)

plt.xlabel("x, number of heads")
plt.ylabel("Probability")


