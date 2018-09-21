import math
import random
import time
import matplotlib.pyplot as plt
from copy import deepcopy

def initial(N):
    listofzeros = []
    for i in range(N):
        listofzeros.append([])
    
    return listofzeros

def mutate(matrix):
    N = len(matrix)
    mutation = len(matrix[0])
    k = random.randint(0,N-1)
    matrix[k].append(1)
    
    for i in [x for x in range(N) if x not in [k] ]:
        matrix[i].append(0)   
    return matrix

def descend(matrix):
    N = len(matrix)
    i = random.randint(0,N-1)
    j = random.randint(0,N-1)
    matrix[j] = deepcopy(matrix[i])
    return matrix

def coalescent(matrix):
    N = len(matrix)
    m = len(matrix[0])
    i = random.randint(0,N-1)
    j = random.randint(0,N-1)
    p = random.randint(0,N-1)
    newcopy = deepcopy(matrix[p])
    r = 0.5
    k = int(m*r)
    buff = []
    buff.extend(matrix[i][0:k])
    buff.extend(matrix[i][k:m])
    matrix[i] = deepcopy(buff)
    matrix[j] = deepcopy(newcopy)
    #print i,j,p
    #print k,m
    return matrix

def selection(matrix,locus,s):
    N = len(matrix)
    m = len(matrix[0])
    if locus>=m:
        print 'Out of gene range'
        return matrix
    i = 0
    while i<N:
        if matrix[i][locus]== 1:
            p = random.random()
            if p<s:
                del matrix[i]
                N = len(matrix)
            else:
                i+=1
        else:
            i+=1
                
    return matrix
            

def addpop(matrix,Npop):
    N = len(matrix)
    for i in range(Npop-N):
        k = random.randint(0,N-1)
        matrix.append(deepcopy(matrix[k]))
    return matrix

def sampling(matrix,n,t):
    pool = []
    N = len(matrix)
    m = len(matrix[0])
    for i in range(N):
        for j in range(m):
            if matrix[i][j] == 1:
                pool.extend([i])
                break
    while len(pool)<n:
        pool.extend([random.randint(0,N)])
        pool = list(set(pool))
    index = random.sample(pool,n)
    index.sort()
    fname = 't'+ str(t)+ '.txt'
    fid = open(fname,'w')
    for i in index:
        #print matrix[i]
        fid.writelines(["%s" % item for item in matrix[i]])
        fid.writelines("\n")
    fid.close()
    #print pool
    return index

    
T = 2000
Npop = 100000
M = initial(Npop)
T_select = 1000
tau = T - T_select
n = 200
if n>Npop:
    print 'n should be less than Npop'
for t in range(T):
    M = mutate(M)
    M = descend(M)
    if t%20 == 0:
        output = sampling(M,n,t)
    if t > T_select:
        M = selection(M,1,0.8)
        M = addpop(M,Npop)
        
   # print M
