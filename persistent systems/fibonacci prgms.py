#Python Program for Fibonacci numbers

#GeeksforGeeks

"""
The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 
 
Fn = Fn-1 + Fn-2

with seed values 

F0 = 0 and F1 = 1."""


#Method 1 ( Use recursion ) :

# Function for nth Fibonacci number

def Fibonacci(n):
	if n<=0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n==1:
		return 0
	# Second Fibonacci number is 1
	elif n==2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

# Driver Program

print(Fibonacci(9))


#Method 2 ( Use Dynamic Programming ) :


# Function for nth fibonacci number - Dynamic Programing
# Taking 1st two fibonacci nubers as 0 and 1

FibArray = [0,1]

def fibonacci(n):
	if n<=0:
		print("Incorrect input")
	elif n<=len(FibArray):
		return FibArray[n-1]
	else:
		temp_fib = fibonacci(n-1)+fibonacci(n-2)
		FibArray.append(temp_fib)
		return temp_fib

# Driver Program

print(fibonacci(9))


#Method 3 ( Space Optimized):


# Function for nth fibonacci number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
	a = 0
	b = 1
	if n <= 0:
		print("Incorrect input")
	elif n == 1:
		return b
	else:
		for i in range(2,n):
			c = a + b
			a = b
			b = c
		return b

# Driver Program

print(fibonacci(9))



















