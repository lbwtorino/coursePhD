#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:26:10 2018

@author: liubowen
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as ss

#===========================
#ex-1
#sample_num=1000
#x=np.linspace(0,5,sample_num)
#y=5*np.cos((20*np.pi)*x) + 3*np.cos((2*np.pi)*x)
#Maxtime=5.
#timestep=Maxtime/sample_num
#FreqStep =1./( Maxtime )
#print " freq step ", FreqStep
#print "max freq is " , 1./ timestep
#freq =[]
#for i in range(sample_num):
#    freq.append(i*FreqStep)
#w= np.fft.fft(y)
#print w
#(b)
#plt.figure()
#plt.plot(x,y)
#(c)
#plt.figure()
#plt.plot(freq ,w)
#plt.xlim (0 ,60)
#from cmath import exp, pi
#print w
#def DFT_slow(x):
#    """Compute the discrete Fourier Transform of the 1D array x"""
#    x = np.asarray(x, dtype=float)
#    N = x.shape[0]
#    n = np.arange(N)
#    k = n.reshape((N, 1))
#    M = np.exp(-2j * np.pi * k * n / N)
#    return np.dot(M, x)
 
#def FFT(x):
#    """A recursive implementation of the 1D Cooley-Tukey FFT"""
#    x = np.asarray(x, dtype=float)
#    N = x.shape[0]
#    
#    if N % 2 > 0:
#        raise ValueError("size of x must be a power of 2")
#    elif N <= 32:  # this cutoff should be optimized
#        return DFT_slow(x)
#    else:
#        X_even = FFT(x[::2])
#        X_odd = FFT(x[1::2])
#        factor = np.exp(-2j * np.pi * np.arange(N) / N)
#        return np.concatenate([X_even + factor[:N / 2] * X_odd,
#                               X_even + factor[N / 2:] * X_odd])       
#print FFT(y)
#def a(x):
#    size = len(x)
#    w = np.arange(0, size)
#    return [sum(np.exp(-w*i*2.0*np.pi*1j / size) * x) for i in w]
#    
#def nativeFFT(x):
#    size = len(x)
#    samples = np.arange(0, size)
#    res = []
#    for i in samples:
#        res.append(sum(np.exp(-samples * i * 2.0 * np.pi * 1j/size) * y))
#    return res
#ab = (nativeFFT(y))
#plt.plot(freq, ab)
#
#
#import operator

#plt.xlim(0, 20)
#b = a(y)
#print operator.eq(ab,b)
#print operator.eq(ab,w)
##(d)
#mag=[]
#for line in w:
#    mag.append(np.linalg.norm(line))
#plt.figure()
#plt.plot(freq , mag)
#plt.xlabel('Freq (Hz )')
#plt.ylabel('FT Magnitude')
#plt.xlim (0 ,60)
##(e)
#from scipy.fftpack import fft, ifft
#plt.figure()
#plt.plot(x, ifft(w))
#F_spec=np.fft.ifft(w)
#plt.figure()
#plt.plot(x, F_spec)

#def fft(x):
#    N = len(x)
#    if N <= 1: return x
#    even = fft(x[0::2])
#    odd =  fft(x[1::2])
#    T= [np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)]
#    return [even[k] + T[k] for k in range(N//2)] + [even[k] - T[k] for k in range(N//2)]

#===========================
#ex-2
def twoFactor():
    data = [[[100,140],[180,140]],[[230,210],[160,200]],[[310,270],[210,250]]]
    size_data = len(data)
    size_data_row = len(data[0])
    size_data_unit = len(data[0][0])
    DoF1 = size_data-1
    DoF2 = size_data_row-1
    DoF3 = (size_data-1)*(size_data_row-1)
    DoF4 = size_data * size_data_row * (size_data_unit-1)
    
    mean1 = []
    for i in range(size_data):
        mean1.append(np.mean(data[i]))
        
    mean2 = []
    for i in range(size_data_row):
        tmp = []
        for j in range(size_data):
            tmp.append(data[j][i])
        mean2.append(np.mean(tmp))
    
    SSA = size_data_row * size_data_unit * np.var(mean1) * len(mean1)
    SSB = size_data * size_data_unit * np.var(mean2) * len(mean2)
    sse_list = []
    for j in range(size_data_row):
        for i in range(size_data):
            sse_list.append(len(data[i][j])*np.var(data[i][j]))
    SSE = sum(sse_list)
    SST = np.var(data) * size_data * size_data_row * size_data_unit
    SSAB = SST-SSA-SSB-SSE
    
    print 'SSA:',SSA
    print 'SSB:',SSB
    print 'SSE:',SSE
    print 'SST:',SST
    print 'SSAB:',SSAB
    
    MSA = SSA/(size_data-1.0)
    MSB = SSB/(size_data_row-1.0)
    MSAB = SSAB/((size_data-1.0) * (size_data_row-1.0))
    MSE = SSE/(size_data * size_data_row * (size_data_unit-1))
    print 'MSA:',MSA
    print 'MSB:',MSB
    print 'MSE:',MSE
    print 'MSAB',MSAB

    Fa = MSA/MSE
    Fb = MSB/MSE
    Fab = MSAB/MSE
    Fac = ss.f.ppf(0.95, DoF1, DoF4)
    Fbc = ss.f.ppf(0.95, DoF2, DoF4)
    Fabc = ss.f.ppf(0.95, DoF3, DoF4)
    print 'Fa:', Fa
    print 'Fb:', Fb
    print 'Fab:', Fab
    print 'Critical Fa:', Fac
    print 'Critical Fb:', Fbc
    print 'Critical Fab', Fabc
    
#    alpha = [np.mean(data[i])-np.mean(data) for i in range(size_data)]
#    beta = [np.mean([data[i][j] for i in range(size_data)])-np.mean(data) for j in range(size_data_row)]
#    ab = [np.mean(data[i][j])-alpha[i]-beta[j]-np.mean(data) for j in range(size_data_row) for i in range(size_data)]
#    print alpha,beta,ab 

#twoFactor()
#===========================
##ex-3
#Ns= 160 #number of samples
#time = np.linspace(0, 0.4, Ns, endpoint = False)
##print time
##time = np.arange(0, 0.4, 0.0025)
#y=20 + 10*np.cos((2*np.pi)*50*time) + 5*np.cos((2*np.pi)*10*time) + 20*np.cos((2*np.pi)*100*time)
#
#Maxtime = 0.4
#timestep = Maxtime/Ns
#FreqStep =1./( Maxtime )
#freq =[]
#for i in range(Ns):
#    freq.append (i*FreqStep)
#w = np.fft.fft(y)
#print len(freq), len(time), len(w)
#plt.figure()
#plt.plot(time,y)
#plt.xlim (0, 0.1)
#plt.figure()
#plt.plot(freq ,w)
#plt.xlim (0, 400)
#
##3(b)=================================
#def window(freq, spec, f):
#    F_spec=spec
#    F_spec[f]=0
#    return F_spec
#
#filtered0 = window(freq, w, 0)
#plt.figure()
#plt.plot(freq, filtered0)
#plt.xlim (0 ,400)
#
#
#plt.figure()
#plt.plot(time,y, 'r')
#F_spec= np.fft.ifft(filtered0)
##plt.figure()
#plt.plot(time, F_spec, 'g')
#plt.xlim (0, 0.4)

## 3(c)=====================
#Ns= 160 #number of samples
#time = np.linspace(0, 0.4, 160)
#y=20 
#
#Maxtime = 0.4
#timestep = Maxtime/Ns
#FreqStep =1./( Maxtime )
#freq =[]
#for i in range(Ns):
#    freq.append (i*FreqStep)
#w = np.fft.fft(y)
#
#plt.figure()
#plt.plot(freq, w)
#plt.xlim (0 ,400)
#
#plt.figure()
#plt.plot(time,y, 'r')
#F_spec= np.fft.ifft(w)
##plt.figure()
#plt.plot(time, F_spec, 'g')
#t3 = np.arange(0,0.4,0.0025)
#y3 = 20+10*np.cos(2*np.pi*50*t3)+5*np.cos(2*np.pi*10*t3)+20*np.cos(2*np.pi*100*t3)
#    
#Ns= 160 #number of samples
#time = np.linspace(0, 0.4, 160, endpoint = False)
#y=20 + 10*np.cos((2*np.pi)*50*time) + 5*np.cos((2*np.pi)*10*time) + 20*np.cos((2*np.pi)*100*time)
#FreqStep = 1./0.4
#freq = np.arange(0,len(time)*FreqStep,FreqStep)
#f = [sum(np.exp(-time*i*2*np.pi*1j)*y) for i in freq]
#y_removeTime = np.fft.ifft(f * (freq==0))
#plt.figure()
#plt.plot(time, y_removeTime)
#plt.plot(time, y)
#plt.xlim(0,0.1)

#
#
##3(d)=================================
#def window(freq, spec, f0): 
#    indx0 = freq.index(f0)
#    F_spec=spec
#    F_spec[indx0]=0
#    indx0 = freq.index(f0)
#    indx02 = len(freq) - indx0
#    F_spec[indx02] = 0
##    freqstep = freq[1]-freq[0]
##    Deltaindex=Delta_f/freqstep
##    IndexStartDelete0 = indx0 - (Deltaindex/2)
##    IndexEndDelete0=indx0 +(Deltaindex /2)
##    IndexStartDelete02 = indx02 - (Deltaindex/2)
##    IndexEndDelete02=indx02+(Deltaindex/2)
##    F_spec=spec
##    F_spec[indx0]
##    F_spec[int(IndexStartDelete0) : int( IndexEndDelete0 )]=0
##    F_spec[int(IndexStartDelete02) : int( IndexEndDelete02 )]=0
#    return F_spec
#filtered50 = window (freq, w, 50)
##plt.figure()
##plt.plot(freq, filtered50)
##plt.xlim(0,400)
#
#plt.figure()
#plt.plot(time, y, 'b')
#
#F_spec=np.fft.ifft(filtered50)
#plt.plot(time, F_spec, 'r')
#plt.xlim(0,0.4)
#
##3(e)=================================
#def window(freq, spec, f0): 
#    indx0 = freq.index(f0)
#    indx02 = len(freq) - indx0
#    F_spec=spec
#    F_spec[0: int( indx0 )]=0
#    F_spec[indx02+1: len(freq)]=0
#    return F_spec
#
#filtered50 = window (freq, w, 100)
#plt.figure()
#plt.plot(freq, filtered50)
#plt.xlim(0,400)
#
#plt.figure()
#plt.plot(time,y)
#F_spec=np.fft.ifft(filtered50)
##plt.figure()
#plt.plot(time, (F_spec))
#plt.xlim(0,0.1)
Ns= 160 #number of samples
time = np.linspace(0, 0.4, Ns, endpoint = False)
y=20 + 10*np.cos((2*np.pi)*50*time) + 5*np.cos((2*np.pi)*10*time) + 20*np.cos((2*np.pi)*100*time)
Maxtime = 0.4
timestep = Maxtime/Ns
FreqStep =1./( Maxtime )
freq =[]
for i in range(Ns):
    freq.append (i*FreqStep)
w = np.fft.fft(y)
plt.figure()
plt.plot(freq ,w)
plt.xlim (0, 400)
def window(freq, spec, f0): 
    indx0 = freq.index(f0)
    indx02 = len(freq) - indx0
    F_spec=spec
    F_spec[0: int( indx0 )]=0
    F_spec[indx02+1: len(freq)]=0
    return F_spec

filtered50 = window (freq, w, 100)
plt.figure()
plt.plot(time,y)
F_spec=np.fft.ifft(filtered50)
plt.plot(time, (F_spec))