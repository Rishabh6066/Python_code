'''Write a lambda function to print True for a even no.'''

# Lambda function to check if a number is even
is_even = lambda x: x % 2 == 0

# Example usage:
number = 4
print(is_even(number))  # Output: True

number = 5
print(is_even(number))  # Output: False
