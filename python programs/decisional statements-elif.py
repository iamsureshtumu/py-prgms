#iii)elif statement.
#student is going to one of engieering college to join course.
#interested to join cse
print("enter to college")
print("going to each dept.")
interest="cs"
if interest=="cs":
    print("join to CSE")
elif interest=="ec":
    print("join to EC")
elif interest=="mech":
    print("join to mech")
else:
    print("join to civil")

print("-"*50)
#if he is interested to join mech
print("enter to college")
print("going to each dept.")
interest="mech"
if interest=="cs":
    print("join to cs")
elif interest=="ec":
    print("join to ec")
elif interest=="mech":
    print("join to mech")
else:
    print("join to civil")

print("-"*50)
#write a program to check the greatest of 3 no's.
a=10
b=20
c=30
if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")

#a,b,c=10,20,30
#print(a)=10
#print(b)=20
#print(c)=30

print("-"*50)
#write a program to check the greatest of 5 no's.
a,b,c,d,e=10,40,29,50,30
if a>b and a>c and a>d and a>e:
    print("a is greater")
elif b>c and b>d and b>e:
    print("b is greater")
elif c>d and c>e:
    print("c is greater")
elif d>e:
    print("d is greater")
else:
    print("e is greater")

print("*"*50)
#write a program to the given input values are equal. if the input is same then print the value.

a,b,c,d,e=10,10,10,10,10
if a>b and a>c and a>d and a>e:
    print("{} is greater".format(a))
elif b>c and b>d and b>e:
    print("{} is greater".format(b))
elif c>d and c>e:
    print("{} is greater".format(c))
elif d>e:
    print("{} is greater".format(d))
else:
    print("{} is greater".format(e))

#iv) nested if statement

#write a program for the greatest of 5 no's by using nestedif statement.


