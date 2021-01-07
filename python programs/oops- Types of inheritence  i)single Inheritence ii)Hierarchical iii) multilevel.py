#OOPS - Types of Inheritence

#i) Single Inheritence

class  A:     #1st argument A
    a1=10     #class value
    b1=20     #class value
    def __init__(self,a,b):   #declaration of self a,b
        self.a=a  #self declaration of a 
        self.b=b  #self declaration of b
    def display(self): #display function
        print("a :",self.a)   #printing the value of a 
        print("b :",self.b)   #printing the value of b
    @classmethod     #classmethod declaration
    def displayc(cls):    #display the class values
        print("members of class A",cls.a1,cls.b1)  #printing the values of class a1 and b1
class B(A):  #class B which is derived from calss A
    c1=10    #class value
    d1=20     #class value
    def __init__(self,a,b,c,d): #init function declaration with class A and class B values
        super().__init__(a,b)   #super class will take the values from CLASS A
        self.c=c    #display the c values
        self.d=d    #display the d values
    def display(self):  #display function
        super().display()  #it will display the values of CLASS A
        print("c :",self.c)   #printing the c values
        print("d :",self.d)   #printing the d values
    @classmethod     #clasmethod enters
    def displayc(cls):  #display the class values
        A.displayc()     #class A values displays
        print("members of Class B",cls.c1,cls.d1) #printing the values of c1 and d1
oa=A(3,4)  
ob=B(9,8,7,6)
oa.display()
print("_"*50)
oa.displayc()
print("-"*50)
ob.display()
print("-"*50)
ob.displayc()


print("ii "*30)

#ii) Hierarchical Inheritence
class A:
    a1=10
    b1=20
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("a :",self.a)
        print("b :",self.b)
    @classmethod
    def displayc(cls):
        print("members of Class A",cls.a1,cls.b1)
class B(A):
    c1=11
    d1=22
    def __init__(self,a,b,c,d):
        super().__init__(a,b)
        self.c=c
        self.d=d
    def display(self):
        super().display()
        print("c :",self.c)
        print("d :",self.d)
    @classmethod
    def displayc(cls):
        A.displayc()
        print("members of class B",cls.c1,cls.d1)
class C(A):
    e1=111
    f1=222
    def __init__(self,a,b,e,f):
        super().__init__(a,b)
        self.e=e
        self.f=f
    def display(self):
        super().display()
        print("e :",self.e)
        print("f :",self.f)
    @classmethod
    def displayc(cls):
        A.displayc()
        print("members of class C ",cls.e1,cls.f1)
oa=A(3,4)
ob=B(9,8,7,6)
oc=C(50,40,30,35)
oa.display()
print("_"*50)
oa.displayc()
print("_"*50)
ob.display()
print("_"*50)
ob.displayc()
print("_"*50)
oc.display()
print("_"*50)
oc.displayc()

print("iii "*30)
# iii) multilevel Inheritence
#eg1
class A:
    a=10
    def __init__(self,a):
        self.a=a
class B(A):
    b=20
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
class C(B):
    c=30
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
oa=A(1)
print("_"*50)
ob=B(2,3)
print("-"*50)
oc=C(4,5,6)
print("_"*50)
print(oa.__dict__)
print("_"*50)
print(ob.__dict__)
print("_"*50)
print(oc.__dict__)

print("iii "*20)
#eg2 with @class method

class A:
    a1=10
    def __init__(self,a):
        self.a=a
    def display(self):
        print("a :",self.a)
    @classmethod
    def displayc(cls):
        print("members of class A",cls.a1)
class B(A):
    b1=20
    def __init__(self,a,b):
        super().__init__(a)
        self.b=b
    def display(self):                       
        super().display() #A.display(self) we can also use this  
        print("b :",self.b)
    @classmethod
    def displayc(cls):
        A.displayc()
        print("Members of class B",cls.b1)
class C(B):
    c1=30
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def display(self):
        super().display()
        print("c :",self.c)
    @classmethod
    def displayc(cls):
        B.displayc()
        
        print("members of class C",cls.c1)

oa=A(1)
ob=B(2,3)
oc=C(4,5,6)
oa.display()
print("_"*50)
oa.displayc()
print("_"*50)
ob.display()
print("_"*50)
ob.displayc()
print("_"*50)
oc.display()
print("_"*50)
oc.displayc()



    
    
    

    
    

        
    

