#check if a string is in a textfile  by using file handling

#Open the file
fobj = open("demo.txt")
text = fobj.read().strip().split()

#Conditions
while True:
    s = input("Enter a string: ") #Takes input of a string from user
    if s == "": #if no value is entered for the string
        continue
    if s in text: #string in present in the text file
        print("Matched")
        break
    else: #string is absent in the text file
        print("No such string found,try again")
        continue
        #break
fobj.close()



print("--------")

# ii)
fobj = open("demo.txt")
text=fobj.read().split()

while True:
        s = input("Enter a string: ")
        if s=="":
                continue
        if s in text:
                print("Matched")
                break
        else:
                print("No such string found,try again")
                continue
fobj.close()

# iii) simple way without continue

fobj=open("demo.txt")
text=fobj.read()

s=input("Enter a string")
if s in text:
    print("matched")
else:
    print("No such string present, try again")

fobj.close()

