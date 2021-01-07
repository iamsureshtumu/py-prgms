#greatest of 5 no's using nested if statement
a,b,c,d,e=10,30,50,20,25
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print("a is greater")
            else:
                print("e is greater")
    else:
        if c>d:
           if c>e:
               print("c is greater")
           else:
               print("e is greater")
        else:
            if d>e:
                print("d is greater")
            else:
                print("e is greater")
else:
    if b>c:
        if b>d:
            if b>e:
                print("b is greater")
            else:
                print("e is greater")
        else:
            if d>e:
                print("d is greater")
            else:
                print("e is greater")
    else:
        if c>d:
            if c>e:
                print("c is greater")
            else:
                print("e is greater")
        else:
            if d>e:
                 print("d is greater")
            else:
                print("e is greater")
                
                
        
                
            
