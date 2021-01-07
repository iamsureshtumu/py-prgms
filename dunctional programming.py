#FUNCTIONAL PROGRAMMING: it is a phenomenon of the function is passing (or) the address of the function as an argument by unsing that address we are going to do functioncall
def add(a,b):
    return a+b
def f(func,a,b):
    res=func(a,b)
    print(res)
    f(add,10,13)

def function1():
    print("control entered into function 1")
def function2():
    print("control entered into function 2")
    func()
function2(function1)
