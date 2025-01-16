#1- WAP to print the reverse of a no. given by user.
#2- WAP to check given no. is pallendrome or not.
#3- WAP to check the given no. is armstrong or not.
#4- WAP to print the first 10 fibonacci series .
#5- WAP to print the the list of first 10 prime no.
#6- WAP to print the list of prime no. till 10
#7- WAP to check given 2 strings by user are anagrams or not

# # reverse no-
# number=int(input("Enter the no."))
# temp=number
# reverse=0

# while number!=0:
#     rem= number % 10
#     reverse= reverse * 10 + rem
#     number=number//10

# print(f"the reverse of {temp} is {reverse}")

# #pallemdrome

# number=int(input("Enter the no."))
# temp=number
# reverse=0

# while number!=0:
#     rem= number % 10
#     reverse= reverse * 10 + rem
#     number=number//10

# if temp == reverse:
#     print(f"{temp} is pallendrome")
# else:
#     print(f"{temp} is not pallendrome")   


#armstrong no.

# number=int(input("Enter the no."))
# l=len(number)
# temp=number
# arm=0

# while number!=0:
#     rem= number % 10
#     arm= arm + rem**l
#     number=number//10

# if temp == reverse:
#     print(f"{temp} is pallendrome")
# else:
#     print(f"{temp} is not pallendrome")  

# '''
# * * * * 
# *     * 
# *     * 
# * * * * 
# '''
# print("-----4*4 hollow rectangle--------")
# n=4
# i=0
# while i<4:
#     j=0
#     while j<4:
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     print()
#     i+=1  

# '''
# * * * * * *
# *         *
# *         *
# * * * * * * 
# '''
# print("-----6*4 hollow rectangle--------")

# l=int(input("Enter the length of hollow rectangle: "))
# b=int(input("Enter the breadth of hollow rectangle: "))

# i=0
# while i<b:
#     j=0
#     while j<l:
#         if i==0 or j==0 or i==b-1 or j==l-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     print()
#     i+=1 

# '''
# * * * * 
# * *   * 
# *   * * 
# * * * * 
# '''
# print("-----hollow square with diagonal")

# n=int(input("Enter the size of hollow square"))
# i=0
# while i<n:
#     j=0
#     while j<n:
#         if i==0 or j==0 or i==n-1 or j==n-1 or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     print()
#     i+=1

# '''
# * 
# * *
# *   *
# *     *
# * * * * *
# '''
# print("-----hollow triangle--------")


# n=5
# i=0
# while i<5:
#     j=0
#     while j<=i:
#         if j==0 or i==j or i==4: 
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     print()
#     i+=1

# print("----hollow square---")
'''
* * * * *

* *   * *

*   *   *

* *   * *

* * * * *
'''
n=5
i=0
while i<5:
    j=0
    while j<5:
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1 

print("---- hollow inverted traingle ----")

'''

* * * * *
*     * 
*   *   
* *   
* 

'''

n= int(input("Enter the size of a hollow triangle: "))
i=0
while i<n:
    j=0
    while j<n-i:
        if j==0 or j==n-i-1  or i==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    print()
    i+=1 


print("---- hollow inverted traingle ----")

'''

* * * * *
  *     *
    *   *
      * *
        *

'''