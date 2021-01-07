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

print("-"*50)

#iv) nested if statement
#write a program for the greatest of 5 no's by using nestedif statement.
a,b,c,d,e=10,30,20,40,3 
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print("a is greater")
            else:
                print("e is greater")
        else:
            if d>e:
                print("d is greater")
            else:
                print("e is greater")
    else:
        if c>d:
            if c>e:
                print("c is greater")
            else:
                print("e is greater")
        else:
            if d>e:
                print("d is greater")
            else:
                print("e is greater")
else:
    if b>c:
        if b>d:
            if b>e:
                print("b is greater")
            else:
                print("e is greater")
        else:
            if d>e:
                print("d is greater")
            else:
                print("e is greater")
    else:
        if c>d:
            if c>e:
                print("c is greater")
            else:
                print("e is greater")
        else:
            if d>e:
                print("d is greater")
            else:
                print("e is greater")


print("*"*50)
#check the program of the given no is even (or) not. if it is even, then check that no. is divisible by 6 (or) not. if it is divisible then remove 5 from it.
#if not add 5 to it and show whether it is divisible by 6 (or) not & display the value.

value=12 
if value%2==0: #to check whether it is even or not
if value%6==0: #value should be divisible by 6
        print("value is divisible by 6")
        value-=5 #if value is divisible by 6 than -5
else:
        print("not dividible")
        value+=5 #value is not divisible by 6 than +5
print(value)
                

            

                

            

