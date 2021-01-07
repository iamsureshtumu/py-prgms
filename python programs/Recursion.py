#RECURSION
# two cases - case1= Base case, case2=Recursive case

#eg1 factorial using recursion

def factorial(n):     #Base case 
    if(n==0 or n==1):
        return 1       #till here is is base case
    else:
        return n*factorial(n-1)  #recursive case
n=int(input("enter the n value"))
res=factorial(n)
print(res)

print("-"*50)
#eg2
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

print("-"*40)
#eg3

def print_n(n):
    for i in range(n):
        print("Hello World")
def print_n(i,n):
    if i<n:
        print("hello world")
        print(i+1,n)
    else:
        return
    
