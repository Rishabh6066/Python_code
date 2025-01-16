# 1- sort the list without using inbuilt func and nested loop
l = [11, 44, 99, 33, 77, 22, 11]

# Create an empty list for the sorted elements
sorted_list = []

# Iterate until the original list is empty
while l:
    # Assume the first element is the smallest
    smallest = l[0]
    for i in l:
        if i < smallest:
            smallest = i
    # Append the smallest element to the sorted list
    sorted_list.append(smallest)
    # Remove the smallest element from the original list
    l.remove(smallest)

print("Sorted list:", sorted_list)


# 2- find the prime from the list 
l=[11,3,8,4,7,29,13]  

l = [11, 3, 8, 4, 7, 29, 13]

primes = []

for num in l:
    if num > 1: 
        flag = True
        for i in range(2, num): 
            if (num % i) == 0:
                flag = False
                break
        if flag:
            primes.append(num)

print("Prime numbers in the list are:", primes)


# 3- Write a program to find the two string given by user is anagrams or not

# string1=input("Enter the string1 : ")
# string2=input("Enter the string2 : ")

# string1= string1.replace(" ","").lower()
# string2= string2.replace(" ","").lower()

# if len(string1) != len(string2):
#     print("This is not Anagram")
# else:
#     if sorted(string1)==sorted(string2):
#         print("This is Anagram")
#     else:
#         print("This is not anagram")  

# 4- Create a list of nos. greater than 20 from 
l=[1,7,30,20,32,60,3,7,19,21,47]
# using list comprehension

l1=[i for i in l if i>20]
print(l1)


'''
5- The Housekeeper's Calendar

You work for a housekeeper who is responsible for tracking daily temperature readings. 
She receives a list of 30 days of temperature data, but some of the readings are in string format. 
Your job is to find out how many days had temperatures above 25°C, 
as those are the days the housekeeper needs to take extra precautions.
'''

temperatures = [22, "30", "25", "29", "not available", "20", "35"]

# Convert valid numeric strings to integers
converted_temperatures = [int(temp) for temp in temperatures if str(temp).isdigit()]

tem=[x for x in converted_temperatures if x>25]
print(f"Temp above 25°C : {tem}")




'''
6- The Shopping Cart

You are managing an online shopping cart. 
Each item in the cart is a dictionary containing the price and quantity. 
However, some quantities are recorded as strings and need to be converted into integers. 
Your task is to calculate the total cost of all items in the cart.
'''

cart = [
    {"item": "Apple", "price": 2, "quantity": "3"},
    {"item": "Banana", "price": 1, "quantity": "5"},
    {"item": "Orange", "price": 3, "quantity": "2"},
    {"item": "Watermelon", "price": 5, "quantity": "7"}
]


total=0
for i in cart:
    price= i['price']
    quant= int(i['quantity'])
    total += price * quant
print(f"Total cost of all items in cart : {total}")  

'''
7- Student Report
You are given a list of dictionaries, where each dictionary contains information about a 
student (their name and age). 
Write a list comprehension to create a list of the names of all students who are over 18 years old.
'''
students = [
    	{"name": "Alice", "age": 17},
    	{"name": "Bob", "age": 20},
    	{"name": "Charlie", "age": 19},
    	{"name": "David", "age": 22},
    	{"name": "Eve", "age": 16}
    ]
#    o/p: ["Bob", "Charlie", "David"]

over_18=[x['name'] for x in students if x['age']>18]
print(f"Over 18 year old : {over_18}")

