for row in range(7):
    for col in range(5):
        if col==4 or ((row==0 or row==6)):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
print("_"*50)
for row in range(7):
    for col in range(5):
        if col==0 or row==6:
            print("*",end=" ")
        else:
            print(end=" ")
    print()
print("_"*50)
for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or row==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("_"*50)
    


        
