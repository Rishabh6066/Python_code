# list of first 10 even no.
# using loops
# o/p- [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
even=[]
for i in range(0,20):
    if i%2==0:
        even.append(i)
print(even) 

'''
the correct way of doing this is: 
using while loop because we dont hat to count the numbers.

even = []
i = 0
while len(even) < 10:
    if i % 2 == 0:
        even.append(i)
    i += 1
print(even)

'''

'''
output-
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
'''
# list of first 10 till 10
# using loops
# o/p- [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# even_num=[]
# i=0
# while len(even_num)<=5: # dont use equal sign here
#     if i%2==0:
#         even_num.append(i)
#     i+=1
# print(even_num)        

even_num = []
i = 0
while len(even_num) < 5:
    if i % 2 == 0:
        even_num.append(i)
    i += 1
print(even_num)

# list of first 10 prime no,
#0/p :
#using loops

# prime_no=[]
# n=2
# i=0
# while len(prime_no) < 10:
#     flag= True
#    if n==1:
#       print(f"{n} is not prime")
#    else:
#       for i in range(2,n):
#          if n % i==0:
#            flag= False
#            break
#       if flag==True:
#          print(f"{n} is prime")
#       else:
#          print(f"{n} is not prime")

# prime_no = []
# n = 2

# while len(prime_no) < 10:
#     flag = True
#     for i in range(2, n):
#         if n % i == 0:
#             flag = False
#             break
#     if flag:
#         print(f"{n} is prime")
#         prime_no.append(n)  # Add the prime number to the list
#     n += 1

# print("First 10 prime numbers:", prime_no)

# list of prime no
#o/p : [2,3,4,7]
# using loops

p=[ ]
n=2

while n < 10:
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    if flag:
        p.append(n)  # Add the prime number to the list
    n += 1

print("First 5 prime numbers:", p)



