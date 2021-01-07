#oops-Behaviours (or) Functionalities (or) Methods- i) OBJECT ii) CLASS iii) STATIC

# i) OBJECT METHOD
class Bank:
    Bank_Name="ICICI"
    No_branches=250
    Rate_of_intrest=14/100
    def __init__(self,Name,Age,Phno,Balance):
        self.Name=Name
        self.Age=Age
        self.Phno=Phno
        self.Balance=Balance
    def deposite(self,amt):
        self.Balance+=amt
        print("amount deposited successfully")
    def withdraw(self,amt):
        if self.Balance>=amt:
            self.Balance-=amt
            print("amount is debited successfully")
            print("please collect cash and card")
        else:
            print("Insufficient Balance")
            print("Balance is:",self.Balance)
    def display_cus(self):
        print("-"*50)
        print("Name of the customer",self.Name)
        print("Age of the customer",self.Age)
        print("Phno of the customer",self.Phno)
        print("Balance of the customer",self.Balance)
        print("-"*50)
leela=Bank("leela",25,9123123123,10000)   #leela deposited 10000rs
lila=Bank("lila",22,9321321321,5000)    #lila deposited 5000rs
leela.display_cus() #it will display the details before withdraw money
leela.withdraw(2000)  #we can also use [ Bank.withdraw(leela,2000) ]
#Bank.withdraw(leela,2000)
Bank.display_cus(leela) #we can also use [ leela.display_cus() ] #it will display the left balance
lila.display_cus()  #it will display the balance before deposite 
lila.deposite(5000) #leela deposited the money
lila.display_cus()  #it will display total money after making deposite


print("_"*50)
# ii) CLASS METHOD

class Bank:
    Bank_Name="ICICI"
    No_branches=250
    Rate_of_intrest=14/100
    def __init__(self,Name,Age,Phno,Balance):
        self.Name=Name
        self.Age=Age
        self.Phno=Phno
        self.Balance=Balance

    @classmethod
    def modify_roi(cls,new):
            cls.Rate_of_intrest=new/100

    @classmethod
    def display(cls):
            print("_"*50)
            print("Name of the Bank is",cls.Bank_Name)
            print("Name of Branches are",cls.No_branches)
            print("current rate of intrest is",cls.Rate_of_intrest)
            print("_"*50)
leela=Bank("leela",25,9123123123,1000)
lila=Bank("lila",22,9321321321,5000)
Bank.display()  #it will display the values
leela.modify_roi(15) #roi will change for leela
leela.display() #it will display the updated the value

#iii) static method:

class Bank:
    BName="ICICI"
    No_of_branches=243
    ROI=14/100
    def __init__(self,Name,Age,Phno,Email,Balance=0,Phno2=None,Email2=None):
        self.Name=Name
        self.Age=Age
        self.Phno=Phno
        self.Email=Email
        self.Balance=Balance
        self.Phno2=Phno2
        self.Email2=Email2
    def withdraw(self):
        amt=self.get_data("withdrawl amount")
        if self.Bal>=amt:
            self.Bal=self.sub(self.Bal,amt)
        else:
            print("Insufficient balance")
            print("Balance is:",self.Bal)
    def deposit(self):
        amt=self.get_data("deposit amount")
        self.Bal=self.add(self.Bal,amt)
    def display(self):
        print("The Name is:",self.Name)
        print("The Age is:",self.Age)
        print("The Phno is:",self.Phno)
        print("The Email is:",self.Email)
        print("The Balance is:",self.Bal)
        if self.Phno2!=None:
            print("alternate Phno2:",self.Phno2)
        if self.Email2!=None:
            print("alternate Email2:",self.Email2)
    @classmethod
    def change_ROI(cls):
        new=cls.get_data("Rate of intrest")
        cls.ROI=new/100
    @classmethod
    def dispcls(cls):
        print("Bank Name is",cls.BName)
        print("No of branches",cls.No_of_branches)
        print("current ROI is",cls.ROI)
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def get_data(data):
        msg="Enter the"+data+"  "
        d=float(input(msg))
        return d

Radha=Bank("Radha",25,9874544545,"radha@gmail.com")
Ravi=Bank("Ravi",22,5847123690,"pichiravi@gmail.com",1000)
Aishwarya=Bank("Aishwarya",46,9632587410,"aishwaryarai@gmail.com",100000,Phno2=6932587410)
akshay=Bank("Akshay",35,2587413690,"kumar.akshay@gmail.com",10000,Email2="neebondha@gmail.com")
            
print(Bank.add(10,20))
print(Radha.add(1000,2000))

#eg2 for for company with employee details by using static method

class company:
    company_Name="QSpiders"
    company_addr="OAR Bangalore"
    company_regno="qsp123"
    website="http://www.qspiders.com"
    No_Employee=0
    def __init__(self,Name,Age,EID,Desig,Phno,Email,Sal,Lev=25,Work_Loc="Bangalore"):
        self.Name=Name
        self.Age=Age
        self.EID=EID
        self.Desig=Desig
        self.Phno=Phno
        self.Email=Email
        self.lev=lev
        self.Work_Loc=Work_Loc
        self.update_no_employee()
    def modify(self,Name=None,Age=None,EID=None,Desig=None,Phno=None,Email=None,Work_Loc=None):
        if Name!=None:
            self.Name=Name
        if age!=None:
            self.age=age
        if EID!=None:
            self.EID=EID
        if Desig!=None:
            self.Desig=Desig
        if Phno!=None:
            self.Phno=Phno
        if Email!=None:
            self.Email=Email
        if lev!=None:
            self.lev=lev
        if Work_Loc!=None:
            self.Work_Loc=Work_Loc
        print("Modification Happened successfully")
    #def display(slef):
     #   for(k,v) in self __dict__.items():
      #      print("The {} is {}".format(k,v))
    def apply_lev(self):
        if self.lev>0:
            self.lev-=1
            print("lev granted")
        else:
            print("no levs")
    @classmethod
    def update_no_employee(cls):
        cls.No_Employee=cls.add(cls.No_Employee,1)
    @staticmethod
    def add(a,b):
        return a+b

Raju=company("Raju",24,1048,"python Developer",7026053650,"suresh@cyware.com",Sal=42500)
ravi=company("Raju",23,1203,"Java Developer",7026053650,"suresht@unisys.com",Sal=30000)
ranga=company("Ranga",23,1049,"US IT RECRUITER",7026053650,"suresht@tellussol.com",Sal=17450)

print("No of Employee's is",company.No_Employee)

        
        
    

 



