#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:50:23 2018

@author: liubowen
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as ss

#==========================
#ex-8.1
#import numpy as np
#import scipy . stats as ss
#import matplotlib . pyplot as plt
#from scipy.stats import f
#
#t=np.linspace ( -5 ,5 ,51)
#plt.figure ()
#for dof in [1, 3, 5, 10, 20]:
#    tPDF =ss.t.pdf(t, dof)
#    plt.plot(t, tPDF )  
#plt.xlabel ('t')
#plt.ylabel ('PDF')
#plt.figure ()
#for dof in [1, 3, 5, 10, 20]:
#    tCDF =ss.t. cdf(t, dof)
#    plt.plot (t, tCDF )
#plt.xlabel ('t')
#plt.ylabel ('CDF')
#==========================
#ex-8.2
H5 =[7 ,8 ,15 ,11 ,9 ,10]
H10 =[12 ,17 ,13 ,18 ,19 ,15]
H15 =[14 ,18 ,19 ,17 ,16 ,18]
H20 =[19 ,25 ,22 ,23 ,18 ,20]
def SSW (* arg ):
    n= len (arg[0]) #n is the number of samples in each level
    levels = len(arg)
    ssw =0
    for i in range (levels):
        var =np.var(arg[i], ddof =0)
        ssw = ssw + var
    df =(n* levels )-levels
    return (n* ssw ), df

def SSB (* arg ):
    grandmean =0
    levels = len ( arg )
    for i in range ( len (arg)):
        grandmean = grandmean +np. mean ( arg [i])
    grandmean = grandmean /len( arg)
    ssb =0
    for i in range ( len (arg)):
        temp =np. mean (arg [i])
        ssb = ssb +( temp - grandmean ) **2
    ssb = len (arg [0]) *ssb
    df= levels -1
    return ssb , df

ssw , sswdf = SSW (H5 , H10 , H15 , H20)
ssb , ssbdf = SSB (H5 , H10 , H15 , H20)
sst1 =np.var(H5+ H10 + H15 + H20 )* len (H5+ H10 + H15 + H20 )
sst2 = ssw + ssb
msw = ssw / sswdf
msb = ssb / ssbdf
F= msb / msw
Fc=ss.f.ppf (0.95,3 ,20) # use 0.95 because we are looking at the area of the RH tail
print " SSW =",ssw
print " MSW =", msw
print " SSB =", ssb
print " MSB =", msb
print " SSTotal =", sst1
print "F=", F
print " Critical F=", Fc
if F>Fc:
    print "F>Fc , Reject H0"
else :
    print "F<Fc , Accept H0"
# ### Using Python ’s built in function :
F1 , p1 = ss. f_oneway (H5 , H10 , H15 , H20 )

#====================================================
#ex-8.3
#x1 =[157.381 , 241.0 , 31.433 , 18.500 , 20.81]
#x2 =[158.429 , 241.571 , 31.479 , 18.446 , 20.839]
#c1 =[[11.048 , 9.100 , 1.557 , 0.870 , 1.286] ,[9.100 , 17.500 , 1.910 , 1.310 ,
#0.880] ,[1.557 , 1.910 , 0.531 , 0.189 , 0.240] ,[0.870 , 1.310 , 0.189 , 0.176 ,
#0.133] ,[1.286 , 0.880 , 0.240 , 0.133 , 0.575]]
#c2 =[[15.069 , 17.19 , 2.243 , 1.746 , 2.931] ,[17.19 , 32.550 , 3.398 , 2.950 ,
#4.066] ,[2.243 , 3.398 , 0.728 , 0.470 , 0.559] ,[1.746 , 2.950 , 0.470 , 0.434 ,
#0.506] ,[2.931 , 4.066 , 0.559 , 0.506 , 1.321]]
#
#n1 =21
#n2 =28
#dof1 =n1 -1
#dof2 =n2 -1
## pairwise Tukey
#print " =================== "
#print " Pairwise Tukey "
#print " =================== "
#tc=ss.t.ppf(0.025, dof1 + dof2 ) # signifficance level of 0.05 is 0.025 for 2 tails
#print " The critical t-value is", tc
#for i, line1 in enumerate (x1):
#    var1 =c1[i][i]
#    var2 =c2[i][i]
#    # print " variance 1=" , var1 , " variance 2=" , var2
#    s2 =(( dof1 * var1 )+( dof2 * var2 ))/( dof1 + dof2 )
#    t=( x1[i]-x2[i])/ pow (( s2 *((1./ dof1 ) +(1./ dof2 ))) ,0.5)
#    if abs (t)>abs(tc):
#        print " Reject H0\n", x1[i], var1 , x2[i], var2 , s2 , "t=", t
#    if abs (t)<abs(tc):
#        print " Accept H0\n", x1[i], var1 , x2[i], var2 , s2 ,"t=", t
#
## Hotelling T^2
#print " =================== "
#print " Hotelling T- squard "
#print " =================== "
#Cov = (dof1 *np.array(c1) + dof2 *np.array(c2))/( dof1 + dof2 )
##print Cov
#invCov = np.linalg.inv( Cov )
##print invCov
#x1minx2 = np.matrix.transpose(np.array (x1)-np. array (x2))
#Tsqd = ((n1*n2 * x1minx2.dot(invCov)).dot(np.array(x1)-np.array (x2)))/( n1+n2)
#F = (n1+n2-5-1)* Tsqd / ((dof1+dof2 ) *5)
#Fc=ss.f.ppf (0.95, 5, 43) # One right hand tail test signifficance is 0.05 , and 95% confidence
#print "T- squared =", Tsqd
#print "F- value ", F
#print " Critical F=", Fc # One right hand tail test signifficance is 0.05 , and 95% confidence
#if F>Fc:
#    print "F>Fc , Reject H0"
#else :
#    print "F<Fc , Accept H0"



