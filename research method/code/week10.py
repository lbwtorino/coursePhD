#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:17:42 2018

@author: liubowen
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as ss
import csv
#=============================
#ex-1
#import numpy as np
#from scipy . signal import butter , lfilter , freqz
#import matplotlib . pyplot as plt
#### Define Low Pass Filter
#def butter_lowpass (cutoff , fs , order =5) :
#    nyq = 0.5 * fs
#    normal_cutoff = cutoff / nyq
#    b, a = butter (order , normal_cutoff , btype ='low', analog = False )
#    return b, a
#### Define Low Pass Filter
#def butter_highpass ( cutoff , fs , order =5) :
#    nyq = 0.5 * fs
#    normal_cutoff = cutoff / nyq
#    b, a = butter (order , normal_cutoff , btype ='high', analog = False )
#    return b, a
#### Define Band Pass Filter
#def butter_bandpass (start ,stop , fs , order =5) :
#    nyq = 0.5 * fs
#    startstop = [ float ( start ) / nyq , float ( stop )/ nyq]
#    b, a = butter (order , startstop , btype ='band', analog = False )
#    return b, a
## Plot the frequency response .
#w, h = freqz (b, a)
## Filter the data
#fdata = lfilter (b,a, data)
##===============================
#nohead =[]
#avgR =[]
#avgT =[]
#maxT =[]
#minT =[]
#avgW =[]
#maxW =[]
#with open ('/ Users / robert_simpson / Downloads / DailyWeather.csv', 'rb') as csvfile :
#    myfile = csv . reader ( csvfile , delimiter =',', quotechar ='|')
#    for row in myfile :
#        nohead . append ( row )
#    del nohead [0]
#    for row in nohead :
#        avgR . append ( float ( row [4]) ) # rain
#        avgT . append ( float ( row [8]) )
#        maxT . append ( float ( row [9]) ) # temp
#        minT . append ( float ( row [10]) )
#
#length = len ( avgT )
#windowlen =30
#kernal =[0]* length
#kernal [0: windowlen ]=[1]* windowlen
#filtT =np. convolve (avgT , kernal )/ windowlen
#plt . figure ()
#plt . plot ( filtT )
#plt . ylim (23 ,31)
#plt . xlim (0 ,6000)
#===============================
#ex-2
import numpy as np
from scipy.signal import butter , lfilter , freqz
import matplotlib.pyplot as plt
def butter_lowpass (cutoff , fs , order =5) :
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter (order , normal_cutoff , btype ='low', analog = False )
    return b, a
def butter_highpass ( cutoff , fs , order =5) :
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter (order , normal_cutoff , btype ='high', analog = False )
    return b, a
def butter_bandpass (start ,stop , fs , order =5) :
    nyq = 0.5 * fs
    startstop = [ float ( start ) / nyq , float ( stop )/ nyq]
    b, a = butter (order , startstop , btype ='band', analog = False )
    return b, a

fs =2000.0 # sample rate , Hz
T = 5.0 # duration of signal in seconds
n = int (T * fs) # total number of samples in signal
t = np. linspace (0, T, n, endpoint = False ) # time axis

# #### CP 10.2( a)
data = 10* np. sin (10*2* np.pi*t) + 5* np. sin (50*2* np.pi*t) + 1
# 10.2(b)
noisy =[]
for pnt in data :
    noisy . append ( pnt +np. random . normal (0 ,2))
plt . figure ()
plt . xlabel ('time (s)')
plt . ylabel ('Amp (A.U)')
plt . plot (t, noisy )
plt . title ('Raw Signal')
plt . xlim (0 ,1)

# 10.2(c)
freqspec =np.fft.fft( noisy )
# sampling frequency is n Hz
Hz=np. linspace (0,fs ,n)
plt . figure ()
plt . title ('(c) Spectrum of Siganal')
plt . plot (Hz , np.abs ( freqspec ))
plt . xlim (0 ,100)
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('Magnitude ( Fourier Component )')

# 10.2 (d)
order =9 # order of the filter
b, a = butter_lowpass (60 , fs , order )
w, h = freqz (b, a)
plt . figure ()
plt . title ('(d) 60 Hz Low Pass Filter Response')
plt . plot (fs*w /(2* np.pi), np. abs(h), 'b')
plt . xlim (0 ,100)
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('Gain')
plt . savefig ('10_2d_response.pdf')
nonoise = lfilter (b,a, noisy )
plt . figure ()
plt . title ('(d) Signal after cleaning with 60 Hz low pass filter')
plt . plot (t, nonoise )
plt . xlim (0 ,1)
plt . xlabel ('Time ( sec )')
plt . ylabel ('Amplitude')

# 10.2(e)
order = 2 # the order of the filter --- related to the sharpness of the filter window
b, a = butter_bandpass (48 ,52 , fs , order ) # create a butterworth bandpass filter
w, h = freqz (b, a) # calculate the window in frequency space
plt . figure () # plot the bandpass window
plt . plot (fs*w /(2* np.pi), np. abs(h), 'b-')
plt . xlim (0, 100)
plt . title ("(e) 50 Hz Bandpass Filter Response ")
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('Gain')
plt . grid ()
# Plot the signal after filtering
w, h = freqz (b, a)
fdata = lfilter (b,a, noisy )
plt . figure ()
plt . title ('(e) 50 Hz Band Pass')
plt . plot (t, fdata )
plt . xlim (0. ,1)
plt . xlabel ('Time ( sec )')
plt . ylabel ('Amplitude')


# 10.2(f)
order =9
b, a = butter_highpass (100 , fs , order )
w, h = freqz (b, a) # calculate the window in frequency space
plt . figure () # plot the bandpass window
plt . plot (0.5* fs*w/np.pi , np. abs(h), 'b-')
# plt . plot ( cutoff , 0.5* np. sqrt (2) , ’ko ’)
# plt . axvline ( cutoff , color =’k ’)
plt . xlim (0, 200)
plt . title ("(f) 100 Hz Highpass Filter Response ")
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('Gain')
plt . grid ()
fdata = lfilter (b,a, noisy)
plt . figure ()
plt . title ('(f) High Freq Noise ( after 100 Hz High Pass )')
plt . plot (t, fdata )
plt . xlabel ('Time (sec )')
plt . ylabel ('Amplitude')
plt . xlim (0. ,1)




