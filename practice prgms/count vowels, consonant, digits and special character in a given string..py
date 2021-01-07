# Python3 Program to count vowels, consonant, digits and special character in a given string. 

# Function to count number of vowels, consonant, digits and special character in a string. 


	# Declare the variable vowels, 
	# consonant, digit and special 
	# characters 

#prgm2 in easy way
vowels=0
consonent=0
digit=0
specialChar=0
string=input("enter the string: ")
for i in string:
    i=i.lower()
    if ( (i>='a' and i<='z') or (i>='A' and i<='Z')):
        if i in "aeiouAEIOU":
            vowels+=1
        else:
            consonent+=1
    elif (i>='0'and i<='9'):
        digit+=1
    else:
        specialChar+=1
    
print("no of vowels: ",vowels)
print("no of consonents: ",consonent)
print("no of digit: ",digit)
print("no of specialChar",specialChar)

print("------------------------------------------------------")

#it will also count length of the input
vowels=0
consonent=0
digit=0
specialChar=0
n=input("enter the input: ")
for i in n:
    i=i.lower()
    if ( (i>='a' and i<='z') or (i>='A' and i<='Z')):
        if i in "aeiouAEIOU":
            vowels+=1
        else:
            consonent+=1
    elif (i>='0'and i<='9'):
        digit+=1
    else:
        specialChar+=1
print("length of the string: ",len(n))
print("no of vowels: ",vowels)
print("no of consonents: ",consonent)
print("no of digit: ",digit)
print("no of specialChar",specialChar)
