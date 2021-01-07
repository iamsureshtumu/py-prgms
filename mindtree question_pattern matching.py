#mindtree question for pattern matching

#print like this

# 1
# 3 2
# 4 5 6
#10 9 8 7
#11 12 13 14 15

n=5
k=1

for j in range(1,n+1):
    l=k+j-1
    for i in range(1,n+1):
        if i<=j:
            if j%2!=0:
                print(k,end=" ")
            else:
                print(l,end=" ")
                l-=1
            k+=1
        else:
            print(" ",end=" ")
print()
