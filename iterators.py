# prgm to create the series if factorial numbers from n to n

def fact(n):
    if n in[0,1]:
        return 1
    return n*fact(n-1)

class fact_series:
    def __init__(self,m,n):
        self.m=m
        self.n=n

    def __iter__(self):
        self.i=self.m
        return self
    def __next__(self):
        if self.i<self.n:
            res=self.fact(self.i)
            self.i+=1
            return res
        raise stopIteration
    def fact(self,n):
        if n in[0,1]:
            return 1
        return n*self.fact(n-1)

oa=fact_series(0,5)
i=iter(oa)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
