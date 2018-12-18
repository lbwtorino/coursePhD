#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:52:36 2018

@author: liubowen
"""
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as ss

def SSW (* arg ):
    n= len (arg[0]) 
    levels = len(arg)
    ssw =0
    for i in range (levels):
        var =np.var(arg[i], ddof =0)
        ssw = ssw + var
    df =(n* levels )-levels
    return (n* ssw ), df
    
def SSB (* arg ):
    grandmean =0
    levels = len ( arg )
    for i in range ( len (arg)):
        grandmean = grandmean +np. mean ( arg [i])
    grandmean = grandmean /len( arg)
    ssb =0
    for i in range ( len (arg)):
        temp =np. mean (arg [i])
        ssb = ssb +( temp - grandmean ) **2
    ssb = len (arg [0]) *ssb
    df= levels -1
    return ssb , df

# find the closed 10 data in all samples
def findClosed(data):
    data.sort()
    size = len(data)
    tmp = data[4] - data[0]
    index = [0, 4]
    for i in range(size-4):
        diff = data[i+4] - data[i]
        if diff < tmp:
            index[0] = i
            index[1] = i+4
    return data[index[0]:index[1]+1]


def Hz1():
    chicken =[508, 164, 698, 1143, 465, 1947, 1057, 1168, 354, 3325, 909, 671, 567, 469, 208, 461, 1]
    porker =[3202, 399, 360, 1838, 21134, 14919, 4193, 161, 151, 2233, 59, 1598]
    xiao =[236, 555, 2000, 908, 1760, 500, 960, 984, 307, 229, 390, 497, 351, 629, 572, 248, 1290, 274]
    
    cartoon =[661, 314, 887, 547, 755, 616, 329, 423, 574, 640, 131, 1664, 434, 384, 135, 451, 329, 936]
    comedy = [1825, 148, 331, 310, 507, 674, 669, 394, 265, 394, 1396, 906, 898, 724, 276, 453, 566, 1089, 1111, 1067]
    horrible = [1555, 564, 1964, 1635, 2370, 2231, 5184, 166, 259, 946, 141, 134, 1558, 399, 423, 3999, 3994, 878, 166, 509, 761, 9043, 633, 389]
    
    light = [1555, 564, 1964, 1635, 2370, 2231, 5184, 166, 259, 946, 141, 134, 1558, 399, 423, 3999, 3994, 878, 166, 509, 761, 9043, 633, 389]
    rock = [1555, 564, 1964, 1635, 2370, 2231, 5184, 166, 259, 946, 141, 134, 1558, 399, 423, 3999, 3994, 878, 166, 509, 761, 9043, 633, 389]
    yesterday = [794, 430, 1051, 1363, 1006, 1046, 231, 309, 224, 2317, 437, 474, 190, 1563, 446, 530]
            
    h1,h2,h3,h4,h5,h6,h7,h8,h9 = findClosed(chicken),findClosed(porker),findClosed(xiao),findClosed(cartoon),findClosed(comedy),findClosed(horrible),findClosed(light),findClosed(rock),findClosed(yesterday)
    ssw, sswdf = SSW (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    ssb, ssbdf = SSB (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    msw = ssw / sswdf
    msb = ssb / ssbdf
    F= msb / msw
    Fc=ss.f.ppf(0.95, 8, 36)
    print "F=", F
    print " Critical F=", Fc
    if F>Fc:
        print "F>Fc , Reject H0"
    else :
        print "F<Fc , Accept H0"
    F1 , p1 = ss. f_oneway (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    print 'F1', F1, 'p1', p1

def Hz2():
    chicken =[326, 249, 75, 82, 138, 294, 392, 94, 226, 160, 171, 96, 523, 117, 284, 28, 60]
    porker =[22, 314, 663, 546, 4600, 3500, 1759, 301, 403, 1305, 118, 287]
    xiao =[1134, 371, 205, 232, 696, 74, 154, 82, 211, 179, 553, 456, 75, 470, 396, 109, 550, 336]
    
    cartoon =[143, 212, 435, 45, 930, 333, 60, 122, 259, 305, 44, 55, 52, 149, 129, 134, 142, 446]
    comedy = [421, 273, 59, 146, 84, 174, 133, 107, 187, 175, 411, 222, 384, 177, 1359, 190, 144, 2209, 255, 446]
    horrible = [560, 141, 1365, 835, 317, 930, 1869, 134, 205, 421, 89, 141, 883, 74, 23, 938, 1242, 205, 98, 349, 261, 2611, 129, 176]
    
    light = [359, 7840, 4356, 341, 448, 526, 205, 261, 270, 3577, 320, 311, 82, 76, 220, 504, 371, 402]
    rock = [30, 244, 39, 153, 161, 124, 117, 196, 394, 1155, 314, 128, 82, 76, 264, 517, 89, 89]
    yesterday = [212, 271, 108, 282, 120, 24, 119, 119, 140, 811, 130, 124, 410, 1274, 84, 107]
            
    h1,h2,h3,h4,h5,h6,h7,h8,h9 = findClosed(chicken),findClosed(porker),findClosed(xiao),findClosed(cartoon),findClosed(comedy),findClosed(horrible),findClosed(light),findClosed(rock),findClosed(yesterday)
    ssw, sswdf = SSW (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    ssb , ssbdf = SSB (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    msw = ssw / sswdf
    msb = ssb / ssbdf
    F= msb/msw
    Fc=ss.f.ppf (0.95, 8, 36)
    print "F=", F
    print "Critical F=", Fc
    if F>Fc:
        print "F>Fc , Reject H0"
    else :
        print "F<Fc , Accept H0"
    F1, p1 = ss. f_oneway (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    print 'F1', F1, 'p1', p1

def Hz3():
    chicken =[44, 97, 63, 127, 102, 540, 58, 10, 78, 275, 133, 39, 69, 82, 217, 62, 144]
    porker =[39, 460, 339, 128, 2033, 1843, 382, 416, 405, 165, 110, 365]
    xiao =[752, 172, 201, 224, 1189, 126, 110, 77, 33, 165, 350, 79, 165, 117, 117, 80, 239, 24]
    
    cartoon =[22, 8, 37, 57, 355, 90, 34, 51, 138, 46, 16, 33, 35, 104, 12, 71, 27, 96]
    comedy = [22, 8, 37, 57, 355, 90, 34, 51, 138, 46, 16, 33, 35, 104, 12, 71, 27, 96]
    horrible = [386, 5, 371, 175, 135, 375, 1032, 9, 101, 501, 56, 12, 528, 82, 9, 460, 594, 147, 54, 97, 121, 1387, 162, 112]
    
    light = [296, 5914, 2254, 206, 86, 343, 91, 81, 83, 1889, 244, 131, 117, 24, 128, 117, 179, 188]
    rock = [41, 45, 111, 34, 136, 104, 69, 190, 358, 754, 116, 58, 44, 95, 96, 178, 239, 40]
    yesterday = [41, 45, 111, 34, 136, 104, 69, 190, 358, 754, 116, 58, 44, 95, 96, 178, 239, 40]
            
    h1,h2,h3,h4,h5,h6,h7,h8,h9 = findClosed(chicken),findClosed(porker),findClosed(xiao),findClosed(cartoon),findClosed(comedy),findClosed(horrible),findClosed(light),findClosed(rock),findClosed(yesterday)
    ssw, sswdf = SSW (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    ssb , ssbdf = SSB (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    msw = ssw / sswdf
    msb = ssb / ssbdf
    F= msb / msw
    Fc=ss.f.ppf (0.95, 8, 36)
    print "F=", F
    print " Critical F=", Fc
    if F>Fc:
        print "F>Fc , Reject H0"
    else :
        print "F<Fc , Accept H0"
    F1 , p1 = ss. f_oneway (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    print 'F1', F1, 'p1', p1

def Hz4():
    chicken =[72, 35, 16, 18, 34, 125, 28, 54, 36, 51, 55, 28, 46, 46, 23, 36, 25]
    porker =[32, 129, 105, 74, 1237, 986, 248, 103, 190, 174, 34, 31]
    xiao =[245, 12, 60, 71, 169, 29, 36, 55, 28, 21, 128, 21, 54, 27, 63, 22, 64, 40]
    
    cartoon =[18, 32, 16, 51, 126, 19, 13, 20, 70, 46, 28, 26, 22, 25, 17, 24, 26, 5]
    comedy = [71, 30, 3, 13, 13, 18, 44, 34, 10, 50, 133, 90, 173, 0, 8, 30, 43, 78, 10, 71]
    horrible = [143, 25, 183, 31, 128, 201, 452, 15, 48, 39, 17, 67, 224, 41, 35, 181, 349, 89, 79, 101, 106, 607, 13, 66]
    
    light = [141, 2068, 1446, 49, 59, 148, 164, 66, 37, 885, 120, 95, 90, 39, 17, 98, 79, 57]
    rock = [20, 63, 51, 2, 67, 27, 42, 94, 44, 97, 33, 20, 31, 9, 111, 88, 60, 41]
    yesterday = [17, 44, 36, 120, 11, 38, 21, 43, 47, 251, 25, 45, 88, 305, 99, 46]
            
    h1,h2,h3,h4,h5,h6,h7,h8,h9 = findClosed(chicken),findClosed(porker),findClosed(xiao),findClosed(cartoon),findClosed(comedy),findClosed(horrible),findClosed(light),findClosed(rock),findClosed(yesterday)
    ssw, sswdf = SSW (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    ssb , ssbdf = SSB (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    msw = ssw / sswdf
    msb = ssb / ssbdf
    F= msb / msw
    Fc = ss.f.ppf(0.95, 8, 36)
    print "F=", F
    print " Critical F=", Fc
    if F>Fc:
        print "F>Fc , Reject H0"
    else :
        print "F<Fc , Accept H0"
    F1, p1 = ss.f_oneway (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    print 'F1', F1, 'p1', p1

def Hz5():
    chicken =[42, 19, 14, 11, 31, 54, 14, 45, 24, 58, 33, 13, 17, 35, 15, 10, 22]
    porker =[11, 73, 63, 41, 624, 569, 98, 63, 76, 97, 10, 33]
    xiao =[54, 24, 13, 29, 30, 36, 16, 25, 15, 36, 63, 19, 29, 12, 41, 14, 3, 13]
    
    cartoon =[54, 24, 13, 29, 30, 36, 16, 25, 15, 36, 63, 19, 29, 12, 41, 14, 3, 13]
    comedy = [5, 15, 5, 11, 8, 4, 40, 12, 5, 17, 68, 79, 78, 27, 31, 14, 14, 31, 8, 40]
    horrible = [92, 6, 101, 50, 148, 148, 226, 14, 4, 45, 2, 25, 99, 17, 21, 49, 120, 22, 18, 28, 53, 513, 41, 30]
    
    light = [92, 6, 101, 50, 148, 148, 226, 14, 4, 45, 2, 25, 99, 17, 21, 49, 120, 22, 18, 28, 53, 513, 41, 30]
    rock = [5, 28, 22, 2, 45, 8, 23, 41, 33, 13, 51, 21, 10, 13, 61, 60, 18, 28]
    yesterday = [33, 24, 31, 61, 13, 18, 13, 12, 21, 143, 8, 17, 35, 226, 49, 14]
            
    h1,h2,h3,h4,h5,h6,h7,h8,h9 = findClosed(chicken),findClosed(porker),findClosed(xiao),findClosed(cartoon),findClosed(comedy),findClosed(horrible),findClosed(light),findClosed(rock),findClosed(yesterday)
    ssw, sswdf = SSW (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    ssb , ssbdf = SSB (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    msw = ssw / sswdf
    msb = ssb / ssbdf
    F= msb / msw
    Fc = ss.f.ppf (0.95, 8, 36)
    print "F=", F
    print " Critical F=", Fc
    if F>Fc:
        print "F>Fc , Reject H0"
    else :
        print "F<Fc , Accept H0"
    F1 , p1 = ss. f_oneway (h1,h2,h3,h4,h5,h6,h7,h8,h9)
    print 'F1', F1, 'p1', p1
    
Hz1()
Hz2()
Hz3()
Hz4()
Hz5()
