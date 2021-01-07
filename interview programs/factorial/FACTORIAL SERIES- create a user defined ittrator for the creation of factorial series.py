 #create userdefined itterator for the creation of factorial series
def fact(n):
    if n in [0,1]:
        return 1
    return n*fact(n-1)

class Fact_series:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        self.i=0
        return self
    def __next__(self):
        if self.i<self.n:
            res=fact(self.i)
            self.i+=1
            return res
        raise StopIteration

var=Fact_series(10)
print(list(var))
