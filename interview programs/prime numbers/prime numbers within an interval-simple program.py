# Python program to display all the prime numbers within an interval

# change the values of lower and upper for a different result
start = 50
end = 100

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

print("Prime numbers between",start,"and",end,"are:")

for num in range(start,end + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)


print("--------------------------------------------------------------")

start=11
end=25
print("Prime numbers between",start,"and",end,"are:")
for val in range(start,end+1):
    if val>1:
        for n in range(2,val):
            if (val%n)==0:
                break
        else:
             print(val)
