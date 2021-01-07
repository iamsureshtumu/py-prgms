#1 incrementing the values with k=1+j-1
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
 
#2 decrementing the values k=1+n-1
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

#3 decrementing the values k=1+n-1 in reverse pyramid
n=5
for j in range(1,n+1):
    k=1+n-1
    for i in range(1,n+1):
        if i>=j:
            print(k,end=" ")
            k-=1
        else:
            print(" ",end=" ")
    k+=2
    for i in range(1,n+1):
        if i+j<n+1:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("_"*50)

#4 decrementing the values k=1 in reverse pyramid
n=5
for j in range(1,n+1):
    k=1+n-1
    for i in range(1,n+1):
        if i>=j:
            print(k,end=" ")
            k-=1
        else:
            print(" ",end=" ")
    k+=2
    for i in range(1,n+1):
        if i+j<n+1:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("_"*50)

#5 ORD ('A') pattern incrementation order k=ord('A')+j-1
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

#6 decrementing the values k=ord('A')+n-1 in reverse pyramid
n=5
for j in range(1,n+1):
    k=ord('A')+n-1
    for i in range(1,n+1):
        if i>=j:
            print(chr(k),end=" ")
            k-=1
        else:
            print(" ",end=" ")
    k+=2
    for i in range(1,n+1):
        if i+j<n+1:
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ")
    print()
print("_"*50)


#7 decrementing the values k=1+n-1
n=5
for j in range(1,n+1):
    k=1+n-1
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


#8 incrementing  the values k=1+n-1
n=5
for j in range(1,n+1):
    k=1
    for i in range(1,n+1):
        if i+j>n+1:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    
    for i in range(1,n+1):
        if i<=j:
            print(k,end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
print("_"*50)  
