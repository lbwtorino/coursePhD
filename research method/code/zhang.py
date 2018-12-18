import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss
#Q1.1#
def analytical(r,Q,dr,dQ,P0):
    dtr=(1/(Q*r/P0+1)*(Q/P0)*r-np.log(Q*r/P0+1))/r**2
    dtQ=1/(Q*r/P0+1)/P0
    dt=dr**2*dtr**2+dQ**2*dtQ**2
    sdt=np.sqrt(dt)
    return sdt
P0=5
r=0.027
dr=0.002
Q=1000
dQ=100
sd1=analytical(r,Q,dr,dQ,P0)
print sd1
###Q1.2##
N=10000000
r2=np.random.normal(r,dr,N)
Q2=np.random.normal(Q,dQ,N)
t2=np.log(Q2*r2/P0+1)/r2
sd2=np.std(t2)
print sd2
