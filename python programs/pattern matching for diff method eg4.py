# i+j<n+1 i+j==n+1 i+j>n+1
def pattern1(n):
    for j in range(1,n+1):
        for i in range(1,n+1):
            if i+j<n+1:
                print("*",end=" ")
            elif i+j==n+1:
                    print("#",end=" ")
            else:
                print("$",end=" ")
        print()
def pattern11(n):
    for j in range(1,n+1):
        for i in range(1,n+1):
            if i+j<=n+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
def pattern111(n):
    for j in range(1,n+1):
        for i in range(1,n+1):
            if i+j>=n+1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
n=int(input("enter the order"))
pattern1(n)
print("_"*50)
pattern11(n)
print("_"*50)
pattern111(n)
print("_"*50)
                
                
