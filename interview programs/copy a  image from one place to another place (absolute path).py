## copy a file/image/video from one location to another location
## to copy image format or video format...we use read binary

file1=open('C:/Users/anush/Desktop/nani.jpg','rb')
file2=open('C:/Users/anush/AppData/Local/Programs/Python/Python37-32/s.jpg','wb')

for data in file1:
        file2.write(data)

print("success")
file1.close()
file2.close()

