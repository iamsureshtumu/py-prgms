#check the program... the given no is even (or) not. if is even, then check that no. is divisible then remove 5 from it.
#(continue) if not add 5 to it & show weather it is divisible by 6 or not& display the value.

value=16
if value%2==0:
    if value%6==0:
        print("value is divisible by 6")
        value-=5
    else:
        print("value is not not divisible")
        value+=5
    print(value)
        
