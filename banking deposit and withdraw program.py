#Banking

class Bank:
    Bank_Name="ICICI"
    No_branches=243
    Rate_of_inrest=14/100
    def __init__(self,Name,Age,Phno,Balance):
        self.Name=Name
        self.Age=Age
        self.Phno=Phno
        self.Balance=Balance
    def deposit(self,amt):
        self.Balance+=amt
        print("Amount of ",amt," deposited successfully")
    def withdraw(self,amt):
        if self.Balance>=amt:
            self.Balance-=amt
            print("amt of",amt,"is successfull debited")
            print("please collect cash and card")
        else:
            print("insufficient balance")
            print("Balance is",self.Balance)
    def display_cus(self):
        print("*"*50)
        print("Name of the customer: ",self.Name)
        print("Age of the customer: ",self.Age)
        print("Phno of the customer: ",self.Phno)
        print("Balance of the customer: ",self.Balance)
        print("*"*50)
        

Reeta=Bank("Reeta",98,7852143690,7000000)
Bata=Bank("Bata",12,7896541230,73690)
Bank.display_cus(Reeta)
Reeta.withdraw(20000)
Bank.display_cus(Reeta)
Bata.display_cus()
Bata.deposit(5000)
Bata.display_cus()
