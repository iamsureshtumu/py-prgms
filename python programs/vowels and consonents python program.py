#write a program to count the no.of vowels and consonents present in a given string.

def vowel_count(s):
    s=s.lower()
    count=0
    for i in s:
        if i in "aeiou":
            count+=1
    return count
def cons_count(s):
    s=s.lower()
    count=0
    for i in s:
        if i.isalpha() and i not in "aeiou":
            count+=1
    return count
def vccc(s):
    s=s.lower()
    vc=0
    cc=0
    for i in s:
        if ord(i) in range(ord('a'),ord('z')+1):
            if i in"aeiou":
                vc+=1
            else:
                cc+=1
    return vc,cc


    

                

                

        

            
            
    
