'''
1. Write a program to check if a number entered by the user is positive. If yes, print "The number is positive."

2. Write a program to check if a number entered by the user is even or odd.

3.Write a program to determine the grade of a student based on marks:

 Marks >= 90: Grade A

 Marks >= 75: Grade B

 Marks >= 50: Grade C

 Below 50: Grade F

 
 4.Write a program to check if a number is positive, negative, or zero. If it's positive, check if it's greater than 100.

5.Write a program to check if a number is divisible by both 3 and 5.

6.
 Write a one-liner program to check if a given year is a leap year or not using ternary operator.
 value_if_true if condition else value_if_false

7.

Write a program to check if a number lies between 10 and 50 (inclusive).

8.

Write a program to create a simple calculator that performs addition, subtraction, multiplication, or division based on user input.


9.

Write a program to determine if a triangle is valid based on the sides entered by the user. (A triangle is valid if the sum of any two sides is greater than the third side.)

10.

Write a program to calculate the electricity bill based on the following conditions:

 

For the first 100 units: ₹1.5 per unit

 

For the next 200 units: ₹2.5 per unit

 

Above 300 units: ₹4.0 per unit

Ask the user for total units consumed and compute the bill.
'''

#1 Write a program to check if a number entered by the user is positive. If yes, print "The number is positive."

num=int(input("Enter the number: "))

if num>=1 and num>=0:
    print("The no. is  +ve number")
else:
    pass

#2. Write a program to check if a number entered by the user is even or odd.

num=3
if num%2==0:
    print("The no. is even")
else:
    ("The no. is odd")  

'''
3.Write a program to determine the grade of a student based on marks:
Marks >= 90: Grade A
Marks >= 75: Grade B
Marks >= 50: Grade C
Below 50: Grade F
'''
marks=80

if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Grade F")  

#4.Write a program to check if a number is positive, negative, or zero. 
# If it's positive, check if it's greater than 100.  

num=int(input("Enter the number: "))


if num>0:
    print("The no. is +ve")
    if num>100:
        print("yes the number is greater than 100")
    else:
        pass   
elif num<0:
    print("The no. is -ve no.")

else:
    print("The no. is Zero")

#5.Write a program to check if a number is divisible by both 3 and 5.

num=50
if num%3==0 and num%5==0:
    print("The no is divisible by both")
else:
    print   





