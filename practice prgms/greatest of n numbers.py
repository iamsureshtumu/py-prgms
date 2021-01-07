# Python program to find largest number in a list


#Method 1 : Sort the list in ascending order and print the last element in the list.

# Python program to find largest 
# number in a list 
  
# creating empty list 
list1 = [] 
  
# asking number of elements to put in list 
num = int(input("Enter number of elements in list: ")) 
  
# iterating till num to append elements in list 
for i in range(1, num + 1): 
    ele = int(input("Enter elements: ")) 
    list1.append(ele) 
      
# print maximum element 
print("Largest element is:",max(list1))



#Method 2 : Using max() method

# Python program to find largest 
# number in a list 

# list of numbers 
list1 = [10, 20, 4, 45, 99] 


# printing the maximum element 
print("Largest element is:", max(list1))










