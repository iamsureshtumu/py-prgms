#program that should receive the i/p
# i) aababcbc and o/p is a3b3c2
# ii) abacaac and o/p is a4b1c2

def count(s,key):
    c=0
    for i in s:
        if i==key:
            c+=1
    return c
def main():
    s=input("enter the string:")
    temp=" "
    for i in s:
        if i not in temp:
            temp+=i
            temp+=str(count(s,i))
    return temp
result=main()
print(result)




