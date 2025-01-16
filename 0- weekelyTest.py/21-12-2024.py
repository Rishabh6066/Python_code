'''
Section A: Theory (10 Questions)  

1. What is the difference between a list and a tuple in Python?  

2. Explain the immutability of strings with an example.  

3. Define a set and list two of its key properties.  

4. How does a dictionary store its elements, and why are keys required to be immutable?  

5. What is the purpose of conditional statements in Python? Provide an example.  

6. Explain the difference between `for` loops and `while` loops with examples.  

7. Describe the use of nested loops with a real-world example.  

8. What are the advantages of using list comprehensions in Python?  

9. How do you reverse a string in Python? Write the syntax for it.  

10. Explain the concept of pattern programs and their significance in coding practice.  


Section B: Correct the Error (10 Questions)  
1. 
   my_list = [1, 2, 3
   print(my_list)
   
   Identify and fix the error.  

2. 
   tuple_example = (1, 2, 3)
   tuple_example[1] = 5
   
   Identify and fix the error.  

3. 
   my_set = {1, 2, 3, 3}
   print(len(my_set))
   
   What will the output be, and why? Fix if needed.  

4. 
   my_dict = {1: 'a', 2: 'b'}
   print(my_dict[3])
   
   Identify and fix the error.  

5. 
   if 5 > 3
       print("Five is greater than three")
   
   Identify and fix the error.  

6. 
   for i in range[5]:
       print(i)
   
   Identify and fix the error.  

7. 
   while x < 5:
       print("Hello")
   
   What is the potential issue with this code? Fix it.  

8. 
   nested_list = [[1, 2], [3, 4]]
   for i in nested_list:
   print(i)
   
   Identify and fix the indentation error.  

9. 
   str_example = "Hello"
   str_example[0] = 'h'
   print(str_example)
   
   Identify and fix the error.  

10. 
   for i in range(1, 6):
       for j in range(i):
       print('*', end=' ')
       print()
   
   Fix the alignment issues in the nested loop.  

---

Section C: Coding (10 Questions)  

1. Write a program to reverse a given string.  

2. Create a list of numbers and find their sum using a loop.  

3. Write a Python program to generate the Fibonacci sequence up to `n` terms.  

4. Create a dictionary to store the names and marks of 5 students, then print all students scoring above 80.  

5. Write a program to find the maximum element in a list without using the `max()` function.  

6. Generate a pattern using nested loops:  
   
   1  
   3 5 
   7 9 11  
   13 15 17 19  
     
7. Write a Python program to find the factorial of a given number using a loop.  

8. Create a set of integers and check if a user-provided number exists in the set.  

9. Write a program to count the occurrences of each character in a string using a dictionary.  

10. Develop a program to calculate the sum of squares of the first `n` natural numbers using a loop.  
'''

my_set = {1, 2, 3, 3}
print(len(my_set))
print(my_set)

my_dict = {1: 'a', 2: 'b'}
print(my_dict.get(3, 'Key does not exist'))

for i in range(5):
    print(i)

x=1
while x < 5:
    print("Hello")
    x+=1

nested_list = [[1, 2], [3, 4]]
for i in nested_list:
   print(i)


str_example = "Hello"
print(str_example.replace('H','h'))
print(str_example)

for i in range(1, 6):
    for j in range(i):
       print('*', end=' ')
    print()

'''Write a program to reverse a given string.'''
s='hello'
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")

'''2. Create a list of numbers and find their sum using a loop.  

3.Write a Python program to generate the Fibonacci sequence up to `n` terms. '''
print()
l=[1,12,34,5,7,8,3]
sum=0
for i in l:
    sum+=i
print(sum)    

#3
# num=int(input("Enter the range upto want fibonacci series: "))
# a=0
# b=1
# print(a)
# print(b)
# n=1
# while(n<=num):
#     c=a+b
#     print(c)
#     a=b
#     b=c
#     n+=1
'''
4. Create a dictionary to store the names and marks of 5 students, then print all students scoring above 80.  

5. Write a program to find the maximum element in a list without using the `max()` function.  

6. Generate a pattern using nested loops:  
   
   1  
   3 5 
   7 9 11  
   13 15 17 19      
'''
dict={'Rahul':70,
      'Garima':86,
      'Seema':55,
      'Joe':91,
      'Daniel':68
      }

for i in dict:
    if dict[i]>80:
       print(i,dict[i])   
'''
Output:
Garima 86
Joe 91
'''   
#5

l=[1,2,3,4,5,11,21,3,6]
max=0
for i in l:
    if max<i:
        max=i
print(f'Maximum value in list: {max}')    
'''
Maximum value in list: 21

'''  
#6
num=1  
for i in range(4):
    for j in range(i+1):
        print(num ,end=" ")
        num+=2
    print() 

'''
1
3 5
7 9 11
13 15 17 19

'''

'''
7. Write a Python program to find the factorial of a given number using a loop.  

8. Create a set of integers and check if a user-provided number exists in the set.  

9. Write a program to count the occurrences of each character in a string using a dictionary.  

10. Develop a program to calculate the sum of squares of the first `n` natural numbers using a loop.  
'''
num=int(input("Enter the number: "))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(f"facorial of {num} is : {factorial}")    
'''
Enter the number: 5
facorial of 5 is : 120
'''
#Write a program to count the occurrences of each character in a string using a dictionary.
s="hello my name is Rishabh"
count=0
dict={}
for i in range(len(s)):
    if s[i] in dict:
        dict[s[i]]+=1
    else:
        dict[s[i]]=1
print(dict) 
'''
{'h': 3, 'e': 2, 'l': 2, 'o': 1, 
' ': 4, 'm': 2, 'y': 1, 'n': 1, 'a': 2, 'i': 2, 's': 2, 'R': 1, 'b': 1}
'''    
#8


   
#10
# Develop a program to calculate the sum of 
# squares of the first `n` natural numbers using a loop.



num = int(input("Enter the range of natural numbers: "))
square_sum = 0  

if num > 0:
    for i in range(1, num + 1):
        square_sum += i**2  

print("The sum of squares of the first", num, "natural numbers is:", square_sum)

'''
Output:
Enter the range of natural numbers: 5
The sum of squares of the first 5 natural numbers is: 55

Enter the range of natural numbers: 23
The sum of squares of the first 23 natural numbers is: 4324
'''








