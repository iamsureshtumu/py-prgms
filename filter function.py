#filter program which removes the unwanted values that are present in the collection by using a method returning boolean value
def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
        return True
var=filter(isprime,list(range(2,50)))
print(list(var))
