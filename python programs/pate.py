#write the python program by using given pattern and to get output? (mindtree interview question)
#1 these is 
#3 2
#4 5 6
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
########################################
print("_"*30)
#########################################
# if it pattern was in alphabet

# A
# C B
# D E F
# J I H G
# K L M N O

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
######################################    
print("_"*30)
######################################

