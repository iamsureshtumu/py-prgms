#Break statement

for i in "hello world":
    if i==" ":
        break  #in the break statement it will print only 'hello'. after hello it goes to break statement.
    print(i)
    
print("_"*50)

i=0
while i<20:
    if i==10: 
        break # it will print till 0 to 9 values because i==10. after that it will go to break statement.
    print(i)
    i+=1
    
print("_"*30)

key='z'
flag=0
for i in{'a':1,'b':2,'c':3,'d':4}:
    if i==key:
        flag=1
        break
if flag==1:
    print("element found")
else:
    print("element not found")

print("_"*50)
# ii) continue
#eg1
for i in"hello world":
    if i==' ':
        continue
    print(i)
print("-"*50)
#eg2
for i in range(30):
    if i%5==0:
        continue
    print(i)

print("-"*50)
#pass statement
#eg1
for i in"hello world":
    pass
while True:
    pass
if condition:
    pass
elif condition:
    pass
else:
    pass



