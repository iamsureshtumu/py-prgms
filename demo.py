#to generate first n numbers

def firstn(num):
    n=1
    while n<=num:
        yield n
        n=n+1
for x in firstn(10):
    print(x)


print('-'*50)

# to generate the series of EVEN numbers from 0 to n

def Even_series(n):
    i=0
    while i<n:
        res=i
        i+=2
        yield res
        
for x in Even_series(10):
    print(x)


print('-'*50)

#generate the series if fibonace numbers

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

n=10
print(fibo(n))
