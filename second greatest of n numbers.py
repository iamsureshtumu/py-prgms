#Python program to find second largest number in a list


#Method 1: Sorting is an easier but less optimal method. Given below is an O(n) algorithm to do the same.

# Python program to find second largest 
# number in a list 

# list of numbers - length of list should be at least 2 
list1 = [10, 20, 4, 45, 99] 

max=max(list1[0],list1[1]) 
secondmax=min(list1[0],list1[1]) 

for i in range(2,len(list1)): 
	if list1[i]>max: 
		secondmax=max
		max=list1[i] 
	else: 
		if list1[i]>secondmax: 
			secondmax=list1[i] 

print("Second highest number is : ",str(secondmax)) 



#Method 2 : Sort the list in ascending order and print the second last element in the list.

# Python program to find largest 
# number in a list 

# list of numbers 
list1 = [10, 20, 4, 45, 99] 

# sorting the list 
list1.sort() 

# printing the second last element 
print("Second largest element is:", list1[-2]) 



#Method 3 : By removing the max element from list

# Python program to find second largest 
# number in a list 

# list of numbers 
list1 = [10, 20, 4, 45, 99] 

# new_list is a set of list1 
new_list = set(list1) 

# removing the largest element from temp list 
new_list.remove(max(new_list)) 

# elements in original list are not changed 
# print(list1) 

print(max(new_list)) 




#Method 3 : Find max list element on inputs provided by user

# Python program to find second largest 
# number in a list 

# creating empty list 
list1 = [] 

# asking number of elements to put in list 
num = int(input("Enter number of elements in list: ")) 

# iterating till num to append elements in list 
for i in range(1, num + 1): 
	ele = int(input("Enter elements: ")) 
	list1.append(ele) 

''' 
# sort the list	 
list1.sort() 
	
# print second maximum element 
print("Second largest element is:", list1[-2]) 

'''

# print second maximum element using sorted() method 
print("Second largest element is:", sorted(list1)[-2]) 



