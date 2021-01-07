#series of prime numbers by using generators
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True

def prime_series(m,n):
    i=m
    while i<n:
        if isprime(i)==True:
            yield i
        i+=1

def prime_n(n):
    i=2
    count=0
    while count<n:
        if isprime(i)==True:
            count+=1
            yield i
        i+=1
var=prime_n(20)
for i in var:
    print(i,end=" ")
