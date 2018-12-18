#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:43:16 2018

@author: liubowen
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as ss

#===========================================
#ex-6.6
print ss.t.ppf(q=0.05 , df =9)
lum =[2661. , 2624. , 2641. , 2670. , 2650. , 2638. , 2645. ,
2652. , 2628. , 2675.]
print ss.ttest_1samp(lum , 2650)

#===========================================
#ex-6.7
print ss.t.ppf(q=0.025, df=9)
staked = [19., 19.4, 16.9, 16.4, 18., 16.4, 17., 18.2, 18.6, 19.]
notstaked = [19.4, 19.2, 17.3, 16.9, 18.3, 16.6, 16.9, 18.5, 18.5, 19.4]
notstaked1 = [19.4, 19.2, 17.3, 16.9, 18.3, 16.6, 16.9, 18.5, 18.5, 19.]
print ss.ttest_rel(staked, notstaked)

#===========================================
#ex-6.8
def computemean (count , number ): # computes the mean number of defects
    mysum =0
    for idx , line in enumerate ( count ):
        mysum = mysum +( count [ idx ]* number [ idx ])
        total =sum ( Freq )
    return float ( mysum )/ total
Defects =[0 , 1, 2, 3]
Freq =[242 , 94, 38, 6] # combined the last two categories to make more than 5 occurrences
TotalCount =sum( Freq )
Exp =ss.poisson.pmf( Defects ,0.5) * TotalCount # expected / modelled value
plt.plot ( Defects, Exp )
plt.plot ( Defects , Freq )
print " The chi ^2 statistic is", ss. chisquare (Freq ,Exp) [0]
print " The chi ^2 P value is", ss. chisquare (Freq , Exp ) [1]

#===========================================
#ex-6.9
def lifetime (lam , mean ): # the exponensial
    return lam*np.exp (- lam * mean )
def likelihood (trials , data ):
    meanlife =np.mean ( data )
    print meanlife
    mydist =[]
    for line in trials : # loop over the different trial lambdas
        prob = 1.
        for l in data : # Sub - loop tp compute the likelihood for the lifetime sample
            prob = prob * lifetime (line , l)
        mydist.append(prob) # make a list of the likelihood for each trial lambda
    return mydist

life =[2100 , 2412 , 2738 , 2107, 2435 , 2985 , 2128 , 2438 , 2996 , 2138 , 2456 , 3369 ,
2167 , 2596 , 2374 , 2692]
lamtrials =np.linspace (0, 1e-3, 1001) # create a list of lambda to try.
likely = likelihood (lamtrials, life)
plt.figure ()
plt.plot (lamtrials, likely)
plt.xlabel ('lambda')
plt.ylabel ('Likelihood')
#plt.savefig (’w6cp4 . pdf ’)