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
        print(f"c: {c} is greatest")