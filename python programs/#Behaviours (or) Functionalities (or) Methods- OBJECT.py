#Behaviours (or) Functionalities (or) Methods- i) OBJECT ii) CLASS iii) STATIC

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



