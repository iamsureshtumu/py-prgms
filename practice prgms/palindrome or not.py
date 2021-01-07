#given string is palindrome or not
def ispalindrome(s):
    if s==s[::-1]:
        return True
    return False
#n=input("enter the value")
if ispalindrome("malayalam"):
    print("palindrome")
else:
    print("not a palindrome")



