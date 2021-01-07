def v_count(s,start=0,end=0):
    if end==0:
        end=len(s)
    count=0
    for i in range(start,end):
        if s[i] in "aeiouAEIOU":
            count+=1
    return count

if __name__=='__main__':
    print(v_count("abcdefghijklmnopqrstuvwxyz"))
    print(v_count("abcdefghijklmnopqrstuvwxyz",19))
    print(v_count("abcdefghijklmnopqrstuvwxyz",0,5))
                  
