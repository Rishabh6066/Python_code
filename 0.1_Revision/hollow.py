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
# '''
# * * * * *

# * *   * *

# *   *   *

# * *   * *

# * * * * *
# '''
# n=5
# i=0
# while i<5:
#     j=0
#     while j<5:
#         if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     print()
#     i+=1 

# print("---- hollow inverted traingle ----")

# '''

# * * * * *
# *     * 
# *   *   
# * *   
# * 

# '''

# n= int(input("Enter the size of a hollow triangle: "))
# i=0
# while i<n:
#     j=0
#     while j<n-i:
#         if j==0 or j==n-i-1  or i==0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     print()
#     i+=1 


# print("---- hollow inverted traingle ----")

# '''

# * * * * *
#   *     *
#     *   *
#       * *
#         *

# '''

print("----inclined line----")

'''

* 
  *     
    *    
      * 
        *

'''

for i in range(5):
    for j in range(i+1):
        if i==j:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()        


print("----x pattern---")
'''
*      *

  *   * 

    *   

  *   * 

*       *
'''

for i in range(5):
    for j in range(5):
        if i==j or i+j==4:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()  