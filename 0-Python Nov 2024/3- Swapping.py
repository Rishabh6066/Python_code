'''
a=5
b=7
c =0
print('before Swapping',a,b)

c=a # a=5 , b=7 , c=5
a=b # a=7 , b=7 , c=5
b=c # a=7 , b=5 , c=5


print('after swapping',a,b)

#using fstring and using 2 variable
d=int(input("Enter the first number:"))
e=int(input("Enter the Second number:"))

print(f"Before Swapping the value of d: {d} and e: {e}")
#performing Swapping with two no.
e=e+d
d=e-d
e=e-d
print(f"After Swaping the value of e: {e} and d: {d}")
'''

#direct method

first=int(input("Enter your no."))
second=int(input("Enter your no."))

print(f"Before Swapping the value of first: {first} and second: {second}")
#performing Swapping with two no.
first,second=second,first
print(f"After Swaping the value of first: {first} and second: {second}")
