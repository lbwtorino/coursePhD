#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:28:02 2018

@author: liubowen
"""
import serial, io
import time
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz
import pandas as pd
import math

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

#parse native data
def read(filename):
    times = []
    volt = []
    f = open(filename)             
    line = f.readline()             
    while line:
        times.append(int(line.strip('\r\n').split(',')[0]))
        volt.append(int(line.strip('\r\n').split(',')[1]))
        line = f.readline()
    
    f.close()
    return times, volt

#
def convert(filename):
    data = pd.read_csv(filename, names=['times', 'volts'])
    dataframe = data.sort_values(by=['times'])
    return (dataframe['times'][5:len(dataframe)-5]).tolist(), (dataframe['volts'][5:len(dataframe)-5]).tolist()


def getFreq(times, volt):
    
    t = np.linspace(times[0], times[len(times)-1], len(times)) 
    print t, len(times), len(t)
    v = np.interp(t,times,volt)  
    
    tim = np.linspace(0,(t[len(times)-1]-t[0])/1000,len(t)) 
    print len(tim)
    
    fs = 1.0/tim[1]
    n=len(t)
    
    freqspec = np.fft.fft(v)
    Hz = np.linspace(0,fs,n)
    return Hz, freqspec

def plotFig(times, volts):
    t=np.linspace(times[0],times[len(times)-1],len(times))
    v=np.interp(t,times,volts)
    plt.figure()
    plt.plot(times,volts)
    
    tim=np.linspace(0,(t[len(times)-1]-t[0])/1000,len(t)) 
    
    plt.figure()
    plt.title("interpolated")
    plt.plot(tim, v)
    
    fs =1.0/tim[1]
    n=len(t)
    
    freqspec=np.fft.fft(v)
    Hz=np.linspace(0,fs,n)
    plt.figure()
    plt.plot(Hz[1:len(Hz)/2], np.abs(freqspec)[1:len(Hz)/2])
    
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
    
def getMeanAndVar(times, volts):
    t=np.linspace(times[0], times[len(times)-1], len(times)) 
    v=np.interp(t,times,volts)  
    tim=np.linspace(0, (t[len(times)-1]-t[0])/1000, len(t)) 
    
    fs =1.0/tim[1]
    n=len(t)
    freqspec = np.fft.fft(v)
    Hz = np.linspace(0,fs,n)
    index = []
    for i in range(len(Hz)):
#        if Hz[i] >=0.5 and Hz[i] <=4.0:
#        if Hz[i] >=4.0 and Hz[i] <=8.0:
        if Hz[i] >=8.0 and Hz[i] <=13.0:
#        if Hz[i] >=13.0 and Hz[i] <=30.0:
#        if Hz[i] >=30.0 and Hz[i] <=45.0:
            index.append(i)
    freqres = (freqspec[index[0]:index[len(index)-1]])
    return int(np.abs(np.mean(freqres))), int(np.std(freqres))
            
def file_name(file_dir): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for f in files:
            if os.path.splitext(f)[1] == '.csv':
                L.append(os.path.join(root, f))
    return L 

dir_path = 'data/movie/horrible/'
res_path = 'data/game/res/rock/'
hzrange = ['0.5-4','4-8','8-13','13-30','30-45']
files = file_name(dir_path) 

means=[]
vari=[]
for i in range(len(files)):
    times, volts = convert(files[i])
    mean, var = getMeanAndVar(times, volts)
    means.append(mean)
    vari.append(var)
print means, vari    
res = []
for j in range(len(means)):
    temp = []
    temp.append(means[j])
    temp.append(vari[j])
    res.append(temp)
   
name=['mean','std']
test=pd.DataFrame(columns=name, data=res)
test.to_csv(res_path+hzrange[1]+'res.csv', encoding='gbk')


