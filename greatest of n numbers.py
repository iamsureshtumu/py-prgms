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

list1.sort()
# print maximum element 
print("largest value is ",max(list1))
print("second largest value is",list1[-2])
print("smallest value is",min(list1))



#Method 2 : Using max() method

# Python program to find largest 
# number in a list 

# list of numbers 
list1 = [10, 20, 4, 45, 99] 

list1.sort()
# printing the maximum element 
print("Largest element is:", max(list1))
print("second largest value is",list1[-2]) #not true
print("smallest value is",list1[+2])








