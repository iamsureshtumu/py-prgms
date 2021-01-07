#Python program to check whether a number is Prime or not

# Python program to check if
# given number is prime or not

def prime(n):
    count = 0
    for i in range(1, (n+1)): 
         if n % i == 0: 
             count += 1
    if count > 2:
        print("Not a prime")
    else:
        print("A prime")

