#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:07:28 2018

@author: liubowen
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as ss   
import math

import matplotlib.ticker as ticker
plt.figure()
eth = 201.9
gas_price = 2.9e-9*eth
#print gas_price

def plotMultiple():
    y1 = [461688, 953844, 1425782, 1902189, 2381856]
    y2 = [461723, 950011, 1445988, 1932209, 2419099]
    y3 = [470280, 984529, 1473357, 1940010, 2428734]
    y4 = [470302, 991023, 1474099, 1978600, 2461287]
    y5 = [495382, 1038728, 1513798, 2049017, 2518945]
    y6 = [495382.0*gas_price, 1038728.0*gas_price, 1513798.0*gas_price, 
         2049017.0*gas_price, 2518945.0*gas_price]
    x = [1,2,3,4,5]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y1, ':r', marker='^', markeredgecolor='r', markersize=7, label="Type-1");
    ax1.plot(x, y2, ':g', marker='>', markeredgecolor='g', markersize=7, label='Type=2')
    ax1.plot(x, y3, ':b', marker='*', markeredgecolor='b', markersize=8, label='Type=3')
    ax1.plot(x, y4, ':m', marker='<', markeredgecolor='m', markersize=7, label='Type=4')
    ax1.plot(x, y5, ':k', marker='o', markeredgecolor='k', markersize=7, label='Type=5')
    ax1.set_xlabel('Tickets Type');
    ax1.set_ylabel('Gas Cost');
    ax2 = ax1.twinx() # this is the important function
    y = [0.3, 0.6, 0.9, 1.2, 1.5]
    ax2.plot(x, y, ':w',marker='^')
#    ax2.ytickes(y_tickets)
    ax2.set_ylabel('Cost(USD dollar)');
    x_ticks = np.arange(1, 10, 1)
    plt.xticks(x_ticks)
    #plt.yticks(my_y_ticks)
    ax1.legend(loc='upper left')
#    plt.plot(x, y, ':b', marker='p', markeredgecolor='b')
    plt.xlabel("Tickets number")
    plt.ylabel("Cost(USD dollar)")
    fig.tight_layout()
    fig.savefig('multiple.pdf')


def plotSingle():
    y1 = [461688, 461723, 470280, 
         470302, 495382.0]
    y2 = [461688.0*gas_price, 461723.0*gas_price, 470289.0*gas_price, 
         470302.0*gas_price, 495382.0*gas_price]
    print y2
    x = [1,2,3,4,5]
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y1, ':r', marker='^', label="right");
#    ax1.legend(loc=1)
    ax1.set_xlabel('Tickets Type');
    ax1.set_ylabel('Gas Cost');
#    ax1.get_yaxis().set_major_formatter(plt.LogFormatter(10,  labelOnlyBase=False))
    ax2 = ax1.twinx() # this is the important function
    ax2.plot(x, y2, ':r',marker='^', label = "left")
#    ax2.legend(loc=2)
#    ax2.set_xlim([0, np.e]);
    x_ticks = np.arange(1, 6, 1)
    plt.xticks(x_ticks)
    ax2.set_ylabel('Cost(USD dollar)');
    ax2.set_xlabel('Tickets Type'); 
    plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%1.3f'))
#    plt.plot(x, y, marker='+', markeredgecolor='red')
    plt.xlabel("Tickets type")
#    plt.ylabel("Cost(USD dollar)")
#    plt.ylim(0.2,0.3)
    plt.figure(figsize=(60,30))
#    plt.show()
    fig.tight_layout()
    fig.savefig('single.pdf')
   
def specificType5():
#    y5 = [495382, 1038728, 1513798, 2049017, 2518945]
    N = 5
    parseMeans = (0.040, 0.042, 0.045, 0.050, 0.053)
    sigMeans = (0.790, 0.760, 0.770, 0.770, 0.760)
    moveMeans = (0.040, 0.038, 0.039, 0.039, 0.039)
    move2 = (0.83, 0.802, 0.815, 0.820, 0.813)
    mechaMeans = (0.13, 0.16, 0.146, 0.141, 0.148)
    mecha2= (0.87, 0.84, 0.852, 0.851, 0.852)
#    menStd = (2, 3, 4, 1, 2)
#    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    p1 = plt.bar(ind, parseMeans, width)
    p2 = plt.bar(ind, sigMeans, width, bottom=parseMeans)
    p3 = plt.bar(ind, moveMeans, width, bottom=move2)
    p4 = plt.bar(ind, mechaMeans, width, bottom=mecha2)
     
    plt.ylabel('Percentage')
    plt.xlabel('Tickets Number (Type=5)')
    plt.title('Cost Percentage For Each Operation')
    plt.xticks(ind, ('1', '2', '3', '4', '5'))
#    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Parse', 'verify-sig', 'One-trip index', 'Miscellaneous'))
    
    plt.savefig('specific-type5.pdf')
    plt.show()
    
    
def specificType1():
#    y1 = [461688, 953844, 1425782, 1902189, 2381856]
    N = 5
    parseMeans = (0.045, 0.043, 0.042, 0.042, 0.042)
    sigMeans = (0.826, 0.800, 0.790, 0.800, 0.795)
    mechaMeans = (0.129, 0.157, 0.168, 0.158, 0.163)
    mecha2= (0.871, 0.843, 0.832, 0.842, 0.837)
    ind = np.arange(N)    
    width = 0.35       
    
    p1 = plt.bar(ind, parseMeans, width)
    p2 = plt.bar(ind, sigMeans, width, bottom=parseMeans)
    p3 = plt.bar(ind, mechaMeans, width, bottom=mecha2)
    
    plt.ylabel('Percentage')
    plt.xlabel('Tickets Number (Type=1)')
    plt.title('Cost Percentage For Each Operation')
    plt.xticks(ind, ('1', '2', '3', '4', '5'))
#    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0], p3[0]), ('Parse', 'Verify-sig', 'Miscellaneous'))
    
    plt.savefig('specific-type1.pdf')
    plt.show()
    
def NumberInc():
    x_title = ['$10^{0}$', '$10^{1}$', '$10^{2}$', '$10^{3}$', '$10^{4}$']
    x = [1,2,3,4,5]
    y1 = [0.116605959,	0.025104594,	0.010172219,	0.011061569,	0.0066930  ]
    plt.plot(x, y1, ':r', marker='s', markeredgecolor='r', markersize=7, label='Type=1')
    y2 = [0.098063946,	0.025626707,	0.00918169,	0.012875495,	0.0068752  ]
    plt.plot(x, y2, ':g', marker='>', markeredgecolor='g', markersize=7, label='Type=2')
    y3 = [0.089972019,	0.027306914,	0.01574759,	0.011213413,	0.0066791  ]
    plt.plot(x, y3, ':b', marker='*', markeredgecolor='b', markersize=8, label='Type=3')
    y4 = [0.09879303,	0.030475402,	0.017266011,	0.012062883,	0.0068459  ]
    plt.plot(x, y4, ':m', marker='<', markeredgecolor='m', markersize=7, label='Type=4')
    y5 = [0.102459908,	0.040509105,	0.02990006,	0.02288891,	0.0222897 ]
    plt.plot(x, y5, ':k', marker='o', markeredgecolor='k', markersize=7, label='Type=5')
    plt.xlabel("Number of queries")
    plt.ylabel("Time Cost (s/query)")
    plt.grid(True)
    plt.xticks(x, x_title)
    plt.xlim(0.5, 5.2)
    plt.ylim(0.001, 0.14)
    plt.legend()
    plt.title("Throughput of AAA")
    plt.savefig('query.pdf')
    
    
def NumberInc2():
    y_title = ['$10^{0}$', '$10^{1}$', '$10^{2}$', '$10^{3}$', '$10^{4}$']
    y = [1,2,3,4,5]
    x1 = [0.116605959,	0.025104594,	0.010172219,	0.011061569,	0.0066930  ]
    plt.plot(x1, y, ':r', marker='s', markeredgecolor='r', markersize=7, label='Type=1')
    x2 = [0.098063946,	0.025626707,	0.00918169,	0.012875495,	0.0068752  ]
    plt.plot(x2, y, ':g', marker='>', markeredgecolor='g', markersize=7, label='Type=2')
    x3 = [0.089972019,	0.027306914,	0.01574759,	0.011213413,	0.0066791  ]
    plt.plot(x3, y, ':b', marker='*', markeredgecolor='b', markersize=8, label='Type=3')
    x4 = [0.09879303,	0.030475402,	0.017266011,	0.012062883,	0.0068459  ]
    plt.plot(x4, y, ':m', marker='<', markeredgecolor='m', markersize=7, label='Type=4')
    x5 = [0.102459908,	0.040509105,	0.02990006,	0.02288891,	0.0222897 ]
    plt.plot(x5, y, ':k', marker='o', markeredgecolor='k', markersize=7, label='Type=5')
    plt.ylabel("Number of queries")
    plt.xlabel("Time Cost (s/query)")
    plt.grid(True)
    plt.yticks(y, y_title)
    plt.ylim(0.5, 5.2)
    plt.xlim(0.001, 0.14)
    plt.legend()
    plt.title("Throughput of AAA")
    plt.savefig('query2.pdf')
    
def NumberInc3():
    x_title = ['$10^{0}$', '$10^{1}$', '$10^{2}$', '$10^{3}$', '$10^{4}$']
    x = [1,2,3,4,5]
    y1 = [0.116605959,	0.025104594*10,	0.010172219*10**2,	0.011061569*10**3,	0.0066930*10**4]
    plt.plot(x, y1, ':r', marker='s', markeredgecolor='r', markersize=7, label='Type=1')
    y2 = [0.098063946,	0.025626707*10,	0.00918169*10**2,	0.012875495*10**2,	0.0068752*10**4]
    plt.plot(x, y2, ':g', marker='>', markeredgecolor='g', markersize=7, label='Type=2')
    y3 = [0.089972019,	0.027306914*10,	0.01574759*10**2,	0.011213413*10**2,	0.0066791*10**4]
    plt.plot(x, y3, ':b', marker='*', markeredgecolor='b', markersize=8, label='Type=3')
    y4 = [0.09879303,	0.030475402*10,	0.017266011*10**2,	0.012062883*10**2,	0.0068459*10**4]
    plt.plot(x, y4, ':m', marker='<', markeredgecolor='m', markersize=7, label='Type=4')
    y5 = [0.102459908,	0.040509105*10,	0.02990006*10**2,	0.02288891*10**2,	0.0222897*10**4]
    plt.plot(x, y5, ':k', marker='o', markeredgecolor='k', markersize=7, label='Type=5')
    plt.xlabel("Number of queries")
    plt.ylabel("Time Cost (s)")
    plt.grid(True)
    plt.xticks(x, x_title)
    plt.xlim(0.5, 5.2)
#    plt.ylim(0.001, 0.14)
    plt.legend()
    plt.title("Throughput of AAA")
    plt.savefig('query3.pdf')
    
def NumberInc4():
    x_title = ['$10^{0}$', '$10^{1}$', '$10^{2}$', '$10^{3}$', '$10^{4}$']
    x = [1,2,3,4,5]
    y1 = [0.050,	0.015,	0.00732,	0.00453,	 0.00414]
    plt.plot(x, y1, ':r', marker='s', markeredgecolor='r', markersize=7, label='Type=1(Sender policy)')
    y2 = [0.047,	0.020,	0.00708,	0.00507,	0.00432]
    plt.plot(x, y2, ':g', marker='>', markeredgecolor='g', markersize=7, label='Type=2(Function policy)')
    y3 = [0.052,	0.019,	0.00826,	0.0052,0.0051]
    plt.plot(x, y3, ':b', marker='*', markeredgecolor='b', markersize=8, label='Type=3(Args policy)')
    y4 = [0.062,	0.021,	0.011,	0.0051,	0.0052]
    plt.plot(x, y4, ':m', marker='<', markeredgecolor='m', markersize=7, label='Type=4(Exclusive policy)')
    y5 = [0.125,	0.0324,	0.020,	 0.018,	0.0179]
    plt.plot(x, y5, ':k', marker='o', markeredgecolor='k', markersize=7, label='Type=5(One-way policy)')
    plt.xlabel("Number of queries")
    plt.ylabel("Time Cost (s/query)")
    plt.grid(True)
    plt.xticks(x, x_title)
    plt.xlim(0.5, 5.2)
    plt.ylim(0.001, 0.14)
    plt.legend()
    plt.title("Throughput of AAA")
    plt.savefig('query4.pdf')
#def bitsize():
#    x = [0, 10, 100]
#    y = 


#print 41.4/10000.0
#plotMultiple()
#plotSingle()
#NumberInc() 
#NumberInc2() 
#NumberInc3()
#NumberInc4()
specificType5()
specificType1()
#bitsize()
def specificType6():
    y5 = [495382, 1038728, 1513798, 2049017, 2518945]
    parseMeans = [0.040, 0.042, 0.045, 0.050, 0.053]
    sigMeans = [0.790, 0.760, 0.770, 0.770, 0.760]
    moveMeans = [0.040, 0.038, 0.039, 0.039, 0.039]
    mechaMeans = [0.13, 0.16, 0.146, 0.141, 0.148]
    t1, t2, t3, t4=[], [], [], []
    for i in range(5):
        t1.append(y5[i]*parseMeans[i])
        t2.append(y5[i]*sigMeans[i])
        t3.append(y5[i]*moveMeans[i])
        t4.append(y5[i]*mechaMeans[i])
    print t1, t2, t3, t4

specificType6()




