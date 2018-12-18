#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:52:55 2018

@author: liubowen
"""

import serial, io
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
import pandas as pd
import read as rd

measuretime=5 #time in seconds to collect data


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a



def butter_bandpass(start,stop, fs, order=5):
    nyq = 0.5 * fs
    startstop = [float(start) / nyq, float(stop)/nyq]
    b, a = butter(order, startstop, btype='band', analog=False)
    return b, a


fname = '/Users/liubowen/sutd/course/research method/project/peace/data1543396502.17.csv'
fmode = 'w+'
t0=float(time.time())


times=[]
volts=[]
times, volts = rd.convert(fname)


t=np.linspace(times[0], times[len(times)-1], len(times)) #creates regular time grid in secs
v=np.interp(t,times,volts)  #puts data onto reg time grid
plt.figure()
plt.plot(times,volts)

#tim=np.linspace(0,(times[len(times)-1]-times[0])/1000,len(times)) 
tim=np.linspace(0,(t[len(times)-1]-t[0])/1000,len(t)) 

plt.figure()
plt.title("interpolated")
plt.plot(tim,v)

fs =1.0/tim[1]
n=len(t)


freqspec=np.fft.fft(v)
Hz=np.linspace(0,fs,n)
plt.figure()
plt.plot(Hz, np.abs(freqspec))


betaorder=5 #order of the filter
bbeta, abeta = butter_bandpass(16,31, fs, betaorder)
thetaorder=2
btheta, atheta = butter_bandpass(4,7, fs, thetaorder)

wbeta, hbeta = freqz(bbeta, abeta)
wtheta, htheta = freqz(btheta, atheta)

plt.figure()
plt.title('Band Pass Filter Responses')
plt.plot(fs*wbeta/(2*np.pi), np.abs(hbeta), 'b')
plt.plot(fs*wtheta/(2*np.pi), np.abs(htheta), 'r')
plt.xlim(0,100)


beta=lfilter(bbeta,abeta,v)
theta=lfilter(btheta,atheta,v)
fig=plt.figure()
plt.title('Theta Signal after 3-7 Hz band pass filter')
ax = fig.add_subplot(111)
ax.plot(tim, (theta))

fig=plt.figure()
plt.title('Theta Signal after 16-31 Hz band pass filter')
ax = fig.add_subplot(111)
ax.plot(tim, (beta))
