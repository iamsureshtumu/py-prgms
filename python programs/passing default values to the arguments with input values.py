#passing default values to the arguments with input values

def backed(Name,Email,Phno,Email2=None,Phno2=None):
    print("Name is",Name)
    print("Email is",Email)
    print("Phno is",Phno)
    if Email2!=None:
        print("Alternate Email ID is",Email2)
    if Phno2!=None:
        print("Alternate Phno is",Phno)
def add(a,b,c=0,d=0,e=0):
    return a+b+c+d+e
