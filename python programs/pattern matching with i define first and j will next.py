#decrementation k=1+j-1 and k+=1 (here i will define first and j will be next)
def pattern1(n):
    for i in range(1,n+1):
        k=1+i-1
        for j in range(1,n+1):
            if i<=j:
                print(k,end=" ")
                k+=1
            else:
                print(" ",end=" ")
        print()
def pattern11(n):
    for i in range(1,n+1):
        k=ord('A')+i-1
        for j in range(1,n+1):
            if i<=j:
                print(chr(k),end=" ")
                k+=1
            else:
                print(" ",end=" ")
        print()
def pattern2(n):
    for i in range(1,n+1):
        k=1+i-1
        for j in range(1,n+1):
            if i>=j:
                print(k,end=" ")
                k+=1
            else:
                print(" ",end=" ")
        print()
def pattern22(n):
    for i in range(1,n+1):
        k=ord('A')+i-1
        for j in range(1,n+1):
            if i>=j:
                print(chr(k),end=" ")
                k+=1
            else:
                print(" ",end=" ")
        print()
n=int(input("enter the order:"))
pattern1(n)
print("_"*20)
pattern11(n)
print("_"*20)
pattern2(n)
print("_"*20)
pattern22(n)
print("_"*20)
        

                
     
        
