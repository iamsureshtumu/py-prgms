#writing a program to find the greatest of n numbers
def input_to_list(n):
    a=[]
    for i in range(n):
        value=int(input("enter the values "))
        a.append(value)
    return a
        
def greater(n):
    n=int(input("enter the no. of elements "))
    data= input_to_list(n)
    great=data[0]
    for i in range(1,n):
        if data[i]<great:
            great=data[i]
    return great
        
