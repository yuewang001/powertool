import os
import commands
import time
from utils import parseFile 
from utils import queryValue
import sys

#print len(sys.argv)
if(len(sys.argv)==1):
    configfile='C:\\Users\\yuewang\\Desktop\\config.txt'
else:
    configfile=sys.argv[1]

print "config file:"+configfile

config_key_value=parseFile(configfile)
file1=queryValue('file1',config_key_value)
file2=queryValue('file2',config_key_value)
resultfile=queryValue('resultfile',config_key_value)
time_slice_on=int(queryValue('time_slice_on',config_key_value))
time_slice_begin=float(queryValue('time_slice_begin',config_key_value))
time_slice_end=float(queryValue('time_slice_end',config_key_value))
muxian=int(queryValue('muxian',config_key_value))
print_all_data=int(queryValue('print_all_data',config_key_value))
print "file1: "+file1
print "file2:"+file2
print "resultfile:"+resultfile

#resultfile='C:\\Users\\yuewang\\Desktop\\result4.txt'
#configfile='C:\\Users\\yuewang\\Desktop\\config.txt'
#file1='C:\\Users\\yuewang\\Desktop\\Ser_result.txt'
#file2='C:\\Users\\yuewang\Desktop\\Par_result.txt'
#resultfile='C:\\Users\\yuewang\\Desktop\\result4.txt'


#time_slice_on=1
#time_slice_begin=49.100000
#time_slice_end=50.200000

#print_all_data=1

bool_time=0
time_slice=[]

#muxian=1 #1--bus  0--GEN


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
    
def constructMatrixFromFile(file):
    x=[]
    global time_slice_on
    global time_slice_begin
    global time_slice_end
    
    try:
        with open(file,'r') as f:
            for line in f:
                tmp=[]
                
                if(time_slice_on == 1):
                    time_value=float(line.split()[0])
                    
                    if(time_value>time_slice_end):
                        break
                    if(time_value>time_slice_begin):
                        print time_value
                        for xtmp in line.split():
                            tmp.append(xtmp)
                        x.append(tmp) 
                        continue
                    if(time_value>time_slice_begin):
                        continue
                else:
                    for xtmp in line.split():
                        tmp.append(xtmp)
                    x.append(tmp) 
        return x
    except:
         print "open file error "
     

        
def comp(x1,x2):
    print "len of x1:"+str(len(x1))+"\n"
    print "len of x2:"+str(len(x2))+"\n"
    if(len(x1)==0 or len(x2)==0): 
        return 
    
    lg=len(x1)
    global data
    global result_data
    global muxian
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
        result_data.append(max_row)
        re1="max value of odd: "+str(max_odd)
        re2="max value of even: "+str(max_even)
        result_data.append(re1.strip())
        result_data.append(re2.strip())
        data.append(re1.strip())
        data.append(re2.strip())
        print "len of max value:"+str(len(max_row))
        
        print "max value of odd: "+str(max_odd)+"\n"
        print "max value of even: "+str(max_even)+"\n"



data=[]
result_data=[]

x1=constructMatrixFromFile(file1)
#print "len of x1:"+str(len(x1))+"\n"
x2=constructMatrixFromFile(file2)
#print "len of x2:"+str(len(x1))+"\n"
comp(x1,x2)
            
if(print_all_data==1):
    writefile(resultfile,data)
else:
    writefile(resultfile,result_data)
print "----------Done  ----\n"
