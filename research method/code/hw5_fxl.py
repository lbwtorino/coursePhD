# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 09:25:04 2018

@author: T_T
"""

import serial, io
import csv
import os
import time
import pandas as pd
import numpy as np
import scipy.stats as ss
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz


def pro2():
    a = [[[100,140],[180,140]],[[230,210],[160,200]],[[310,270],[210,250]]]
    
    am = [np.mean(a[i]) for i in range(len(a))]
    bm = [np.mean([a[j][i] for j in range(len(a))]) for i in range(len(a[0]))]
    
    SSA = len(a[0])*len(a[0][0])*np.var(am)*len(am)
    SSB = len(a)*len(a[0][0])*np.var(bm)*len(bm)
    SSE = sum([len(a[i][j])*np.var(a[i][j]) for i in range(len(a)) for j in range(len(a[0]))])
    SST = np.var(a)*len(a)*len(a[0])*len(a[0][0])
    SSAB = SST-SSA-SSB-SSE
    
    print SSA,SSB,SSE,SST,SSAB
    
    MSA = SSA/(len(a)-1.)
    MSB = SSB/(len(a[0])-1.)
    MSAB = SSAB/((len(a)-1.)*(len(a[0])-1.))
    MSE = SSE/(len(a)*len(a[0])*(len(a[0][0])-1))
    print MSA,MSB,MSE,MSAB

    Fa = MSA/MSE
    Fb = MSB/MSE
    Fab = MSAB/MSE
    Fac = ss.f.ppf(0.95,len(a)-1,len(a)*len(a[0])*(len(a[0][0])-1))
    Fbc = ss.f.ppf(0.95,len(a[0])-1,len(a)*len(a[0])*(len(a[0][0])-1))
    Fabc = ss.f.ppf(0.95,(len(a)-1)*(len(a[0])-1),len(a)*len(a[0])*(len(a[0][0])-1))
    print Fa,Fb,Fab
    print Fac,Fbc,Fabc
    
    alpha = [np.mean(a[i])-np.mean(a) for i in range(len(a))]
    beta = [np.mean([a[i][j] for i in range(len(a))])-np.mean(a) for j in range(len(a[0]))]
    ab = [np.mean(a[i][j])-alpha[i]-beta[j]-np.mean(a) for j in range(len(a[0])) for i in range(len(a))]
    print alpha,beta,ab


def pro3():
    t3 = np.arange(0,0.4,0.0025)
    print t3
    y3 = 20+10*np.cos(2*np.pi*50*t3)+5*np.cos(2*np.pi*10*t3)+20*np.cos(2*np.pi*100*t3)
    
    FreqStep3 = 1./0.4
    freq3 = np.arange(0,len(t3)*FreqStep3,FreqStep3)
    f3 = [sum(np.exp(-t3*i*2*np.pi*1j)*y3) for i in freq3]
    w3 = np.fft.fft(y3)
#    p3 = pro1fft(y3)
    plt.figure()
#    plt.plot(freq3,f3,'r')
    plt.plot(freq3, w3,'g')
#    plt.plot(freq3,p3,'b')
#    print len(f3),len(freq3)
    
    
    yi = np.fft.ifft(f3*(freq3<len(freq3)/2))
    yb = np.fft.ifft(f3*(freq3>0))
    yc = np.fft.ifft(f3*(freq3==0))
    yd = np.fft.ifft(f3*(freq3<50)+f3*(freq3>50))
    ye = np.fft.ifft(f3*(freq3==100))
    plt.figure()
    ye2 = np.fft.ifft(f3-f3*(freq3<100))
    plt.figure()
    plt.plot(t3,yi,'y')
    plt.plot(t3,y3,'r')
    plt.xlim(0,0.1)
    
    plt.figure()
    plt.plot(t3,yb,'g')
    plt.plot(t3,y3,'r')
    plt.xlim(0,0.1)
    
    plt.figure()
    plt.plot(t3,yc,'b')
    plt.plot(t3,y3,'r')
    plt.xlim(0,0.1)
    
    plt.figure()
    plt.plot(t3,yd,'c')
    plt.plot(t3,y3,'r')
    plt.xlim(0,0.1)
    
    plt.figure()
    plt.plot(t3,ye,'k')
#    plt.plot(t3,ye2,'g')
    plt.plot(t3,y3,'r')
    
    plt.xlim(0,0.1)
    
    plt.figure()
    F_spec=np.fft.ifft(w3)
    plt.plot(t3, F_spec, 'r')


def pro1fft(y):
    w = np.arange(0,len(y))
    return [sum(np.exp(-w*i*2.*np.pi*1j/len(y))*y) for i in w]


def pro1():
    t = np.arange(0, 5, 1/200.0)
    y = 5*np.cos(2*np.pi*10*t)+3*np.cos(2*np.pi*t)
    
#    figsize = 18,18
    plt.figure()
    plt.plot(t,y)
    
    FreqStep = 1./5
    freq = np.arange(0,len(t)*FreqStep, FreqStep)
    f0 = pro1fft(y)  # [sum(np.exp(-w*i*2.*np.pi*1j/len(y))*y) for i in w]
    
#    figsize = 18,18
    plt.figure()
    plt.plot(freq,np.abs(f0))
#    figsize = 18,18
    plt.figure()
    w = np.fft.fft(y)
    plt.plot(freq,w)
    

#    
#    fig = plt.figure(figsize = figsize)
#    fig.suptitle("FFT",fontsize=30)
#    
#    plt.plot(freq,[np.linalg.norm(i) for i in w])
    #plt.xlim(0,20)

#pro1()
pro3()
#pro2()




