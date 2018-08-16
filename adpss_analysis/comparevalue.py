import os
import commands
import time
from test.test_datetime import Oddballs

file1='C:\\Users\\yuewang\\Desktop\\version2\\Ser_result.txt'
file2='C:\\Users\\yuewang\Desktop\\version2\\Par_result.txt'
resultfile='C:\\Users\\yuewang\\Desktop\\version2\\result4.txt'


time_slice_on=1
time_slice_begin=49.100000
time_slice_end=50.200000

bool_time=0
time_slice=[]



muxian=1 #1--bus  0--GEN
x1=[]
x2=[]

def writefile(filename, data):
    fo = open(filename, "w")
    for line in data:
        for astr in line:
            #print astr
            #print xx
            
            #xx=("%.6f"  % float(astr))
            tmp=str(astr)+"   "
            fo.write(tmp)
        
        fo.write("\n")
            
    fo.close
    
    
try:
        with open(file1,'r') as f1:
            for line in f1:
                tmp=[]
                
                #judge if time lice is within defined .
                #print line
                #print line.split()[0]


                if(time_slice_on == 1):
                    time_value=float(line.split()[0])
                    print time_value
                    if(time_value>time_slice_end):
                        break
                    if(time_value>time_slice_begin):
                        for x in line.split():
                            tmp.append(x)
                        x1.append(tmp) 
                        continue
                    if(time_value>time_slice_begin):
                        continue
                else:
                    for x in line.split():
                        tmp.append(x)
                    x1.append(tmp) 
               
        
        with open(file2,'r') as f2:
            for line in f2:
                
                tmp=[]
                
                #judge if time lice is within defined .
                
                
                #print time_value
                if(time_slice_on == 1):
                    time_value=float(line.split()[0])
                    if(time_value>time_slice_end):
                        break
                    if(time_value>time_slice_begin):
                        for x in line.split():
                            tmp.append(x)
                        x2.append(tmp)
                        continue
                    if(time_value<time_slice_begin):
                        contine
                else:
                    #print " file 2 open, no time slice on\n"
                    for x in line.split():
                        tmp.append(x)
                    x2.append(tmp) 
          
                 
                
except:
        print "open file error "
        
print "len of x1:"+str(len(x1))+"\n"
print "len of x2:"+str(len(x2))+"\n"
        
lg=len(x1)
data=[]
maxdata=[]
for i in range(len(x1)):
    #print i
    tmp=[]
    tmp.append(x1[i][0])
    for j in range(1,len(x1[i])):
        #print x1[i][j]
        #print x2[i][j]
        t=abs(float(x1[i][j])-float(x2[i][j]))
        if(muxian==1):
            if(j  % 2) == 1:
                t=abs(100*t/float(x1[i][j]))
        tmp.append(round(t,6))
      
    data.append(tmp)

row_num=len(data)
col_num=len(data[0])
 
print row_num
print "-----"
print col_num
print "-----"

cc=0

if(muxian==0 or muxian==1):
    max_row=[]
    max_row.append("-----")
    odd=1
    max_odd=-1
    max_even=-1
    for i in range(1,col_num):
        #print "i="+str(i)+"\n"
        #max_row=[]
        max_tmp=0
        for j in range(row_num):
            xx=float(data[j][i])
            if(xx>max_tmp):
                max_tmp=xx
        max_row.append(round(max_tmp,6))
        if(odd==0):
            #print "odd="+str(odd)
            if(max_tmp>max_even):
                max_even=max_tmp
                #print "max_even="+str(max_even)
                #print "max_tmp="+str(max_tmp)
            odd=1
            
        else:
            #print "odd="+str(odd)
            if(max_tmp>max_odd):
                max_odd=max_tmp
                #print "max_odd="+str(max_odd)
                #print "max_tmp="+str(max_tmp)
            odd=0
        
        

    data.append(max_row)
    print "len of max value:"+str(len(max_row))
    
    print "max value of odd: "+str(max_odd)+"\n"
    print "max value of even: "+str(max_even)+"\n"

               
writefile(resultfile,data)
print "----------Done  ----\n"
