'''

Write a Python program to check whether a given number is a prime number.

'''
n=int(input("Enter the no.: "))
flag= True
if n==1:
    print(f"{n} is not prime")
else:
    for i in range(2,n):
        if n % i==0:
            flag= False
            break
    if flag==True:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")        


   