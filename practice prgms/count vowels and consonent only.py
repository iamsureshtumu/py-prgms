#simple prgm without any builtin function
string=input("Enter string:")
vowels=0
consonent=0
for i in string:
      if ((i>='a' and i<='z') or (i>='A' and i<='Z')):
            if i in "aeiouAEIOU":
                vowels+=1
            else:                
                consonent+=1
    
print("Number of vowels are: ",vowels)
print("No of consonents are: ",consonent)

