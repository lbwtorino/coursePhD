import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss
a1b1=[100,140]
a2b1=[230,210]
a3b1=[310,270]
a1b2=[180,140]
a2b2=[160,200]
a3b2=[210,250]
a=np.concatenate((a1b1,a2b1,a3b1,a1b2,a2b2,a3b2),axis=0)
mu=np.mean(a)
##copute SSA
a1=np.concatenate((a1b1,a1b2),axis=0)
mua1=np.mean(a1)
a2=np.concatenate((a2b1,a2b2),axis=0)
mua2=np.mean(a2)
a3=np.concatenate((a3b1,a3b2),axis=0)
mua3=np.mean(a3)
ssa=2*2*((mua1-mu)**2+(mua2-mu)**2+(mua3-mu)**2)
##copute SSB
b1=np.concatenate((a1b1,a2b1,a3b1),axis=0)
mub1=np.mean(b1)
b2=np.concatenate((a1b2,a2b2,a3b2),axis=0)
mub2=np.mean(b2)
ssb=3*2*((mub1-mu)**2+(mub2-mu)**2)
##compute SSE
sse=0
for i in range(len(a1b1)):
    sse=sse+(a1b1[i-1]-np.mean(a1b1))**2
for i in range(len(a2b1)):
    sse=sse+(a2b1[i-1]-np.mean(a2b1))**2
for i in range(len(a3b1)):
    sse=sse+(a3b1[i-1]-np.mean(a3b1))**2
for i in range(len(a1b2)):
    sse=sse+(a1b2[i-1]-np.mean(a1b2))**2
for i in range(len(a2b2)):
    sse=sse+(a2b2[i-1]-np.mean(a2b2))**2
for i in range(len(a3b2)):
    sse=sse+(a3b2[i-1]-np.mean(a3b2))**2
##compute SST
sst=0
for i in range(len(a1b1)):
    sst=sst+(a1b1[i-1]-mu)**2
for i in range(len(a2b1)):
    sst=sst+(a2b1[i-1]-mu)**2
for i in range(len(a3b1)):
    sst=sst+(a3b1[i-1]-mu)**2
for i in range(len(a1b2)):
    sst=sst+(a1b2[i-1]-mu)**2
for i in range(len(a2b2)):
    sst=sst+(a2b2[i-1]-mu)**2
for i in range(len(a3b2)):
    sst=sst+(a3b2[i-1]-mu)**2
##compute SSAB
ssab=sst-ssa-ssb-sse
##compute MSA
msa=ssa/2
##compute MSB
msb=ssb/1
##compute MSAB
msab=ssab/2
##compute MSE
mse=sse/6
##compute F-value
fa=msa/mse
fb=msb/mse
fab=msab/mse
fca=ss.f.ppf(q=1-0.05, dfn=2,dfd=6)
fcb=ss.f.ppf(q=1-0.05, dfn=1,dfd=6)
fcab=ss.f.ppf(q=1-0.05, dfn=2,dfd=6)
