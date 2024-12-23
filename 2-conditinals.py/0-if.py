'''
conditionals:
  on certain condition we can define a block of code
'''
'''
if condition:
   if-body

elif condition:
   elif body
   .
   .
   .
else:
   else-body in indentation   

'''

# a=4
# b=13

# if a>b:
#     print("a is greater than b")
# elif a==b:
#     print(f"a:{a} is equal to b:{b}")
# else:
#     print(f"a:{a} is less than b:{b}")

# #find the smaller of 2 no

# a=int(input("Enter your first number:"))
# b=int(input("Enter your second no.:"))

# if a<b:
#     print("a is smaller than b")
# elif a==b:
#     print(f"a:{a} is equal to b:{b}")
# else:
#     print(f"b:{b} is smaller than a:{a}")

#find the greatest no. among three

a=int(input("Enter your first number:"))
b=int(input("Enter your second no.:"))
c=int(input("Enter your third no.:"))

if a>b and a>c:
    print(f"a:{a} is the greatest no.")
elif b>c:
     print(f"b:{b} is the greatest no.")
else:
     print(f"c:{c} is the greates no.")     
     
