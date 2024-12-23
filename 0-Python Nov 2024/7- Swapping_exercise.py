#by default value of input() or value entered by user is string
# here we have to convert that string into integer using int() 'typecasting6

# swapping using 2 variables
a=int(input("enter first no."))
b=int(input("enter second no."))
print(f"Before Swapping a: {a} b: {b}")
a=a+b #using arithmetic operation
b=a-b
a=a-b
print(f"After Swapping a: {a} b: {b} ")
