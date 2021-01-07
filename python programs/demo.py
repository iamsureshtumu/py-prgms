for row in range(7):
    for col in range(5):
        if row==0 or col==0 or row==6 or ((row==3 or row==4 or row==5) and col==4) or (row==3 and col==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
            
        
