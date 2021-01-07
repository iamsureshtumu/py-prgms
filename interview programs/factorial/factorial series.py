# Python code to demonstrate naive method 
# to compute factorial
n=int(input("Enter the integer: ")) #n=value
fact = 1

for i in range(1,n+1): 
	fact = fact * i 
	
print ("The factorial value of given integer is : ",end="") 
print (fact) 
