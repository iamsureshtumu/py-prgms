#class and object with specific data.

class Bank:
    Bank_Name="ICICI"
    No_branches=243
    def __init__(self):
        print(self)
        self.c=10
        print("conrol come to __init__")
Cus1=Bank()
print(Cus1)
Cus2=Bank()
print(Cus2)

print("_"*50)
#specific data with customer name

class Bank:
    Bank_Name="ICICI"
    No_branches=243
    def __init__(self):
        print(self)
        self.c=10
        print("control come to __init__")
Reeta=Bank()
print(Reeta)
print("_"*50)
Bata=Bank()
print(Bata)
print("_"*50)
print(dir(Bank))
print("_"*50)
print(dir(Reeta))
print("_"*50)
print(dir(Bata))
print(Reeta.c,Bata.c)

print("_"*50)
#with some changes add specific data of customers along with full details.

class Bank:
    Bank_Name="ICICI"
    No_branches=243
    def __init__(self,Name,Phno,Email,Phno2=None,Email2=None):
        self.Name=Name
        self.Phno=Phno
        self.Email=Email
        self.Phno2=Phno2
        self.Email2=Email2
        
Reeta=Bank("Reeta",9123123123,"reeta@gmail.com",9685741230)     #Reeta doesn't have any alterate email
#print(Reeta)  #if we print(Reeta) then it will print address like 0x12331
Bata=Bank("Bata",9321321321,"Bata@gamil.com",Email2="bata2@gmail.com") #Bata have alternate email
#print(Bata)
Seetha=Bank("Seetha",9010101010,"seetha@gmai.com",9632587410,"seetha2@gmail.com") #seetha have both the alternate email and phno
#print(Seetha)

print("Details of Reeta")
print("Name is",Reeta.Name)
print("Phno is",Reeta.Phno)
print("Email is",Reeta.Email)
if Reeta.Phno2!=None:
    print("Alternate Number is",Reeta.Phno2)
if Reeta.Email2!=None:
    print("Alternate Email is",Reeta.Email2)
    
print("-"*50)

print("Details of Bata")
print("Name is",Bata.Name)
print("Phno is",Bata.Phno)
print("Email is",Bata.Email)
if Bata.Phno2!=None:
    print("Alternate Number is",Bata.Phno2)
if Bata.Email2!=None:
    print("Alternate Email is",Bata.Email2)
    
print("_"*50)

print("Details of Seetha")
print("Name is",Seetha.Name)
print("Phno is",Seetha.Phno)
print("Email is",Seetha.Email)
if Seetha.Phno2!=None:
    print("Alternate Number is",Seetha.Phno2)
if Seetha.Email2!=None:
    print("Alternate Email is",Seetha.Email2)
