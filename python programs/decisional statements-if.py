#decisional statements
#i) if statement

print("statement 1")
print("statement 2")
if False:
    print("True statement1")
    print("True statement2")
    print("True statement3")
    print("True statement4")
print("statement 3")
print("statement 4")

print("-"*50)

#the person is not interested to donate blood (NOTE: Please refer the diagram clearly mentiond in the book)
print("class is happening")
print("announcement came for blood donation")
interested="no"
if interested=="yes":
    print("go to camp")
    print("donate blood")
    print("have some food")
    print("take some rest")
print("class will be resumed")

print("_"*50)

#the person is interested to donate blood
print("class is happening")
print("announcement came for blood donation")
interested="yes"
if interested=="yes":
    print("go to camp")
    print("donate blood")
    print("have some food")
    print("take some rest")
print("classes will be resumed")

print("-"*50)


###################### this might be good ########################
print("Class is Happening")
print("announcement came for blood donation")
interested=input("if interested to doante say 'yes' else say 'no': ")
if interested=="no":
    print("wait untill class starts")
if interested=="yes":
    print("go to camp")
    print("DOnate blood")
    print("take some rest")
    print("have some food")
print("class will be resumed")


############################################################

#program to check whether the value is 10 then substract 5 from it and display. if not, dont display.
value=11
if value==10:
    value-=5
print(value)

#eg2
value=10
if value==10:
    value-=5
print(value)

print("*"*50)
#program to check whether the value is 10. if it is 10 then substract from 5 from it and display, if not check whether it is 15 or not.
#if it is 15 add 10 to it and display. if not also display.

value=15
if value==10:
    value-=5
if value==15:
    value+=10
print(value)

#eg2
value=10
if value==10:
    value-=5
if value==15:
    value+=10
print(value)


#ii)ifelse statemen







