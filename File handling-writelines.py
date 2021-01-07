#writelines
fileObj=open("testing.py",'w')  #we can also use .txt to write and read
def writeData():
    data="hello"
    data1=["hi","hello","how","are","you", "suresh"]
    fileObj.writelines(data1)
    fileObj.close()
writeData()  
