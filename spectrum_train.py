import math
import random
import time
import matplotlib.pyplot as plt
from copy import deepcopy
import os

def get_spectrum(fname,t):
    
    fid = open(fname,'r')
    count = 0
    mscomment = []
    matrix = []
    for line in fid:
        l = line.split()
        if count == 0:
            mscomment.extend(l)
        if count == 4:
            segsites = int(l[1])
        if count == 5:
            positions = l[1:]
        if count >5:
            matrix.extend(l)
        count+=1
        #print l

    #del matrix[-1]
    #print matrix
    fid.close()


    n = len(matrix)
    m = len(matrix[0])
    v_col = []
    #print n,m
    #print matrix
    for j in range(m):
        colsum = 0
        for i in range(n):
            if matrix[i][j] == '1':
                colsum+=1
        #print colsum
        v_col.append(colsum)
    x_i = []
    #print v_col
    for i in range(max(v_col)):
        #print i+1
        x_i.append(v_col.count(i+1))
    ix = []
    i = 1
    for item in x_i:
        ix.append(i*item)
        i+=1
    #print x_i
    while len(ix) <200:
        ix.append(0)
    #print len(ix)
    return ix


def write_file(x,t):
    fname = '..\\spectrum3000_train_tau2000.txt'
    fid = open(fname,'a')
    fid.writelines(["%s " % item for item in x])
    fid.writelines('%s' %t)
    fid.writelines("\n")
    fid.close()



tmax = 200
skip = 1
for t in range(0,10000,2000):
    k = t/10000.0
    tau = ("%0.5f" %k)
    fdir = 'test'+tau
    os.chdir(".\\"+fdir)
    ave = [0]*200
    for i in range(tmax):
        fname = str(i)+'.txt'
        ix = get_spectrum(fname,i)
        write_file(ix,k)
        #for m in range(200):
            #ave[m]+=ix[m]
        #if (i+1)%skip == 0:
            #write_file(ave,t)
            #ave = [0]*200
        
    os.chdir("..")

    
    #write_file(ix,i)    
    #plt.plot(ix)
    #plt.show()
