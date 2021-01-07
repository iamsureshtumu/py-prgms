#writefunction
#write
fileObj=open("testing.py",'w')   #we can also use .txt file to write or read
def writeData():
    data="hello suresh"
    data1=["hello","hai"]
    fileObj.write(data)
    fileObj.close()
writeData()



  

