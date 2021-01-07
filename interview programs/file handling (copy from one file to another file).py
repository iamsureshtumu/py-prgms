file1=open("demo.txt",'r')
file2=open("testing.txt",'w')

for data in file1:  #for loop
    file2.write(data)
print("success")
file1.close()
file2.close()

####################

file1=open("demo.txt",'r')
file2=open("testing.txt",'w')

file2.write(file1.read())       ##########simplified way

print("success")
file1.close()
file2.close()

####################

