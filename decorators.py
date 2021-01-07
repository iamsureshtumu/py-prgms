#decorators

def outer(func):
    print("control entered into outer function")
    print("func")
    print('-'*50)

    def inner(*args,**kwargs):
        print("control entered into function")
        func(*args,**kwargs) #function call
        print("control is leaving from inner function")
        print('-'*50)
    print("control is going out of outer function")
    return inner

@outer
def sample():
    print("-"*50)
    print("control entered into sample")
    print("control is leaving from sample")
    print("-"*50)
