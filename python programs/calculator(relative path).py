# this is known as relative path(where the two files located in same folder)

from calc import *
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
num=input("Enter the operation: ")
if num=='+':
    print(add(a,b))
elif num=='-':
    print(sub(a,b))
elif num=='*':
    print(mul(a,b))
elif num=='/':
    print(div(a,b))
else:
    print("Invalid Operation")
    


