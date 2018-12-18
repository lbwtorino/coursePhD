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

#=============================
#ex-1
def w9cp1(t, n, k):
    out=0
    for kk in range (k, n):
        out += (n-kk) * np.sin(2*np.pi*kk*t)
    return out

Ns=600
t=np.linspace( 0 , 4 , Ns )
Maxtime =4.0
timestep=Maxtime/Ns
FreqStep =1./( Maxtime )
print "max freq is " , 1/ timestep
freq =[]
for i in range(Ns):
    freq.append(i*FreqStep)
ft = w9cp1(t, 20 ,10)

w=np.fft.fft(ft)
plt.figure()
plt.plot(t, ft, lw=1)
mag=[]
for line in w:
    mag.append(np.linalg.norm(line))
plt.figure()
plt.plot(freq , mag)
plt.xlabel('Freq (Hz )')
plt.ylabel('FT Magnitude')
plt.xlim (0 ,50)
#=============================
#ex-2
Ns=1001 #number of samples
x=np.linspace(0 ,2 , Ns )
y=5*np.cos((2*np.pi)*2*x) + np.cos((2*np.pi)*50*x )
Maxtime=2.
timestep=Maxtime/Ns
FreqStep =1./( Maxtime )
print " freq step ", FreqStep
print "max freq is " , 1./ timestep
freq =[]
for i in range(Ns):
    freq.append (i*FreqStep )
w=np.fft.fft( y )
plt.figure()
plt.plot(x , y)
plt.figure()
plt.plot(freq ,w)
plt.xlim (0 ,60)
##============
win =[]
def window(freq, spec, f0 , Delta_f): #Create a w
    indx0 = freq.index(f0)
    indx02 = len(freq) - indx0
    print indx0 , indx02
    freqstep = freq[1]-freq[0]
    print freqstep
    Deltaindex=Delta_f/freqstep
    print "Delta index ", Deltaindex
    IndexStartDelete0 = indx0 - (Deltaindex/2)
    IndexEndDelete0=indx0 +(Deltaindex /2)
    IndexStartDelete02 = indx02 - (Deltaindex/2)
    IndexEndDelete02=indx02+(Deltaindex/2)
    F_spec=spec
    F_spec[int(IndexStartDelete0) : int( IndexEndDelete0 )]=0
    F_spec[int(IndexStartDelete02) : int( IndexEndDelete02 )]=0
    return F_spec

filtered50=window ( freq ,w, 50 ,10)
plt.figure()
plt.plot(x , y)
plt.figure()
plt.plot(freq , filtered50)
plt.xlim (0 ,60)
F_spec=np.fft.ifft(filtered50)
plt.figure()
plt.plot(x, F_spec)