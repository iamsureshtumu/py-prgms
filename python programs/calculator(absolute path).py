# this is known as absolute path(where the two files located in different folder or different directory)

import sys
sys.path.append('C:/Users/anush/AppData/Local/Programs/Python/Python37-32/practice prgms')

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
