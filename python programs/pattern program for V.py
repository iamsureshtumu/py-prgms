for row in range(4):
    for col in range(7):
        if row==col or (row==2 and col==4) or (row==1 and col==5) or (row==0 and col==6):
            print("*",end=" ")
        else:
            print(end=" ")
    print()
print("V"*50)
