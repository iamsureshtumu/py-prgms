#simple calculator by using python
def get_elements():
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    return a,b
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
        if ch==2:
            result=sub()
        if ch==3:
            result=mul()
        if ch==4:
            result=div()
        if ch==5:
            result=mod()
        if ch==6:
            break
        else:
            print("invalid input")
        continue
    print("result is",result)
print()

