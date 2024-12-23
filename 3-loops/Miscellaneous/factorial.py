# #factorial
# num=int(input("Enter you no.: "))

# #logic
# factorial=1
# i=1
# while i< num:
#     factorial= factorial *i
#     i+=1
# print(factorial) 



number = int(input("Enter a number: "))

# Initialize the factorial to 1
factorial = 1

# Use a for loop to calculate the factorial
for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is {factorial}")

'''
Output:
Enter a number: 5
The factorial of 5 is 120

Enter a number: 3
The factorial of 3 is 6
'''
