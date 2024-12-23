s1 = {1, 2, 4, 5, 6, 7}
s2 = {2, 5, 8, 9, 10, 11}

difference= s1.symmetric_difference(s2) 
result_list = list(difference)  # Convert the symmetric difference set to a list
print(f"Symmetric difference: {result_list}")

'''
output-
Symmetric difference: [1, 4, 6, 7, 8, 9, 10, 11]
'''

'''
 Write a program that takes a dictionary of people's names and their ages.
 It should return a dictionary where the names of people who are older than 30 are changed to uppercase
'''
# d ={}
# num_entries = int(input("How many people do you want to enter? "))
# for i in range (num_entries):
#    name=input("Enter your name:")
#    age=int(input("Enter your age:"))
#    d[name]=age
# print(d)

data={
    'Aman': 25, 'Ayush': 31, 'Rahul': 24, 'Prateek': 40
    }
new_d={}

for name,age in data.items():
    if age>30:
        new_d[name.upper()]=age
    else:
        new_d[name]=age

print(f"Modified data : {new_d}")

'''
Output-

Modified data : {'Aman': 25, 'AYUSH': 31, 'Rahul': 24, 'PRATEEK': 40}

'''

'''
Write a program that accepts a list of tuples, where each tuple contains a person's name and their age.
The program should return a list of names of people whose age is greater than 18.
'''
data=[('Aman', 25), ('AYUSH', 12) , ('Rahul', 20), ('PRATEEK', 17)]
modified_data=[]

for name, age in data:
    if age>18:
        modified_data.append(name)
print(f"Age greater than 18: {modified_data}")    

'''
Output-
Age greater than 18: ['Aman', 'Rahul']
'''

'''
Given a list of numbers, write a program that classifies each number as
"even" or "odd" and returns the count of "even" and "odd" numbers in the list
'''
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
count_even=0
count_odd=0

for num in l1:
    if num%2==0:
        count_even+=1
    else:
        count_odd+=1

print(f"The no. of even in list: {count_even}")
print(f"The no. of odd in list: {count_odd}")

'''
Output:
The no. of even in list: 8
The no. of odd in list: 9
'''

'''
Write a program that takes a list of integers and returns the sum of all the even numbers.
If the sum of even numbers exceeds 100, print "Limit Exceeded" and stop.
'''
l2=[23,4,5,61,2,4,6,8,13,24,5,7,8,22]
sum=0

for num in l2:
    if num%2==0:
        sum+=num
    if sum>100:
        print("limit Exeed")
        break
if sum<=100:
    print(f"The sum of even no. is: {sum}")        

'''
limit Exeed

The sum of even no. is: 78
'''



'''
Write a program that prints the following pattern of stars:
    
    *
    **
    ***
    ****
    
    The number of stars should be equal to the row number.

'''

for i in range(4): # no. of rows
    for j in range(i+1): # no. of coloumn
        print("*",end="")
    print()    

'''
output-
*
**
***
****
'''    

'''
8. Write a program that prints a reverse triangle pattern of numbers, such as:
    
    12345
    1234
    123
    12
    1

'''
for i in range(5,0,-1): #now of rows
    for j in range(1,i+1):
        print(j,end="")
    print()    

'''
Write a program that takes a list of integers and prints
the sum of the squares of all numbers in the list, using a for-range() loop.
'''
l3=[1,2,3,4,5,6,7,8,9,10]

sum_of_square=0

for i in l3:
    sum_of_square += i**2

print(f"The sum of square of all the num in the list: {sum_of_square}")

'''
Output-
The sum of square of all the num in the list: 385
'''

'''
Write a program that uses a while loop to print all
numbers from 1 to 50 that are divisible by 7.
'''
i=1
while i<=50:
    if i%7==0:
        print(i)
    i+=1  

'''
7
14
21
28
35
42
49
'''