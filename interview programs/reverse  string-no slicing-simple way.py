def reverse(s):
    temp=" "
    for i in s:
        temp=i+temp
    return temp
print(reverse("hello"))
