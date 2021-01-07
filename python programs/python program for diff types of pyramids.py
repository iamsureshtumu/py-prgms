# python program for pattern matching for PYRAMID and HEART shape by using row and col

for row in range(9):
    for col in range(7):
        if row==8 or (row==7 and(col!=0 and col!=6)) or ((row==6 and col==2)or (row==6 and col==3)or(row==6 and col==4)) or (row==5 and col==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("PYRAMID_"*10)
#heart shape
for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):  #1st condition at row 0 col 0,3,6 we don't want star, so we took condition like col%3!=0 
            print("*",end=" ") #for 2nd condition col%3=0 is true, when col value is 0 3 6
        else:  #3rd condition row-col==2 and 4th condition row+col==8
            print(" ",end=" ")
    print()
print("HEART_"*10)
#daimond shape
for row in range(5): #for more clarity please draw a picture of 5 rows and 5 columns
    for col in range(5):
        if row+col==2 or col-row==2 or row-col==2 or row+col==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("DAIMOND_"*10)
#pyramid pattern by using logic
n=7
for j in range(1,n+1):
    for i in range(1,n+1):
        if i+j>=n+1 and i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("pyramid_"*10)
#pyramid in reverse by using logic
n=7
for j in range(1,n+1):
    for i in range(1,n+1):
        if i+j<=n+1 and i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("reverse_pyramid_"*5)
#pyramid towards left side using small logic
n=7
for j in range(1,n+1):
    for i in range(1,n+1):
        if i+j<=n+1 and i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("left side"*5)
#pyramid towards right side using small logic
n=7
for j in range(1,n+1):
    for i in range(1,n+1):
        if i+j>=n+1 and i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("right side"*5)

#patrern in dif
n=7
for j in range(1,n+1):
    for i in range(1,n+1):
        if i+j<=n+1 and i<=j or i+j>=n+1 and i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("_"*30)
            
 #pyramid by usind numbers
n=5
for j in range(1,n+1):
    k=1           #k defines the numbers
    for i in range(1,n+1):
        if i+j>=n+1:
            print(k,end=" ")
            k+=1
        else:
            print(" ",end=" ")
    k-=2
    for i in range(1,n+1):
        if i<j:          #normally we will mention i<=j. but, here = is not require to get the values because we will get dif values
            print(k,end=" ") 
            k-=1
        else:
            print(" ",end=" ")
    print()
print("pyramid"*10)

#pyramid by using alphabets
for j in range(1,n+1):
    k=ord('A')
    for i in range(1,n+1):
        if i+j>=n+1:
            print(chr(k),end=" ")
            k+=1
        else:
            print(" ",end=" ")
    k-=2
    for i in range(1,n+1):
        if i<j:
            print(chr(k),end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
print("reverse_pyramid"*4)
            
            
