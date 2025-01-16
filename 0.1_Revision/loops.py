'''
Loops revision

1) You are given a list of dictionaries, where each dictionary contains information about a student 
(their name and age). 
Write a list comprehension to create a list of the names of all students who are over 18 years old.

    	students = [
                {"name": "Alice", "age": 17},
                {"name": "Bob", "age": 20},
    		    {"name": "Charlie", "age": 19},
    		    {"name": "David", "age": 22},
    		    {"name": "Eve", "age": 16}
   	]
    	o/p: ["Bob", "Charlie", "David"]

2) Find the longest palindrome from the string : 'abacdabbacd'

3) l=[1,3,('a',[1,9,'Sunita',66,(22,[('Lyn')],"l"),-3]),[44,7,1,["Williams"],77,90]] 

 o/p: Sunita Lyn Williams

4) The Magic Number Game
You’re playing a game with your friends where you have a list of numbers. 
If a number is divisible by 3, it’s considered "Magic". However, 
if the number is both divisible by 3 and greater than 100, 
it’s called "Super Magic". 
Your task is to loop through the list and print the appropriate labels.

	numbers = [3, 10, 30, 150, 9, 7, 102]

 
5)      Write a nested loop to print


	    *
	   ***
	  *****
 	 *******
	*********
'''


#1
students = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 22},
    {"name": "Eve", "age": 16}
]

over_18 = [student["name"] for student in students if student["age"] > 18]
print(over_18)


#3)
l=[1,3,('a',[1,9,'Sunita',66,(22,[('Lyn')],"l"),-3]),[44,7,1,["Williams"],77,90]] 

#o/p: Sunita Lyn Williams

print(f"{l[2][1][2]} {l[2][1][4][1][0]} {l[3][3][0]}")



'''
4) The Magic Number Game
'''
numbers = [3, 10, 30, 150, 9, 7, 102]
divisible_by_3=[]
greater_than_100=[]

for i in numbers:
    if i%3==0 and i<100:
        divisible_by_3.append(i)
    elif i%3==0 and i>100:
        greater_than_100.append(i)  

print(f"No. diisible by 3: {divisible_by_3}")
print(f"Divisible by 3  greater than 100 : {greater_than_100}")

#5
'''

	    *
	   ***
	  *****
 	 *******
	*********
'''

n = 5
for x in range(n):
    for y in range(n - x - 1):
        print(" ", end="")
    for y in range(2 * x + 1):  # Adjusted this line
        print("*", end="")
    print()

#2


#6)     Write a recursive function to calculate the sum of digits of a integer no

 

#7)     Write a user defined function that works as split()