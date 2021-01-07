# Python program to display all the prime numbers within an interval

start = 50
end = 100

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

