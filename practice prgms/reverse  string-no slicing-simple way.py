def reverse(s):
    temp=" "
    for i in s:
        temp=i+temp
    return temp
n=input("Enter the value :") 
print(reverse(n))
