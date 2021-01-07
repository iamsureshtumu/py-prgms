#i) while loop

#Eg1 write a program to check whether the given no. is even or not. if it is even then remove the no.of 2's present inside it and print the no which doesn't consists of
#any 2's and also i wanted to remove count the no of 2's

num=5041    #change the num and try to give odd value
count=0
if num%2==0:
    while num>=2:
        num-=2
        count+=1
print(num)
print("the no of 2's removed is",count)

print("_"*50)

#Eg2 write a program to print "hello world" statement for 10 times.

a="hello world"
count=0
while count<10:
    print(a)
    count+=1

print("_"*50)

#for loop

for i in "hello":
    print('i',i)
print("_"*50)
for i in [1,2,3,4,5]:
    print('i',i)
print("_"*50)
for i in('a','b','c','d'):
    print('i',i)
print("_"*50)
for i in {1,2,3,4}:
    print('i',i)
print("_"*50)
for i in {'a':1,'b':2,'c':3,'d':4}:
    print('i',i)
print("_"*50)
for i in range(0,5,1):
    print('i',i)
print("_"*50)
for (k,v) in {'a':1,'b':2,'c':3,'d':4}.items():
    print("{}:{}".format(k,v))
print("_"*50)


