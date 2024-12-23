
'''
WAP that uses a for loop and a conditional statement to create a new list that contains the square of all 
number from 1 to 20 , but only include numbers that are greater than 50.
using for- range()
'''
squares_above_50 = [] 
# Use a for loop with range to iterate through numbers from 1 to 20 
for number in range(1, 21): 
   number square = number ** 2 
if square > 50: 
    squares_above_50.append(square)
    print("Squares greater than 50:", squares_above_50)