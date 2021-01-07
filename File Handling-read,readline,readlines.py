#readfunction(read,readline,readlines)
#read
fileObj=open("testing.py",'r')  #demo file is created and mentioned here
print(fileObj)

def display():
    data=fileObj.read()
    print("data\n",data)

display()

print("_"*50)

#readline
fileObj=open("testing.py",'r')
print(fileObj)

def display():
    data=fileObj.readline()
    print("data\n",data)

display()

print("_"*50)

#readlines
fileObj=open("testing.py",'r')
print(fileObj)

def display():
    data=fileObj.readlines()
    print("data\n",data)

display()
print("-"*50)


