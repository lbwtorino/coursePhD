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

global kb
kb = 8.6173303e-5
def kis(t,p):
    x = []
    y = []
    for i in range(len(t)):
        y.append(math.log(p[i]/t[i]**2))
        x.append(-1/(t[i]*kb))
    return np.array(x),np.array(y)


def t_g(x,y):
    g_i = (y[1]-y[0])/(x[1]-x[0])
    g_min = min(g_i/100,g_i*100)
    g_max = max(g_i/100,g_i*100)
    g_l = []
    c_l = []
    vg = []
    vc = []
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


###################################################
    
#def t_g(x,y):
#    g_i = (y[1]-y[0])/(x[1]-x[0])
#    if g_i>0:
#        g_min = g_i/100
#        g_max = g_i*100
#    else:
#        g_min = g_i*100
#        g_max = g_i/100
#    g_l = []
#    c_l = []
#    v = []
#    for i in range(50):
#        g = (g_min+g_max)/2
#        c = y.mean()-g*x.mean()
#        v0 = (y - x*g).var()
#        v.append(v0)
#        c_l.append(c)
#        g_l.append(g)
#        v1 = (y-(g+0.01*abs(g_max-g))*x).var()
#        v2 = (y-(g-0.01*abs(g-g_min))*x).var()
#        if v1>v2:
#            g_max = g
#        else:
#            g_min = g
#    return g_l,c_l,v

################################################

def ActE(T,phi,c):
    return (c-math.log(phi/T**2))*T*kb

def MCAE8(c,N=10000):
    AE = []
    t = [440.6, 440.3, 439.7, 438.2, 437.3, 434.4, 431.7, 429.7]
    p = [4.5, 3.4, 3.2, 2.7, 2.1, 1.0, 0.8, 0.5]
    for i in range(N):
        k = random.randint(1,8)
        T1 = ss.norm.rvs(t[k],0.2)
        p1 = ss.norm.rvs(p[k],0.1)
        AE.append(ActE(T1,p1,c))
    return AE

def MCAE(T,phi,c,N=10000):
    AE = []
    for i in range(N):
        T1 = ss.norm.rvs(T,0.2)
        p1 = ss.norm.rvs(phi,0.1)
        AE.append(ActE(T1,p1,c))
    return AE

t = [440.6, 440.3, 439.7, 438.2, 437.3, 434.4, 431.7, 429.7]
p = [4.5, 3.4, 3.2, 2.7, 2.1, 1.0, 0.8, 0.5]

x,y = kis(t,p)
g,c,vg,vc = t_g(x,y)
ax = range(len(g))
c0 = c[-1]  #y.mean()-g[-1]*x.mean()
Tc = 1/(x.mean()*kb)
Pc = math.exp(y.mean())*Tc**2
Ea = np.array(MCAE(Tc,Pc,c0))
plt.hist(Ea,bins='auto')


p = np.logspace(-6,-1,50)
dE = []
for h in p:
    dE2 = 0.2**2*((ActE(Tc+Tc*h,Pc,c0)-ActE(Tc-Tc*h,Pc,c0))/(2*h*Tc))**2+0.1**2*((ActE(Tc,Pc+Pc*h,c0)-ActE(Tc,Pc-Pc*h,c0))/(2*h*Tc))**2
    dE.append(dE2**0.5)
#plt.plot(p,dE)
#plt.yscale('log')
#plt.xscale('log')


#plt.plot(ax,g)
#plt.plot(ax,v)