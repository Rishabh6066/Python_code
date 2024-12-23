# # Write a program to reverse a given list of numbers.

# # l=[1,2,3,4,5,6,7,8,9,10]
# # newlist=[]
# # for i in range(len(l)-1,-1,-1):
# #     newlist.append(l[i])
# # print(f"Reversed list: {newlist}")

# # '''
# # Output-
# # Reversed list: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# # '''
# #Write a program to check if a given list is a palindrome.

# # n=int(input("Enter the no.: "))
# # temp=n
# # rev=0
# # while n!=0:
# #     rem= n%10
# #     rev= rev * 10 + rem
# #     n= n//10

# # if temp==rev:
# #     print("The no. is pallendrome")
# # else:
# #     print("The no. is not pallendrome")
# # '''
# # Output:

# # Enter the no.: 123
# # The no. is not pallendrome

# # Enter the no.: 131
# # The no. is pallendrome
# # '''

# '''
# Write a program to reverse a 
# given string using a loop (without slicing).
# '''
# # string=input("Enter you string: ") #rishabh

# # reverse=" "

# # for i in string:
# #     reverse= i + reverse #r + ''= r    'i' + 'r' =ir 
# # # loke this it will continue until it will reach the  last string
# # print(f"Your reverse string is: {reverse}")

# '''
# output:
# Enter you string: rishabh
# Your reverse string is: hbahsir 
# '''

# '''
# Write a program to create a dictionary from two lists—one 
# for keys and the other for values.

# '''
# keys=['car','bus','train','plane']
# value=[100, 200, 50, 1000]  

# dict= {}
# for i in range(len(keys)):
#     #Assign the value to the dictionary
#     dict[keys[i]]= value[i]
# print(f"The dictionary is : {dict}")
# '''
# Output:
# The dictionary is : {'car': 100, 'bus': 200, 'train': 50, 'plane': 1000}
# '''
# '''
# Write a program to find the union of two sets and print the result.

# '''

# s1={2,3,4,5,8}
# s2={4,6,7,2,3}

# s3=s1.intersection(s2)

# print(f"The intersiction of s1:{s1} and s2:{s2} is {s3}")

# '''
# Output-

# The intersiction of s1:{2, 3, 4, 5, 8} and s2:{2, 3, 4, 6, 7} is {2, 3, 4}
# '''

# '''
# Write a program to calculate the 
# sum of all elements in a list using a loop.
# '''
# l=[1,2,3,4,5,6,7,8,9,10]

# sum=0

# for x in range(len(l)):
#     sum= sum + l[x]
# print(f"The total sum: {sum}")    
# '''
# output:
# The total sum: 55
# '''
# '''
# Write a program to count how many
#  times a specific element appears in a list.

# '''
# l=[4,5,4,6,7,6,4,2,1,9,5,1]


# for i in range(len(l)):
#     count_num= l.count(l[i])
#     print(F"{l[i]} appears {count_num}")

   

# '''
# Output:
# The max value is 81
# The min value is 3
# '''

# '''
# Write a program to remove duplicates
#  from a list using a set and print the result.

# '''
# l=[4,5,4,6,7,6,4,2,1,9,5,1]

# set=set(l)
# print(f"The result: {set}")

   

# '''
# Output:
# The result: {1, 2, 4, 5, 6, 7, 9}
# '''
# '''

# '''

# # Given list of numbers
# numbers = [4, 5, 6, 7,11, 8, 9, 10]

# # Initialize a flag variable
# flag = True

# # Use a for loop with range to iterate through the list
# for i in range(len(numbers) - 1):
#     if numbers[i] > numbers[i + 1]:
#         flag = False
#         break

# # Print the result
# if flag:
#     print(f"The list {numbers} is sorted in ascending order.")
# else:
#     print(f"The list {numbers} is not sorted in ascending order.")

# '''
# Output:

# The list [4, 5, 6, 7, 8, 9, 10] is sorted in ascending order.

# The list [4, 5, 6, 7, 11, 8, 9, 10] is not sorted in ascending order.

# '''    



# l = [4, 5, 4, 6, 7, 6, 4, 2, 1, 9, 5, 1]

# # Initialize an empty dictionary to store the counts
# count_dict = {}

# # Use a for loop to iterate through the list
# for element in l:
#     # If the element is already in the dictionary, increment its count
#     if element in count_dict:
#         count_dict[element] += 1
#     # If the element is not in the dictionary, add it with count 1
#     else:
#         count_dict[element] = 1

# # Print the counts of each element
# for key, value in count_dict.items():
#     print(f"{key} appears {value} times")

# '''
# Output-

# 4 appears 3 times
# 5 appears 2 times
# 6 appears 2 times
# 7 appears 1 times
# 2 appears 1 times
# 1 appears 2 times
# 9 appears 1 times

# '''

# '''
# Write a program to print the multiplication table of a given number 
# (up to 10) using a for loop.
# '''

# for i in range(1,11):
#     for j in range(1,11):
#         print(i * j, end=" ")
#     print('\n')    
 

# '''
# Output:

# 1 2 3 4 5 6 7 8 9 10 

# 2 4 6 8 10 12 14 16 18 20

# 3 6 9 12 15 18 21 24 27 30

# 4 8 12 16 20 24 28 32 36 40

# 5 10 15 20 25 30 35 40 45 50

# 6 12 18 24 30 36 42 48 54 60

# 7 14 21 28 35 42 49 56 63 70

# 8 16 24 32 40 48 56 64 72 80

# 9 18 27 36 45 54 63 72 81 90

# 10 20 30 40 50 60 70 80 90 100

# '''
 
'''
Create a tuple with the elements (1, 2, 3, 4, 5). Write a program to convert 
this tuple to a list and add the number 6 to the end of the list.
'''
# t=(1, 2, 3, 4, 5)

# #convert the tuple tothe list
# l=list(t)


# #add the element 6 in the list
# l.append(6)
# print(l)

# '''
# Output:

# [1, 2, 3, 4, 5, 6]

# '''

# s1={2,3,4,5,8}
# s2={4,6,7,2,3}
# s3=s1.intersection(s2)
# s4=s1.union(s2)
# s5=s1.difference(s2)
# print(f"The intersection of s1:{s1} and s2:{s2} is {s3}")
# print(f"The intersection of s1:{s1} and s2:{s2} is {s4}")
# print(f"The intersection of s1:{s1} and s2:{s2} is {s5}")
# '''
# Output:
# The intersection of s1:{2, 3, 4, 5, 8} and s2:{2, 3, 4, 6, 7} is
# {2, 3, 4}
# The intersection of s1:{2, 3, 4, 5, 8} and s2:{2, 3, 4, 6, 7} is
# {2, 3, 4, 5, 6, 7, 8}
# The intersection of s1:{2, 3, 4, 5, 8} and s2:{2, 3, 4, 6, 7} is
# {8,5}
# '''

# # Given dictionary of student names and their marks
# student_marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 88,
#     "Diana": 95,
#     "Eve": 78
# }

# # Calculate the sum of all marks
# total_marks = sum(student_marks.values())

# # Calculate the number of students
# number_of_students = len(student_marks)

# # Calculate the average marks
# average_marks = total_marks / number_of_students

# # Print the result
# print(f"The average marks of all students is {average_marks:.2f}")

# '''
# Output-
# The average marks of all students is 87.60
# '''

'''
Given a list of integers, write a program that returns a list with 
all duplicate elements removed, but preserves the order of the original elements.
'''

list = [4, 5, 4, 6, 7, 6, 4, 2, 1, 9, 5, 1]
preservList=[]

for i in list:
    if i not in preservList:
        preservList.append(i)

print(f"The preserves order of the original list: {preservList} ")

'''
Output:

The preserves order of the original list: [4, 5, 6, 7, 2, 1, 9] 

'''
'''
Write a program that takes two sets of integers and returns a 
list of elements that are present in both sets but not in the other.
'''
s1 = {1, 2, 4, 5, 6, 7}
s2 = {2, 5, 8, 9, 10, 11}

union_set = s1.union(s2)  # Use a different variable name to store the union
result_list = list(union_set)  # Convert the union set to a list
print(result_list)
