# Iterative Python program to count 
# number of digits in a number 

def countdigit(n): 
	count = 0
	while n != 0: 
		n //= 10  #floor div 
		count+= 1
	return count 
#n = 345289467
n=int(input("enter the integer m1"))
print ("Number of digits m1 : ",(countdigit(n))) 




#method 2  in output we have to give countdigits(value)
def countdigits(num):
    count=0
    while num!=0:
        num=num//10
        count+=1
    return count
n=int(input("value m2:"))
print("no of digits m2",(countdigits(n)))



#method 3
def countDigit(n): 
	if n == 0: 
		return 0
	return 1 + countDigit(n // 10) 
	 
n = 345289467
print ("Number of digits m3: % d"%(countDigit(n))) 



#method 4
# Log based Python program to count number of digits in a number 
# function to import ceil and log 
import math 

def countDigit(n): 
	return math.floor(math.log(n, 10)+1)

n = 345289467
print ("Number of digits m4 : % d"%(countDigit(n)))


#method 5

n=int(input("Enter number m5:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are m5:",count)









