#swap two numbers without 3rd variable
def swap(a,b):
    a,b=b,a
    return(a,b)
a,b=10,20
print(a,b)
a,b=swap(a,b)
print(a,b)
print("*"*50)

#swap 4 numbers 
def swap(a,b,c,d):
    a,b,c,d=d,c,b,a
    return a,b,c,d
a,b,c,d=10,20,30,40
print(a,b,c,d)
a,b,c,d=swap(a,b,c,d)
print(a,b,c,d)

