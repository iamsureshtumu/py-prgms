#1) simple code for count the vowels
string=input("Enter string:")
vowels=0
for s in string:
      if s in "aeiouAEIOU":
            vowels+=1
print("Number of vowels are: ",vowels)



print("-"*30)
#2)code to count vowel in 
# a string using set 

# Function to count vowel 
def vowel_count(str): 
	
	# Intializing count variable to 0 
	count = 0
	
	# Creating a set of vowels 
	vowel = set("aeiouAEIOU") 
	
	# Loop to traverse the alphabet 
	# in the given string 
	for alphabet in str: 
	
		# If alphabet is present 
		# in set vowel 
		if alphabet in vowel: 
			count = count + 1
	
	print("No. of vowels :", count) 
	
# Driver code 
str=input("enter the string: ")   #str= "suresh"
# Function Call 
vowel_count(str)


print("-"*30)
#3)count the vowels with in the range of boundaries.





