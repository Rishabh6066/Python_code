'''

1- Write a program to find the largest of three numbers using conditional statements.

2- Write a program to print all prime numbers between 1 and 50 using a loop.

3- Create a function that takes a list of numbers and returns the sum of its elements.

4- Write a lambda function to calculate the square of a given number.

5- Implement a program to check whether a given number is a palindrome using a loop.

6- Write a function that takes two arguments and returns the greater of the two.

7- Create a Higher-Order Function that applies a given function to each element in a list.

8- Write a program to calculate the factorial of a number using recursion.

9- Create a function that filters out odd numbers from a list using filter and a lambda function.

10- Write a program to count the number of vowels in a given string using loops and conditionals.

'''

# 1- Write a program to find the largest of three numbers using conditional statements.

# a=int(input("Enter the First no: "))
# b=int(input("Enter the Second no: "))
# c=int(input("Enter the Third no: "))

# if a>b:
#     if a>c:
#         print(f"a: {a} is largest")    
#     else:                            
#         print(f"c:{c} is largest")

# else:
#     if b>c:                            
#         print(f"b: {b} is largest") 
#     else:
#         print(f"c: {c} is largest")

# '''
# output-
# Enter the First no: 6
# Enter the Second no: 9
# Enter the Third no: 11
# c: 11 is greatest

# Enter the First no: 8
# Enter the Second no: 5
# Enter the Third no: 4
# a: 8 is largest

# Enter the First no: 7
# Enter the Second no: 11
# Enter the Third no: 3
# b: 11 is largest
# '''        


#2 Write a program to print all prime numbers between 1 and 50 using a loop.

prime_no=[]

for i in range(2,50):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
    if flag==True:
        prime_no.append(i)

print(f" Prime no. between 1 to 51: \n {prime_no}")  
'''
Output:
 Prime no. between 1 to 51: 
 [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
'''
#3 Create a function that takes a list of numbers and returns the sum of its elements.

# def numbers():
#     sum=0
#     list_of_num=[ ]
#     l=int(input("Enter the lenght of list: "))
#     for i in range(l):
#         num=int(input("Enter the no."))
#         list_of_num.append(num)
  
#     for i in list_of_num:
#         sum+=i
#     return print(f"sum of {list_of_num} is  : {sum}")

# numbers()  

'''
Enter the lenght of list: 6
Enter the no.21
Enter the no.2
Enter the no.45
Enter the no.2
Enter the no.71
Enter the no.22
sum of [21, 2, 45, 2, 71, 22] is  : 163

'''
#4- Write a lambda function to calculate the square of a given number.


#5- Implement a program to check whether a given number is a palindrome using a loop.

#6- Write a function that takes two arguments and returns the greater of the two.

def greatest(a,b):
    if a>b:
        return print(f"a: {a} is greatest")
    else:
        return print(f"b: {b} is greatest")

greatest(9,6) 
greatest(2,3)
greatest(1001,543)
greatest(0,1) 

'''
Output:

a: 9 is greatest
b: 3 is greatest
a: 1001 is greatest
b: 1 is greatest

'''



