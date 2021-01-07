#reverse the string or a number and check it is palindrome or not
def reverse(str1):
    if(len(str1)==0):
        return str1
    else:
        return reverse(str1[1 : ])+str1[0]
string=input("enter the string or value: ")
str1=reverse(string)
print("string in reverse order: ",str1)

if(string==str1):
    print("it is a Palindrome")
else:
    print("Not a Palindrome")
