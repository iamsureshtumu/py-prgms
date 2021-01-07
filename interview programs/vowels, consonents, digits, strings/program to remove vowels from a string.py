# Python program to remove vowels from a string 
# Function to remove vowels 
def rem_vowel(string): 
	vowels = ('a', 'e', 'i', 'o', 'u') 
	for i in string.lower(): 
		if i in vowels: 
			string = string.replace(i,"") 
			
	# Print string without vowels 
	print(string) 

# Driver program 
string =input("enter the string:")
rem_vowel(string) 
