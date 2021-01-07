def pattern1(n):
    for j in range(1,n+1):
        for i in range(1,n+1):
            if i<j:
                print("*",end=" ")
            if i==j:
                print("#",end=" ")
            else:
                print("$",end=" ")
        print()
def pattern2(n):
    for j in range(1,n+1):
         for i in range(1,n+1):
             if i>j:
                 print("*",end=" ")
             if i==j:
                 print(" ",end=" ")
             else:
                 print("$",end=" ")
         print()
def pattern3(n):
    for j in range(1,n+1):
        for i in range(1,n+1):
            if i>j:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        print()
n=int(input("enter the orders:"))
pattern1(n)
print("_"*50)
pattern2(n)
print("_"*50)
pattern3(n)
print("_"*50)
