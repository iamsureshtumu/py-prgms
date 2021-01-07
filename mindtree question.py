#Mind Tree question

#program that should receive the i/p i) aababcb and o/p as a3b3c2
# ii) abacaac and o/p a4b1c2


def count(s,key):
    count=0
    for i in s:
        if i==key:
            count+=1
    return count

def main():
    s=input("enter the string")
    temp=" "
    for i in s:
        if i not in temp:
            temp+=i
            temp+=str(count(s,i))
    return temp
result=main()
print(result)
