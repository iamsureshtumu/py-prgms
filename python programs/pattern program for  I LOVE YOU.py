#pattern program for I LOVE YOU by using rows and columns for each and every single alphabet
for row in range(7):
    for col in range(5):
        if col==2 or (row==0 or row==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("I"*50)
for row in range(7):
    for col in range(5):
        if col==0 or row==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("L"*50)
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and(row!=0 and row!=6)) or ((row==0 or row==6) and (col!=0 and col!=4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("O"*50)
for row in range(4):
    for col in range(7):
        if row==col or (row==2 and col==4) or (row==1 and col==5) or (row==0 and col==6):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
print("V"*50)
for row in range(7):
    for col in range(5):
        if col==0 or (row==0 or (row==3 and col!=4) or row==6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("E"*50)
for row in range(5):
    for col in range(5):
        if (col==2 and row>1) or (col==row and col<2) or (row==0 and col==4) or (row==1 and col==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("Y"*50)
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and(row!=0 and row!=6)) or ((row==0 or row==6) and (col!=0 and col!=4)):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("O"*50)
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=6) or (row==6 and (col!=0 and col!=4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("U"*50)

    


            
    


            
        
