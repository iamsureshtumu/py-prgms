#4 types of Functions

# i) function with no argument & no return value.

def print_n():
    print("Hello World")
print(print_n)
print("Function call yet to hapen")
print_n()
print("function call happened")

print("-"*50)
#example pgrm
#write a program to find the GCD of the given no's
def gcd():  #no arguments
    m,n=1,0
    while n!=0:
        if m>n:
            m=m-n
        else:
            n=m-n #n-=m
    gcd=m               #no return value
    print("gcd is",gcd)
print(gcd)
print("function call yet to happen")
gcd()
print("function call happened")

print("_"*50)


# ii) function with argument and no return value.
 
#actual arguments and formal arguments
#eg 1
def gcd(m,n):  #m,n are called formal arguments
    while n!=0:
        if m>n:
            n=m-n
        else:
            n-=m
        gcd=m
        print("gcd is",gcd)
print(gcd)
print("function call yet to happen")
a,b=10,20
gcd(a,b) #a,b are actual arguments
print("function call happened")

print("_"*50)
#eg 2 the formal arguments (modified) is actual arguments.

def modify(a,b): #with arguments
    print(a,b)
    a+=10
    b+=20
    print(a,b) #with no return value
a=10
b=20
print(a,b)
modify(a,b)
print(a,b)

print("_"*50)
#eg3
def add_element(list_var,value):  #with arguments and no return value
    print(list_var)
    list_var.append(value)
    print(list_var)
a=[1,2,3]
print(a)
add_element(a,4)
print(a)

print("-"*50)
# iii) function with no argument and with return value:

#eg1
def get_element(): #no  arguments
    a,b=10,20
    return a,b   #return value
def add():
    a,b=get_element()
    return a+b
def main():
    sum=add()
    print("The sum is",sum)
    return
main()

print("_"*40)

# iv)function with arguments and with return value:

def get(m,n): #with argument
    if m==0:
        return n #with return value
    if n==0:
        return m
    while n!=0:
        if m>n:
            m-=n
        else:
            n-=m
    return m

#o/p : g=gcd(1,2) 




        
