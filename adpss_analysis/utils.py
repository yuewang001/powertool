


def  parseFile(file):
    KeyValueList=[]
    with open(file,'r') as f:
        for line in f:
            tmp=line.strip().split('=')
            #print tmp[0]
            #print tmp[1]
            KeyValueList.append([tmp[0],tmp[1]])
    #print KeyValueList
    return KeyValueList


def queryValue(key,keyValuelist):
    for (x,y) in keyValuelist:
         if(key==x):
             return y
    return None
       
       

result=[]
if __name__ == '__main__':
    
    file='C:\\Users\\yuewang\\Desktop\\config.txt'
    result=parseFile(file)
    print "----------"
    print result
    
    print queryValue('zz',result)
    print queryValue('x',result)
    