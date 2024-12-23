
#-Write a Python program that sum all even numbers in the list [21,45,29,5,0,11,75,20].

num= [21,45,29,5,0,11,75,20]
sum=0
i=0

while i < len(num):
    if i%2==0:
        sum= sum + num[i]
    i+=1

print(f'The sum of even no. is : {sum}')

'''
output-
The sum of even no. is : 125

'''

#Write a Python program to count how many times a specific element 11 appears in a list.[21,11,29,5,0,11,11,20]
num= [21,11,29,5,0,11,11,20]
count=0
i=0
while i < len(num):
    if num[i]==11:
        count +=1
    i+=1
print(f"The no. 11 apperes {count} times.")    

'''
output-
The no. 11 apperes 3 times.

'''
# #reverse the list
# list=[21,11,29,5,0,11,11,20]
# i= len(list) - 1
# while i >=0:
#     print(list[i])
#     i-=1
# '''
# Output:

# 20
# 11
# 11
# 0
# 5
# 29
# 11
# 21

# '''    

#Write a Python program to print new list with only the elements from the original list that are divisible by 3.[21,11,27,5,3,11,12,20]

num=[21,11,27,5,3,11,12,20]

new_list=[]

i=0
while i<len(num):
    if i%3==0:
        new_list.append(num[i])
    i+=1

print (new_list)

'''
Output-

[21, 5, 12]

'''

# 6-Write a Python program to find the factorial of a number using a while loop.

'''

'''

#Write a Python program to generate a multiplication table for a number using a for loop.

# num=int(input("Enter your number: "))
# i=1
# while i<=10:
#     a= num * i 
#     print(a)
#     i+=1
'''
output-
Enter your number: 8
8
16
24
32
40
48
56
64
72
80
'''    
# Write a Python program that prints all even numbers from 1 to 50 using a while loop.

i=1
while i<=50:
    if i%2==0:
        print(i)
    i+=1

'''
Output-
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
'''

#11-Write a Python program that create a list of even index numbers from a list.
l=[21,10,29,18,0,12,11,20]
even=[]
i=0
while i<len(l):
    if i%2==0:
        even.append(l[i])
    i+=1
print(even)   

'''
Output-
[21, 29, 0, 11]
'''