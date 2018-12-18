# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:15:05 2018

@author: T_T
"""

import numpy as np
import math
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

#global kb
#kb = 8.6173303e-5
def kis(t,p): # prepare data for linear fit
    x = []
    y = []
    kb = 8.6173303e-5
    for i in range(len(t)):
        y.append(math.log(p[i]/t[i]**2))
        x.append(-1/(t[i]*kb))
    return np.array(x),np.array(y)


def t_g(x,y): # linear fit
    # Initialization
    g_i = (y[1]-y[0])/(x[1]-x[0])
    g_min = min(g_i/100, g_i*100)
    g_max = max(g_i/100, g_i*100)
    g_l = []
    c_l = []
    vg = []
    vc = []
    
    # Linear fit
    for i in range(50):
        g = (g_min+g_max)/2
        v0 = (y - x*g).var()
        vg.append(v0)
        g_l.append(g)
        v1 = (y-(g+0.01*abs(g_max-g))*x).var()
        v2 = (y-(g-0.01*abs(g-g_min))*x).var()
        if v1>v2:
            g_max = g
        else:
            g_min = g
    c = y.mean()-g*x.mean()
    c_min = min(c*100,c/100)
    c_max = max(c*100,c/100)
    for i in range(50):
        c = (c_max+c_min)/2
        v0 = ((y - (x*g+c))**2).sum()
        c_l.append(c)
        vc.append(v0)
        v1 = ((y - (x*g+(c+0.01*abs(c_max-c))))**2).sum()
        v2 = ((y - (x*g+(c-0.01*abs(c-c_min))))**2).sum()
        if v1>v2:
            c_max = c
        else:
            c_min = c
    return g_l,c_l,vg,vc

################################################

def ActE(T,phi,c):
    kb = 8.6173303e-5
    return (c-math.log(phi/T**2))*T*kb

def MCEa(T,phi,c,N=10000):  # Monte Carlo simulations
    Ea = []
    for i in range(N):
        T1 = ss.norm.rvs(T,0.2)
        p1 = ss.norm.rvs(phi,0.1)
        Ea.append(ActE(T1,p1,c))
    return np.array(Ea)

def ConfInt(Em,Estd,a): # Confidence Interval with standard norm distribution fit
    Emin = Em + Estd*ss.norm.ppf((1-a)/2) 
    Emax = Em + Estd*ss.norm.ppf((1+a)/2)
    return Emin,Emax

# data from experiment
t = [440.6, 440.3, 439.7, 438.2, 437.3, 434.4, 431.7, 429.7]
p = [4.5, 3.4, 3.2, 2.7, 2.1, 1.0, 0.8, 0.5]
kb = 8.6173303e-5

x,y = kis(t,p) # data preparation
g,c,vg,vc = t_g(x,y) # data from the fit process
c0 = c[-1]  # Constant from fit
print x, y
Tc = -1/(x.mean()*kb)
print Tc
#print t.mean() # reference temperature data for Monte Carlo simulations
Pc = math.exp(y.mean())*Tc**2 
print Pc
#print p.mean() # reference phi data for Monte Carlo simulations
Ea = MCEa(Tc,Pc,c0)  # Ea by Monte Carlo Simulations
plt.hist(Ea,bins=50)  # plot histgram of Ea

Eas = []
for i in range(len(t)):
    Eas.append(ActE(t[i],p[i],c0))
    
print(np.mean(Eas),np.var(Eas),np.std(Eas),np.std(Eas)/math.sqrt(len(Eas)))
print(Ea.mean(),Ea.var(),Ea.std(),Ea.std()/math.sqrt(len(Ea)))
print(ConfInt(Ea.mean(),Ea.std(),0.95))

