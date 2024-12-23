'''
1. Write a Python program to print a right-angled triangle pattern using numbers. The number of rows should be input by the user.

   Example:
   
   1
   1 2
   1 2 3
   1 2 3 4
   

 2. Write a Python program to print an inverted right-angled triangle using numbers. The number of rows should be input by the user.

   Example:
   
   5 4 3 2 1
   5 4 3 2
   5 4 3
   5 4
   5
   

 3. Write a Python program to print a right-angled triangle pattern using alphabets. The number of rows should be input by the user.

   Example:
   
   A
   A B
   A B C
   A B C D
   

 4. Write a Python program to print an inverted right-angled triangle pattern using alphabets. The number of rows should be input by the user.

   Example:
   
   A B C D E
   A B C D
   A B C
   A B
   A
   

 5. Write a Python program that prints the multiplication table for a given number (1 to 10) using nested loops.

   Example for input 5:
   
   1 x 5 = 5
   2 x 5 = 10
   3 x 5 = 15
   4 x 5 = 20
   5 x 5 = 25
   6 x 5 = 30
   7 x 5 = 35
   8 x 5 = 40
   9 x 5 = 45
   10 x 5 = 50
   

 6. Write a Python program that takes a list of numbers and returns the sum of all even numbers in the list.

   Example:
   
   Input: [1, 2, 3, 4, 5, 6]
   Output: 12
   

 7. Write a Python program that finds the maximum and minimum values from a given tuple of numbers.

   Example:
   
   Input: (3, 5, 7, 2, 8)
   Output: Maximum: 8, Minimum: 2
   

 8. Write a Python program that takes two sets and returns the union of these two sets.

   Example:
   
   Input: set1 = {1, 2, 3}, set2 = {3, 4, 5}
   Output: {1, 2, 3, 4, 5}
   

 9. Write a Python program that takes a string, splits it into words, and then reverses the order of the words using loops.

   Example:
   
   Input: "Python is great"
   Output: "great is Python"
   

 10. Write a Python program that counts the number of vowels (a, e, i, o, u) in a given string using split and loop.

   Example:
   
   Input: "Hello, how are you?"
   Output: 7

'''

#5
num=5

for i in range(10):
    for j in range(i):
        print(f"{num} x {i} = {j * num} ")


# Input the number of rows
rows = int(input("Enter the number of rows: "))

# Generate the pattern
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
'''
Output-
1 
1 2 
1 2 3 
1 2 3 4 

'''
# Input the number of rows
rows = int(input("Enter the number of rows: "))

# Generate the pattern
for i in range(rows, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
'''
Output- 

5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 

'''

# Input the number of rows
rows = int(input("Enter the number of rows: "))

# Generate the pattern
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

'''
Output-
A 
A B 
A B C 
A B C D 
'''

# Input the number of rows
rows = int(input("Enter the number of rows: "))

# Generate the pattern
for i in range(rows, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

'''
Output-
A B C D E 
A B C D 
A B C 
A B 
A 

'''

# Input the number for the multiplication table
number = int(input("Enter the number for the multiplication table: "))

# Generate the table
for i in range(1, 11):
    print(f"{i} x {number} = {i * number}")

'''
Output-
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
6 x 5 = 30
7 x 5 = 35
8 x 5 = 40
9 x 5 = 45
10 x 5 = 50

'''

# Input the list of numbers
numbers = [int(x) for x in input("Enter the numbers separated by spaces: ").split()]

# Calculate the sum of even numbers
even_sum = sum(x for x in numbers if x % 2 == 0)

# Print the result
print(f"Sum of all even numbers: {even_sum}")

'''
Output-

Input: 1 2 3 4 5 6
Output: Sum of all even numbers: 12

'''

# Input the tuple of numbers
numbers = tuple(map(int, input("Enter the numbers separated by spaces: ").split()))

# Find maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)

# Print the results
print(f"Maximum: {max_value}, Minimum: {min_value}")

'''
Output-
Input: 3 5 7 2 8
Output: Maximum: 8, Minimum: 2

'''

# Input the two sets of numbers
set1 = set(map(int, input("Enter the first set of numbers separated by spaces: ").split()))
set2 = set(map(int, input("Enter the second set of numbers separated by spaces: ").split()))

# Find the union of the sets
union_set = set1 | set2

# Print the result
print(f"Union of the two sets: {union_set}")

'''
Output-

Input set1: 1 2 3
Input set2: 3 4 5
Output: Union of the two sets: {1, 2, 3, 4, 5}

'''

# Input the string
string = input("Enter a string: ")

# Split the string into words and reverse the order
reversed_words = ' '.join(string.split()[::-1])

# Print the result
print(f"Reversed string: {reversed_words}")

'''
Output-

Input: Python is great
Output: Reversed string: great is Python

'''

# Input the string
string = input("Enter a string: ")

# Initialize vowel count
vowel_count = 0

# List of vowels
vowels = "aeiouAEIOU"

# Count the vowels
for char in string:
    if char in vowels:
        vowel_count += 1

# Print the result
print(f"Number of vowels: {vowel_count}")

'''
Output-
Input: Hello, how are you?
Output: Number of vowels: 7

'''
