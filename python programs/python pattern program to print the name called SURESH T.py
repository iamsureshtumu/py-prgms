#program to print the name called SURESH T
for row in range(7):
    for col in range(5):
        if (row==0 and col!=0) or (row==3 and (col!=0 and col!=4)) or (row==6 and col!=4) or (col==0 and (row!=0 and row!=3 and row!=4 and row!=5)) \
        or(col==4 and(row!=1 and row!=2 and row!=3 and row!=6)):
            print("*",end= " ")
        else:
            print(" ",end=" ")
    print()
print("S"*50)
for row in range(7):
    for col in range(5):
        if (col==0 and row!=6) or (row==6 and (col!=0 and col!=4)) or (col==4 and row!=6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("U"*50)
for row in range(7):
    for col in range(5):
        if col==0 or (row==0 and col!=4) or (col==4 and(row!=0 and row!=3)) or (row==3 and col!=4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("R"*50)
for row in range(7):
    for col in range(5):
        if col==0 or (row==0 or (row==3 and col!=4) or row==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("E"*50)
for row in range(7):
    for col in range(5):
        if (row==0 and col!=0) or (row==3 and (col!=0 and col!=4)) or (row==6 and col!=4) or (col==0 and (row!=0 and row!=3 and row!=4 and row!=5)) \
        or(col==4 and(row!=1 and row!=2 and row!=3 and row!=6)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("S"*50)
for row in range(7):
    for col in range(5):
        if col==0 or col==4 or row==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("H"*50)
for row in range(7):
    for col in range(5):
        if row==6 and col==2:
            print("*",end= " ")
        else:
            print(" ",end=" ")
    print()
print("."*50)
for row in range(7):
    for col in range(5):
        if row==0 or col==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("T"*50)

            



        
