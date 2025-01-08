 '''Perform multiplication of 2 nos without using multiplication operator (*)

# def multiplication(a,b):
#     c=0
#     for x in range(b):
#         c+=a

# print(multiplication(30,6))

a=30
b=3
c=0

for i in range(b):
    c+=a

print(f"{a} * {b} = {c}") 

'''
5 ,4
'''



'''
task7-
Write a recursive Python function count occurrence(lst, target) that counts the no.
of times a given element (target) appers in a list (lst).

Do not use any loops or built-in  method like count(). The function should work for nested lists
as well.

lst=[1,2,1,3,1,4,5,1]
target = 1
output: 4
'''

def count_occurance(lst, target): #
    if not lst:
        return 0
    
    count = 1 if lst[0] == target else 0
    return count + count_occurance(lst[1:], target)

lst=[1,2,1,3,1,4,5,1]
target = 1
result = count_occurance(lst, target)
print(f"Count: {result}")

'''
'''
iteration:

[1, 2, 1, 3, 1, 4, 5, 1]
1 + [2, 1, 3, 1, 4, 5, 1]
1 + 0 + [1, 3, 1, 4, 5, 1]
1 + 0 + 1 + [3, 1, 4, 5, 1]
1 + 0 + 1 + 0 + [1, 4, 5, 1]
1 + 0 + 1 + 0 + 1 + [4, 5, 1]
1 + 0 + 1 + 0 + 1 + 0 + [5, 1]
1 + 0 + 1 + 0 + 1 + 0 + 0 + [1]
1 + 0 + 1 + 0 + 1 + 0 + 0 + 1
'''