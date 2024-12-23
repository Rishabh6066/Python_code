#  #nested conditionls : conditionls in conditionals

# a=int(input("Enter the no."))

# if(a>=0):
#     if(a!=5):
#         print(f"a:{a} is not 5")
#     else:
#         print(f"a:{a} is 5")
# else:
#     if a!=-5:
#         print(f"")            

# greatest of 3 nos given by user using nested if else

a=int(input("Enter a no.: "))
b=int(input("Enter a no.: "))
c=int(input("Enter a no.: "))

if a>b:
    if a>c:
        print(f"a: {a} is greatest")    # a>b a>c
    else:                               #c>a>b
        print(f"c:{c} is greatest")

else:
    if b>c:                             #b>a b>c
        print(f"b: {b} is greatest") 
    else:
        print(f"c: {c} is greatest")   # c>b>a             