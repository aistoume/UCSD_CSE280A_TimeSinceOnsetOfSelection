import os

for t in range(0,5000,50):
    #print t
    k = t/10000.0
    tau = ("%0.5f" %k)
    #print tau
    fdir = 't'+tau
    mkd = 'mkdir ' + fdir
    os.system(mkd)
    os.chdir(".\\"+fdir)
    #os.system('dir>'+fdir+'.txt')
    for i in range(500,1000):
        #prefix = 'msms -N 100000 -ms 200 1 -t 20 >'
        #var = str(100/10000.0)
        #suffix = ' 0.00005 -Smark >'+str(i)+'.txt'
        #suffix = str(i)+'.txt'
        #com = prefix+suffix      
        msms = 'msms 200 1 -t 250 -r 250 -N 100000 -SAA 200 -SAa 100 -SF '+(tau) +'>'+str(i)+'.txt'
        os.system(msms)
    os.chdir("..")
