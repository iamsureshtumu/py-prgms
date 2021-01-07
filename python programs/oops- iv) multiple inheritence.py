#oops- iv) multiple inheritence
#eg1  class A and class B will derived from right to left

class A:
    a=10
    b=30
    def __init__(self):
        print("init of class A")

class B:
    b=20
    def __init__(self):
        print("init of class B")

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("init of class C")

oa=A()
ob=B()
oc=C()
print(A.a,B.b,C.a,C.b)

print("_"*50)
#eg2 reverse the  C(B,A): it will display the A value first and later B will come first

class A:
    a=10
    b=30
    def __init__(self):
        print("init of class A")

class B:
    b=20
    def __init__(self):
        print("init of class B")
class C(B,A):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Init of class C")
oa=A()
ob=B()
oc=C()
print(A.a,B.b,C.a,C.b)

print("*"*50)
# eg3 using object method display function with dispcls and @CLASSMETHOD

class A:
    a=10
    c=35
    def __init__(self,a1):
        print("Init of class A is invoked")
        self.a1=a1
    def display(self):
        print("display method of class A")
        print(self.a1)
    @classmethod
    def dispcls(cls):
        print("control came to display class of class A")
        print(cls.a,cls.c)
class B:
    a=20
    b=30
    def __init__(self,b1):
        print("init of class B is invoked")
        self.b1=b1
    def display(self):
        print("display method of class A")
        print(self.b1)
    @classmethod
    def dispcls(cls):
        print("control came to display class of class B")
        print(cls.a,cls.b)
class C(A,B):
    d=40
    def __init__(self,a1,b1,c1):
        print("Init of class C is invoked")
        self.c1=c1
        A.__init__(self,a1)
        B.__init__(self,b1)
    def display(self):
        print("display method of class C")
        print(self.c1)
    @classmethod
    def dispcls(cls):
        print("control came to display class of calss C")
        print(cls.a,cls.b,cls.c,cls.d)

oa=A(5)
ob=B(7)
oc=C(13,15,17)
print("_"*50)
oa.display()
ob.display()
oc.display()
oa.dispcls()
ob.dispcls()
oc.dispcls()

print("end "*30)

#v) Hybrid inheritence:
class A:
    a=10
class B:
    a=14
class C:
    a=15
class D(B,C):
    pass

oa=A()
ob=B()
oc=C()
od=D()
print(A.a,B.a,C.a,D.a)
print(oa.a,ob.a,oc.a,od.a)
print("_"*50)
A.a=13
print(A.a,B.a,C.a,D.a)
print(oa.a,ob.a,oc.a,od.a)

 




        

