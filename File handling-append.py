#Append

fileobj=open("testing.txt",'a')
def writeData():
    data="\n oar"
    fileobj.write(data)
    fileobj.close()
writeData()

