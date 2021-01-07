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

print("_"*50)

#ii)ifelse statement

#NOTE: refer the diagram first
#eg1, he is not interested
print("class is happening")
print("announcement come from blood camp")
interested="no"
if interested=="yes":
    print("go to camp")
    print("donate blood")
    print("have some food")
    print("take some rest")
else:
    print("go out")
    print("have food")
print("class will be resumed")

print("_"*50)
#eg2, he is interested
print("class is happening")
print("announcement came from blood camp")
interested="yes"
if interested=="yes":
    print("go to camp")
    print("donate blood")
    print("have some food")
    print("take some rest")
else:
    print("go out")
    print("have some food")
print("class will be resumed")

print("-"*50)

#program to check whether the givrn value is 10 or not.
#eg1
value=10
if value==10:
    print("Hai")
else:
    print("hello")

#eg2    
value=20
if value==10:
    print("hai")
else:
    print("hello")

print("*"*50)
#program to find the greatest among 2 numbers.
a,b=100,20
if a>b:
    print("a is greater")
else:
    print("b is greater")




