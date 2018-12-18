import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss
fi=(4.5,3.4,3.2,2.7,2.1,1.0,0.8,0.5)
Tc=(440.6,440.3,439.7,438.2,437.3,434.4,431.7,429.7)
kb= 8.617330/100000
x=[]
y=[]
for i in range(0,8):
    t1=-1/kb/Tc[i]
    x.append(t1)
    t2=np.log(fi[i]/Tc[i]**2)
    y.append(t2)
z1=np.polyfit(x, y, 1) 
C=z1[1]
mufi=np.mean(fi)
muTc=np.mean(Tc)
N=100000
sdTc=0.2
sdfi=0.1
fim=np.random.normal(mufi,sdfi,N)
Tcm=np.random.normal(muTc,sdTc,N)
Ea=-(np.log(fim/Tcm**2)-C)*kb*Tcm
num_bins = 50
plt.hist(Ea, num_bins, normed=1, facecolor='blue', alpha=0.5)
Ans_c=np.std(Ea)
Ans_d=ss.sem(Ea)
print Ans_c
print Ans_d