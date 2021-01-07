#incrementing the values with k=1+j-1
n=5
for j in range(1,n+1):
    k=1+j-1 
    for i in range(1,n+1):
        if i+j>=n+1:
            print(k,end=" ")
            k-=1
        else:
            print(" ",end=" ")
    k+=2        
    for i in range(1,n+1):
        if i<j:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("_"*50)
 
#decrementing the values k=1+n-1
n=5
for j in range(1,n+1):
    k=ord('A')+n-1
    for i in range(1,n+1):
        if i+j>=n+1:
            print(chr(k),end=" ")
            k-=1
        else:
            print(" ",end=" ")
    k+=2
    for i in range(1,n+1):
        if i<j:
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("_"*50)

#decrementing the values k=1+n-1 in reverse pyramid
n=5
for j in range(1,n+1):
    k=1
    for i in range(1,n+1):
        if i>=j:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    k-=2
    for i in range(1,n+1):
        if i+j<n+1:
            print(k,end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
print("_"*50)

#ORD ('A') pattern incrementation order
n=5
for j in range(1,n+1):
    k=ord('A')+j-1
    for i in range(1,n+1):
        if i+j>=n+1:
            print(chr(k),end=" ")
            k-=1
        else:
            print(" ",end=" ")
    k+=2
    for i in range(1,n+1):
        if i<j:
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("_"*50)

#decrementing the values k=ord('A')+n-1 in reverse pyramid
n=5
for j in range(1,n+1):
    k=ord('A')+n-1
    for i in range(1,n+1):
        if i>=j:
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ")
    k-=2
    for i in range(1,n+1):
        if i+j<n+1:
            print(chr(k),end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
print("_"*50)
            
            
