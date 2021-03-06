import serial, io
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz

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

ser = serial.Serial('COM3', 57600, timeout=.1)
time.sleep(2)

ser.flushInput()
ser.flushOutput()



fname = '/Users/robert_simpson/EEGdata/data.dat'
fmode = 'w+'
t0=float(time.time())




def block(ser, duration):
    now=0;
    counter=0
    times=[]
    volts=[]
    while now < duration:
        counter=counter+1
        myt=ser.readline().strip('\r\n').split(',')[0]
        myv=ser.readline().strip('\r\n').split(',')[1]
        now=float(time.time())-t0
        nowstr=str(now)
        if counter >0:
            times.append(int(ser.readline().strip('\r\n').split(',')[0]))
            print ser.readline().strip('\r\n').split(',')
            volts.append(int(ser.readline().strip('\r\n').split(',')[1]))
        #out=zip(times, volts)
    return times, volts
            #print (counter, myt, myv)
        #time.sleep(0.001)
    #        f.write(nowstr + '\t' + x)
    #        f.flush()


times=[]
volts=[]
times, volts=block(ser, measuretime)

def writeFile():
    with open('music\light\data'+str(time.time())+'.dat', 'w') as f:
        for i in range(len(times)):
            f.write(str(times[i])+','+str(volts[i]))
            f.write('\n')
            
writeFile()

t=np.linspace(times[0],times[len(times)-1],len(times)) #creates regular time grid in secs
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

#
#plt.xlim(0,1)
#plt.xlabel('Time (sec)')
#plt.ylabel('Amplitude')



#N=20
#x=[]
#y=[]
##plt.axis()
#
#
##times, volts=block(ser, 1)
#fig=plt.figure()
#ax = fig.add_subplot(111)
#line1, = ax.plot(x, y, 'b-') 
#
#for i in range(N):
#
#    times, volts=block(ser, 1)
#    #plt.ion()
#    x.extend(times)
#    y.extend(volts)
#    
#    line1.set_xdata(x)
#    line1.set_ydata(y)
##    #plt.cla()
##    plt.plot(x, y)
##    plt.draw()
#    fig.canvas.draw()
##    plt.pause(0.05)
##    time.sleep( 1)
#
ser.close()
##plt.show()