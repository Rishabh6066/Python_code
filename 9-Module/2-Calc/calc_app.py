# c=add.add(a,b)
# print(c)
'''
Task:

Welcome to calculator

0- Exit
1- Add
2- Sub
3- mul
4- div
5- mod
6- floordiv
7- Expo
Enter your Choice:
1
add()
a,b?
2:
sub()

attemt 10
'''


# print("---------Welcome to Calculator---------")
# print(" 0- Exit\n 1- Add\n 2- Sub\n 3- Mul\n 4- Div\n 5- Mod\n 6- FloorDiv\n 7- Expo")
# import add,sub,mul,div,mod,floordiv,expo

# for i in range(1,10):
#     print(f"----Attempt: {i}---")
#     choice = int(input("Enter your choice: "))
    
#     if choice == 0:
#         print("Exiting...")
#         break
#     elif choice == 1:
#         c = add.add()
#     elif choice == 2:
#         d = sub.sub()
#     elif choice == 3:
#         e = mul.mul()
#     elif choice == 4:
#         f = div.div()
#     elif choice == 5:
#         g = mod.mod()
#     elif choice == 6:
#         h = floordiv.floordiv()
#     elif choice == 7:
#         i = expo.expo()
#     else:
#         print("Invalid choice. Please try again.")

# print("Finished 10 iterations. Exiting...")















print("Welcome to Calculator")
print(" 0- Exit\n 1- Add\n 2- Sub\n 3- Mul\n 4- Div\n 5- Mod\n 6- FloorDiv\n 7- Expo")

import add, sub, mul, div, mod, floordiv, expo

i=1
while i<=10:
    print(f"----Attempt: {i}----")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 0:
        print("Exiting...")
        break
    elif choice == 1:
        c = add.add()
        
    elif choice == 2:
        d = sub.sub()
        
    elif choice == 3:
        e = mul.mul()
        
    elif choice == 4:
        f = div.div()
        
    elif choice == 5:
        g = mod.mod()
        
    elif choice == 6:
        h = floordiv.floordiv()
        
    elif choice == 7:
        i = expo.expo()
        
    else:
        print("Invalid choice. Please try again.")
    i+=1
print("Finished 10 iterations. Exiting...")




