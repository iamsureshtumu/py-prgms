#random is the inbuilt library to generate the random numbers

#"write a program to generate 6 digit OTP"

from random import randint
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')


print("-"*10)


#if we want 10 otp's at once, then add for loop

from random import randint
for i in range(10):
    print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

