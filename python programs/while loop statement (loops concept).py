# write a program to check the given no. is even or not, if it is even then remove the no of 2's present inside it
# & print the no. which doesn't consists of any 2's and also i want to remove count the no of 2's

num=500
count=0
if num%2==0:
    while num>=2:
        num-=2
        count+=1
print("num")
print("the no of 2's removed is",count)
