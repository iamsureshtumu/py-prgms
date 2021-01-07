# Iterative Python program to count 
# number of digits in a number 

#method 1
def countdigits(n):
        count=0
        while(n>0):
                count+=1   #count=count+1
                n=n//10
        return count
n=int(input("Enter number:"))
print("The number of digits in the number are:",(countdigits(n)))


#Method 2
n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)





