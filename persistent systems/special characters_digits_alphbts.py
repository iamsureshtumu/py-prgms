#Python Program to Count Alphabets Digits and Special Characters in a String using For Loop
"""
Python Program to Count Alphabets Digits and Special Characters in a String
Write a Python program to Count Alphabets Digits and Special Characters in a String using For Loop, while loop, and Functions with an example.


 
Python Program to Count Alphabets Digits and Special Characters in a String using For Loop
This python program allows the user to enter a string.

First, we used For Loop to iterate characters in a String. Inside the For Loop, we are using Elif Statement

isalpha() in the first statement is to check whether the character is an alphabet or not. If true, alphabets value incremented.
isdigit() in the second statement checks whether the character is Digit or not. If true, digits value incremented.
Otherwise, special characters value incremented.
TIP: Please refer String article to understand everything about Python Strings.
"""
# Python program to Count Alphabets Digits and Special Characters in a String
 
string = input("Please Enter your Own String : ")
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
        
print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)
