#oops-constructor chaining

#eg1 of Bank attributes copying to Bank2 and updating some features
class Bank:
    def __init__(self,Name,Age,Phno):
        self.Name=Name
        self.Age=Age
        self.Phno=Phno
class Bank2(Bank):       #copying the attributes from the Bank 1
    def __init__(self,Name,Age,Phno,Aadhar): #adding aadhar
        self.Aadhar=Aadhar  #update the aadhar
        super().__init__(Name,Age,Phno)
    def update_Aadhar(self,Aadhar):   #attribute for upadte aadhar
        self.Aadhar=Aadhar
Ria=Bank("Ria",24,987654)   #bank 1 which aadhar is not updated
Tarun=Bank2("Tarun",34,8348643,232487) #bank2 which everything is updated
print(Ria.__dict__) #printing the attributes of ria in the form of DICTIONARY 
Bank2.update_Aadhar(Ria,567894567)  #updating the Ria aadhar in Bank2
print(Ria.__dict__) #it will display the details of Ria in the form of DICTIONARY
print(Tarun.__dict__) #it will display the details of tarun in the form of DICTIONARY

print("_"*50)

#eg2 to display the values by using DISPLAY function
class Bank:   #this is Bank 1
    def __init__(self,Name,Age,Phno): #having three attributes
        self.Name=Name
        self.Age=Age
        self.Phno=Phno

    def display(self):                               #it will display the values
        print("Name is",self.Name)                   #printing the values according to the attributes given
        print("Age is",self.Age)                      #printing the values according to the attributes given
        print("Phno is",self.Phno)                    #printing the values according to the attributes given
class Bank2(Bank):                                    #this is Bank 2 and which copies the attributes from bank one
    def __init__(self,Name,Age,Phno,Aadhar):                 #adding extra feature called Aadhar
        self.Aadhar=Aadhar                                #updatation of Aadhar 
        super().__init__(Name,Age,Phno)               #calling function from BANK 1 to BANK2 and it will use the atributes of values from BANK 1
    def update_Aadhar(self,Aadhar):                     #defines updation of aadhar
        self.Aadhar=Aadhar 
    def display(self):                             #it is used to display the attributes of BANK 
        Bank.display(self)                                 #Display declaration
        print("Aadhar no is",self.Aadhar)         #aadhar declaration
Ria=Bank("Ria",34,3562)  #values of Ria without aadhar from Bank 1
Tarun=Bank2("Tarun",34,3465872,437832)   #values of tarun from Bank 2 with aadhar value upadated
Ria.display()        #displays the values
print("_"*50)  
Bank2.update_Aadhar(Ria,478658292)           #update the values of Ria
Bank2.display(Ria)               #display the values of Ria from BANK2
print("_"*50)
Tarun.display()           #displays the values


print("*"*50)

#OOPS- Method Chaining with @CLASSMETHOD

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
        print("members of class A",cls.a1,cls.b1)
class B(A):
    c1=10
    d1=20
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

oa=A(3,4)
ob=B(9,8,7,6)
oa.display()
print("_"*50)
oa.displayc()
print("_"*50)
ob.display()
print("_"*50)
ob.displayc()

    
