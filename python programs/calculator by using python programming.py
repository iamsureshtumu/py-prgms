#simple calculator by using python
def get_elements():
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    return a,b
def add():
    a,b=get_elements()
    return a+b
def sub():
    a,b=get_elements()
    return a-b
def mul():
    a,b=get_elements()
    return a*b
def div():
    a,b=get_elements()
    return a/b
def mod():
    a,b=get_elements()
    return a%b
def calc():
    while(True):
        print("choose the option to perform")
        ch=int(input(""" press 1 to add
                         press 2 to sub
                         press 3 to mul
                         press 4 to div
                         press 5 to mod
                         press 6 to exit """))
        if ch==1:
            result=add()
        elif ch==2:
            result=sub()
        elif ch==3:
            result=mul()
        elif ch==4:
            result=div()
        elif ch==5:
            result=mod()
        elif ch==6:
            break
        else:
            print("invalid input")
            continue
        print("result is",result)

