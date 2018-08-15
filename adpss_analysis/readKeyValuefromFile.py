inputfile='C:\Users\yuewang\Desktop\SimpleVariablesSer.txt'
outputfile='C:\Users\yuewang\Desktop\Name.txt'
index_value=104


fo = open(outputfile, "w")
flag=0
keyList=[]
with open(inputfile,'r') as f:
        for key in f:
            #print key
            tmp=key.split(',')
            #print tmp
            #print tmp[2]
            if(int(tmp[2])==index_value):
                if(flag==0):
                    print tmp[3].strip()
                    keyList.append(tmp[3].strip())
                    fo.write(tmp[3].strip())
                    fo.write('\n')
                    flag=1
                else:
                    flag=0
            
            
            #break
        f.close()
 


            
fo.close
      