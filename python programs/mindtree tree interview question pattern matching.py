#write the python program by using given pattern and to get out put (mindtree interview question)

# 1     k value
# 3 2      L value
# 4 5 6    K value
# 10 9 8 7  L value
# 11 12 13 14 15  K value

n=5
k=ord('A')
for j in range(1,n+1):
    l=k+j-1
    for i in range(1,n+1):
        if i<=j:
            if j%2!=0:
                print(chr(k),end=" ")
            else:
                print(chr(l),end=" ")
                l-=1
            k+=1
        else:
            print(" ",end=" ")
    print()
            
