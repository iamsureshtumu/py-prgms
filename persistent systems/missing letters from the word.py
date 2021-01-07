
#method 1
alphabet = "abcdefghijklmnopqrstuvwxyz" 

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]     

def missing_letters(string):
    result = alphabet
    compare = set(string)# use histogram to make a dictionary
    compare=sorted(compare)
    for key in compare: # iterate and sort in alphabetical order
        if key in alphabet: # check if the key in alphabet
            result = result.replace(key,'')# remove it from alphabet
    return result

# Test the function          
print(missing_letters("ab")) # output: bcdefghijklmnopqrstuvwxyz

##### test_miss for loop #####

for letters in test_miss: 
    if len( missing_letters(letters) ) == 0:
        print(letters, 'uses all the letters')   
    else:
        print(letters , 'is missing letters', missing_letters(letters))

# output: zzz is missing letters abcdefghijklmnopqrstuvwxy                                                                               
# subdermatoglyphic is missing letters bcdefghijklmnopqrstuvwxyz                                                                 
# the quick brown fox jumps over the lazy dog uses all the letters

####################################################
#method 2
"""You don't need to count the number of letter, you can directly use a set (that will have only one occurence of
each letter from your input string). Once you have that set you can subtract this set from
the alphabet and you'll end up with a set that contains the missing letters:
"""

from string import ascii_lowercase

alphabet = set(ascii_lowercase)

def missing_letters(string):
    return alphabet - set(string.lower())

print(missing_letters("abcdefghijklmnopqr"))

"""
Will output {'w', 'y', 'x', 'z'}. Note that ascii_lowercase simply is a string containing all lower-case letters.
"""
#################################################

#method 3

"""The main problem is that you return inside of the loop, i.e. after checking
the very first letter. Also, it seems like you are iterating letters in the word and
checking whether they are in the alphabet, instead of the other way around, which would make more senes.
Also, it seems unnecessary to create a histogram of letter frequencies."""

#You can try something like this:

def missing_letters(string):
    missing = []
    for key in alphabet:
        if key not in string:
            missing.append(key)
    return ''.join(missing) or None
#Or you could convert both the alphabet and the string to set and use set difference -:

def missing_letters(string):
    return ''.join(sorted(set(alphabet) - set(string))) or None
