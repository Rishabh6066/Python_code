
# print Greatest middle and smallest of the three no. given by the user

1
5

# if a>b and a>c:
#     if a<b and a>c:
#         if a<b and a<c:
#             smallest=a
#         middle=b   
#     greatest=a

# elif b>a and b>c:
#     greatest=b
#     if a>c
#         middle=a
#     else:


# else:
#     ("c is greatest")


a=int(input("Enter first no: "))
b=int(input("Enter second no: "))
c=int(input("Enter thrid no: "))

if a >= b and a >= c:
    greatest = a
    if b >= c:
        middle = b
        smallest = c
    else:
        middle = c
        smallest = b
elif b >= a and b >= c:
    greatest = b
    if a >= c:
        middle = a
        smallest = c
    else:
        middle = c
        smallest = a
else:
    greatest = c
    if a >= b:
        middle = a
        smallest = b
    else:
        middle = b
        smallest = a

# Print the results
print("Greatest:", greatest)
print("Middle:", middle)
print("Smallest:", smallest)

  
