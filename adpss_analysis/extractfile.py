import os
import commands
import time

from utils import parseFile 
from utils import queryValue
import sys

#print len(sys.argv)
if(len(sys.argv)==1):
    configfile='C:\\Users\\yuewang\\Desktop\\extract_config.txt'
else:
    configfile=sys.argv[1]

print "config file:"+configfile

config_key_value=parseFile(configfile)
keyfile=queryValue('keyfile',config_key_value)
valueFile=queryValue('valueFile',config_key_value)
resultfile=queryValue('resultfile',config_key_value)
time_slice_on=int(queryValue('time_slice_on',config_key_value))
time_slice_begin=float(queryValue('time_slice_begin',config_key_value))
time_slice_end=float(queryValue('time_slice_end',config_key_value))
prefix=queryValue('prefix',config_key_value)

print "keyfile: "+keyfile
print "file2:"+file2
print "resultfile:"+resultfile

debug=0


bool_time=0
time_slice=[]


def readkeylist(keyfile):
	keyList=[]
	with open(keyfile,'r') as f:
		for key in f:
			#print key
			keyList.append(key.strip())
			#break
	f.close()
	return keyList

def getfilename(key,locationFile):
	find=0
	infoList=[]
	with open(locationFile,'r') as f1:
		for line in f1:
			#print line
			tmp=line.split(',')
			#print tmp[3]
			if(len(tmp)<4):
				continue
			tmp1=tmp[3].strip()
			#print tmp1
			if(key==tmp1):
				#print "same"
				#break
				dir=tmp[6].strip()
				filename=tmp[7].strip()
				col=tmp[8].strip()
				find=find+1
				infoList.append([dir,filename,col])
				if(find==2):
					break
			#keyList.append(key)
	f1.close()
	return infoList	
#aindex is 1 parallel ,0 sequenial 
def getRealValue(afolder,afilename,colNum):
	
	keyList=[]
	
	if(Linux==1):
		fullpathFileName=prefix+afolder+'//'+afilename
	else:
		fullpathFileName=prefix+afolder+'\\'+afilename
	#count=0
	try:
		with open(fullpathFileName,'r') as f:
			print "getRealValue successfully on read file :"+fullpathFileName+"---\n"
			#print f
			for line in f:
				#print key
				tmp=line.split(',')
				#print tmp.strip()
				col=int(colNum)
				
				time_value=float(tmp[0].strip())
				if(time_slice_on == 1):
					if(time_value<time_slice_begin):
						continue
					if(time_value>time_slice_end):
						break
				#print col
				#xx=key.strip()

				keyList.append(tmp[col].strip())
				
#				 if(debug==1):
#					 count=count+1
#					 if(count>20):
#						 break
		print "getRealValue successfully  :"+fullpathFileName+"---\n"
		return keyList
	except:
		print "getRealValue error on read file :"+fullpathFileName+"---col:"+colNum+"\n"
		return 
	
	
def getTimeSlice(afolder, afilename):

	keyList=[]
	if(Linux==1):
		fullpathFileName=prefix+afolder+'//'+afilename
	else:
		fullpathFileName=prefix+afolder+'\\'+afilename
	#count=0
	try:
		with open(fullpathFileName,'r') as f:
			for line in f:
				tmp=line.split(',')
				time_value=float(tmp[0].strip())
				if(time_slice_on == 1):
					if(time_value<time_slice_begin):
						continue
					if(time_value>time_slice_end):
						break
				keyList.append(tmp[0].strip())
#				 if(debug==1):
#					 count=count+1
#					 if(count>20):
#						 break
		return keyList
	except:		   
		print "getTimeSlice get error---------on  open file:"+afolder+"---"+afilename
		return 

def writefile(filename, data):
	fo = open(filename, "w")
	for line in data:
		for astr in line:
			tmp=str(astr)+"   "
			fo.write(tmp)
		fo.write("\n")
			
	fo.close

   
if __name__ == "__main__":
		
		x=readkeylist(keyfile)
		key_location=[]
		val_result=[]
		
		time_val_seq=0
		time_val_para=0
		#read time line
		step=0;
		key_len=len(x)
		for key in x:
			index_array=getfilename(key,valueFile)
			key_location.append([key,index_array])
			print key_location
			
			################################################
		
		count=0
		for one in key_location:
			count=count+1
			print "xxxxxxxxxxxxxx\n"
			print "num key: "+str(count)
			print one
			print "xxxxxxxxxxxxxx\n"
			
			value=getRealValue(one[1][0][0],one[1][0][1],one[1][0][2])
			if type(value)==list:
				if(time_val_seq<len(value)):
					time_val_seq=len(value)
				
				val_result.append(value)
			value=getRealValue(one[1][1][0],one[1][1][1],one[1][1][2])
			val_result.append(value)
	 
	
		
			if(bool_time==0):
				time_slice=getTimeSlice(index_array[0][0],index_array[0][1])
				bool_time=1
		
		data_print=[]
		#print val_result
		print "time step: "+str(len(time_slice))
		for i in range(len(time_slice)):
			#print time_slice[i]  
			#print "i="+str(i)
			tmp_matrix=[]
# 			if(time_slice_on == 1):
# 				if(float(time_slice[i])<time_slice_begin):
# 					continue
# 			
# 				if(float(time_slice[i])>time_slice_end):
# 					break
			tmp_matrix.append(time_slice[i])
			for j in range(len(val_result)):
				#print "j="+str(j)
				tmp_matrix.append(val_result[j][i])
			data_print.append(tmp_matrix)
		writefile(result_file,data_print)
		
		print "Done-------------------"
		#print val_seq
		print "col num:"+str(len(val_result))
	
		print "Done-------------------"
		
		
