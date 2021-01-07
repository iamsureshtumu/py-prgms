#varargs : variable arguments
#two types are i) packing ii) unpacking

#i) packing
#eg 1:
def packing_demo(*var):   # star defines 0 to n variables for packing
    print(*var)
    print(var)
    print(type(var))
    print("_"*50)

packing_demo()
packing_demo(10)
packing_demo(1,2)
packing_demo(1,2,3,4)
packing_demo(1,2,3,4,5,6,7,8,9)

print("_"*50)
#eg 2:for dictionary variables

def packing_demo(**var):           # 2 star's is for dictionary values (key:value) in packing
    print(*var)
    print(var)
    print(type(var))
    print("_"*50)

packing_demo()
packing_demo(Name="suresh")
packing_demo(Name="suresh",Age=23)

print("END "*25)
# ii)unpacking

def unpacking_demo(a,b,c):
    print('a:',a)
    print('b:',b)
    print('c:',c)
    print('_'*50)

unpacking_demo(*"hai")
a=[1,2,3]
unpacking_demo(*a)
unpacking_demo(*(1,2,3))
unpacking_demo(*{1,2,3})
unpacking_demo(*[1,2,3])
unpacking_demo(*{'a':1,'b':2,'c':3}) #keys will be unpacked becoz of one star   (*)
unpacking_demo(**{'a':1,'b':2,'c':3})  #values will be unpacked becoz of 2 star's (**)
