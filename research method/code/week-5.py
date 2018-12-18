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

#===========================================
def boat(vel,ang,rad):
    return (ang*np.pi/180)*rad/vel;
def centdiff(vel,ang,rad,Evel,Eang,Erad, h): # calculate POE using a Talylor Approximation
    RE_v=h*vel
    RE_a=h*ang
    RE_r=h*rad #relative error 
    dtdv=(boat(vel+RE_v,ang,rad)-boat(vel-RE_v,ang,rad))/(2*RE_v) 
    dtda=(boat(vel,ang+RE_a,rad)-boat(vel,ang-RE_a,rad))/(2*RE_a) 
    dtdr=(boat(vel,ang,rad+RE_r)-boat(vel,ang,rad-RE_r))/(2*RE_r)
    SqErr=pow(Evel*dtdv ,2) + pow(Eang*dtda ,2) + pow(Erad*dtdr ,2) 
    return np.sqrt(SqErr)

def main(): 
    vel =0.6
    ang =30 
    rad =10 
    Evel =0.1 
    Eang =5 
    Erad =0.1
    h=np.logspace(-6,-1,num=60) 
    poe =[]
    for dh in h:
        poe.append(centdiff(vel,ang,rad,Evel,Eang,Erad , dh))
    print poe
    plt.figure()
    plt.plot(h,poe, marker='o') 
    plt.xlabel('h') 
    plt.ylabel('Error (s)') 

main()
    

##=====================================================

def coalt(Q,r,P0):
    return (np.log((Q*r/P0)+1))/r
def centdiffCP2(Q,r,P0,EQ,Er,h): #calculate POE using a Talylor Approximation
    RE_Q=h*Q 
    RE_r=h*r
    dtdQ=(coalt(Q+RE_Q,r,P0)-coalt(Q-RE_Q,r,P0))/(2* RE_Q)
    dtdr=(coalt(Q,r+RE_r,P0)-coalt(Q,r-RE_r,P0))/(2* RE_r)
    SqErr=pow(EQ*dtdQ ,2) + pow(Er*dtdr ,2) 
    return np.sqrt(SqErr)

def main2(): 
    Q=1000
    r=0.027
    P0 =5
    EQ =100
    Er =0.002 
    h=np.logspace(-6,-1,num=60) 
    poe =[]
    for dh in h:
        poe.append(centdiffCP2(Q,r,P0,EQ,Er,dh))
    print poe
    plt.figure()
    plt.plot(h,poe, marker='o') 
    plt.xlabel('h') 
    plt.ylabel('Error (Years)') 
    
main2()

#======================================================
print ss.t.ppf(0.975, 11)