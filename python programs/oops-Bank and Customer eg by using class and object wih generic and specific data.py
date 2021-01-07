#bank and customers link with generic data and specific data.
class Bank:
    Bank_Name="ICICI"
    No_branches=243
Cus1=Bank()
Cus2=Bank()
print(Bank.Bank_Name,Bank.No_branches)
print(Cus1.Bank_Name,Cus1.No_branches)
print(Cus2.Bank_Name,Cus2.No_branches)

print("-"*50)

#making some modifications wrt to CLASS for the change branch code
class Bank:
    Bank_Name="ICICI"
    No_branches=243
Cus1=Bank()
Cus2=Bank()
print(Bank.Bank_Name,Bank.No_branches)
print(Cus1.Bank_Name,Cus1.No_branches)
print(Cus2.Bank_Name,Cus2.No_branches)
print("modification wrt classname")
Bank.No_branches=300
print(Bank.Bank_Name,Bank.No_branches)
print(Cus1.Bank_Name,Cus1.No_branches)
print(Cus1.Bank_Name,Cus1.No_branches)

print("-"*50)
#making some modifications wrt to OBJECT for change of cus1 bank name.
class Bank:
    Bank_Name="ICICI"
    No_branches=243
Cus1=Bank()
Cus2=Bank()
print(Bank.Bank_Name,Bank.No_branches)
print(Cus1.Bank_Name,Bank.No_branches)
print(Cus2.Bank_Name,Bank.No_branches)
print("modifications wrt object")
Cus1.Bank_Name="Axis"
print(Bank.Bank_Name,Bank.No_branches)
print(Cus1.Bank_Name,Bank.No_branches)
print(Cus2.Bank_Name,Bank.No_branches)

print("-"*50)
#making some modifications wrt to cus1 bank of bank and CLASSname that change of entire bank name.
class Bank:
    Bank_Name="ICICI"
    No_branches=243
Cus1=Bank()
Cus2=Bank()
print(Bank.Bank_Name,Bank.No_branches)
print(Cus1.Bank_Name,Bank.No_branches)    
print(Cus2.Bank_Name,Bank.No_branches)
print("modifications wrt object")
Cus1.Bank_Name="Axis"
print(Bank.Bank_Name,Bank.No_branches)
print(Cus1.Bank_Name,Bank.No_branches)    
print(Cus2.Bank_Name,Bank.No_branches)
print("modifications wrt class")
Bank.Bank_Name="Baroda"
print(Bank.Bank_Name,Bank.No_branches)
print(Cus1.Bank_Name,Bank.No_branches)    
print(Cus2.Bank_Name,Bank.No_branches)

print("-"*50)
#making some modification for object that change of Cus2 and Cus1 change of bank
class Bank:
    Bank_Name="ICICI"
    No_branches=243
Cus1=Bank()
Cus2=Bank()
print(Bank.Bank_Name,Bank.No_branches)
print(Cus1.Bank_Name,Bank.No_branches)    
print(Cus2.Bank_Name,Bank.No_branches)
print("modifications wrt object")
Cus2.Bank_Name="Axis"
print(Bank.Bank_Name,Bank.No_branches)
print(Cus1.Bank_Name,Bank.No_branches)    
print(Cus2.Bank_Name,Bank.No_branches)
print("modifications wrt object")
Cus1.Bank_Name="Baroda"
print(Bank.Bank_Name,Bank.No_branches)
print(Cus1.Bank_Name,Bank.No_branches)    
print(Cus2.Bank_Name,Bank.No_branches)



    



