#incrementation k=1 and k+=1
def pattern1(n):
    for j in range(1,n+1):
        k=1
        for i in range(1,1+n):
            if i<=j:
                print(k,end=" ")
                k+=1
            else:
                print(" ",end=" ")
        print()
def pattern11(n):
    for j in range(1,n+1):
        k=ord('A')
        for i in range(1,1+n):
            if i<=j:
                print(chr(k),end=" ")
                k+=1
            else:
                print(" ",end=" ")
        print()
def pattern2(n):
    for j in range(1,n+1):
        k=1
        for i in range(1,n+1):
            if i>=j:
                print(k,end=" ")
                k+=1
            else:
                print(" ",end=" ")
        print()
def pattern22(n):
    for j in range(1,n+1):
        k=ord('A')
        for i in range(1,1+n):
            if i>=j:
                print(chr(k),end=" ")
                k+=1
            else:
                print(" ",end=" ")
        print()
n=int(input("enter the order:"))
pattern1(n)
print("_"*50)
pattern11(n)
print("_"*50)
pattern2(n)
print("_"*50)
pattern22(n)
print("_"*50)
                
 

                

                


                
