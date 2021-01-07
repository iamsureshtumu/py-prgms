#oops-inheritence
#i) object method
class A:
    a=10
class B(A):
    b=20

oa=A()
ob=B()
print(A.a,oa.a) #parent A class and object of a(oa) class
print("Derived Members",B.a,ob.a) #Child B class and object of child  
print("Derived Members",B.b,ob.b) #b value is given so we have to derive the ob value

print("_"*50)

print("modification wrt parent class")
A.a=30
print(A.a,oa.a)
print("Derived Members",B.a,ob.a)
print("Native members",B.b,ob.b)

print("_"*50)

print("modification wrt child class")
B.a=25
print(A.a,oa.a)
print("Derived Members",B.a,ob.a)
print("Native Members",B.b,ob.b)

print("_"*50)

print("modification wrt parent object class")
oa.a=15
print(A.a,oa.a)
print("Derived Members",B.a,ob.a)
print("Native members",B.b,ob.b)

print("_"*50)

print("modification wrt child object class")
ob.a=35
print(A.a,oa.a)
print("Derived members",B.a,oa.a)
print("Native members",B.b,ob.b)

print("_"*50)

print("modification wrt parent class")
A.a=50
print(A.a,oa.a)
print("Derived members",B.a,ob.a)
print("derived members",B.a,ob.b)

print("_"*50)

#eg2 with __init__ function only for class A
class A:
    a=10
    def __init__(self,c):
        print("init method of parent class is invoked")
        self.c=c
class B(A):
    b=20
oA=A(13)
ob=B(14)
print(oA.c)
print(ob.c)

print("_"*50)

#eg3 with __init__ function for class A and class B

class A:
    a=10
    def __init__(self,c):
        print("invoked method of parent class is invoked")
        self.c=c
class B(A):
    b=20
    def __init__(self,d):
        print("invoked method of child class in invoked")
        self.d=d
oa=A(13)
ob=B(14)
print(oa.c)
print(ob.d)

print("_"*50)

#eg4 using DISPLAY function for CLASS A and class B to display.

class A:
    a=10
    def __init__(self,c):
        self.c=c
    def displayA(self):
        print("display is object method of class A")
        print(self)
class B(A):
    b=20
    def __init__(self,d):
        self.d=d
    def displayB(self):
        print("display is object method of class B")
        print(self)
oa=A(13)
ob=B(14)
print("address in oa",oa)
print("address in ob",ob)
oa.displayA()
ob.displayA()
ob.displayB()

print("_"*50)

#eg5 using DISPLAY function for CLASS A and class B to display.(displayA for both class A and class B)

class A:
    a=10
    def __init__(self,c):
        self.c=c
    def displayA(self):
        print("display is object method of class A")
        print(self)
class B(A):
    b=20
    def __init__(self,d):
        self.d=d
    def displayA(self):
        print("display is object method of class B")
        print(self)
oa=A(13)
ob=B(14)
print("address in oa",oa)
print("address in ob",ob)
oa.displayA()
ob.displayA()

print("_"*50)


#ii) classmethod
#adding @classmethod

class A:
    a=10
    def __init__(self,c):
        self.c=c
    def display(self):
        print("displayA is object method of classA")
        print(self)
    @classmethod
    def dispcls(cls):
        print("dispcls of classB")
        print(cls)
class B:
    b=20
    def __init__(self,d):
        self.d=d
    def displayB(self):
        print("display is object of class A")
        print(self)
    @classmethod
    def dispcls(cls):
        print("display of classB")
        print(cls)
    @classmethod
    def dispclsB(cls):
        print("display of classB")
        print(cls)
oa=A(13)
ob=B(14)
print("address in A",A)
print("address in B",B)
oa.dispcls() #cls will take the address of class A
A.dispcls() #clswill take the address of class A
ob.dispcls() #cls will take the address of class B
B.dispcls()  #cls will take the address of class B
ob.dispcls() #cls will take the address as class B
B.dispcls()  #cls will take the address as class B

print("_"*50)

#iii) @static method
#adding @staticmethod

class A:
    a=10
    def __init__(self,c):
        self.c=c
    @staticmethod
    def disp():
        print("hello world in class A")
class B(A):
    b=20
    @staticmethod
    def disp():
        print("Hello world in classB")
    @staticmethod
    def dispB():
        print("Hello bangalore is classB")
oa=A(13)
ob=B(14)
oa.disp()
A.disp()
ob.disp()
B.disp()
ob.dispB()
B.dispB()
    



