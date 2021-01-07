#functions, arguments, return, function call
#eg1 function to add two numbers

#user defined function
def add(a,b):   #def=function defination  # a and b are arguments/parameters
    sum=a+b
    return sum #return statement
#from here it starts actual program
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
res=add(a,b) #function call
print("result=",res)
