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

print("-------------------------------------------------------------------------------")

#2) this is count only alphabets
vcount = 0
ccount = 0  
str = input("Enter the string: ")  
   
#Converting entire string to lower case to reduce the comparisons  
str = str.lower()  
for i in range(0,len(str)):   
    #Checks whether a character is a vowel  
    if str[i] in ('a',"e","i","o","u"):  
        vcount = vcount + 1  
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        ccount = ccount + 1   
print("vowels",vcount)
print("consonent",ccount)

