# '''
# Given a list of numbers, return the largest number in the list without using the max() function.
# '''
# l=[2,4,5,3,7,61,8,9,23,81,10,19,51]
# max=0
# for i in range (len(l)):
#     if l[i]> max:
#         max=l[i]
# print(f'The maximum elements from thre list is {max}' )

# '''
# Output:
# The maximum elements from thre list is 81

# '''

# '''

# '''

# n=int(input("Enter the no.:"))
# for i in range(1,n):
#     if i%3==0:
#         print(i, end=" ")

"""
Output-
Enter the no.:35
3 6 9 12 15 18 21 24 27 30 33 
"""        

'''
Write a program that takes a number as
 input and checks if it is divisible by both 2 and 5.

'''

# num=int(input("Enter the no.:"))

# if num%2==0 and num%5==0:
#     print("the no is divisible by both")
# # elif
# #     print("The no. is Negative ")
# else:
#     print("The no. is not divisible by both")     

# Given sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the intersection of both sets
intersection = set1.intersection(set2)

# Print the intersection
print(f"The intersectiion of {set1} and {set2} is {intersection}")
'''
Output-
The intersectiion of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8} is {4, 5}
'''


dict= {'a': 1, 'b': 2, 'c': 3}

# Get the list of all values in the dictionary
value= list(dict.values())

# Print the list of values
print(f'The value of dict is : {value}')

'''
Output-
The value of dict is : [1, 2, 3]
'''

grades = {'Alice': 88, 'Bob': 95, 'Charlie': 78, 'David': 85}

# Find the student with the highest grade
highest_grade_student = max(grades, key=grades.get)

# Print the student with the highest grade
print(f"The student with the highest grade is: {highest_grade_student}")

'''
Output-
The student with the highest grade is: Bob
'''

