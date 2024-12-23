#check the no. given by user is divisible by 5 or not

number=int(input("Enter the no."))

if(number%5==0 and number%10==0):
    print(f"The given no.:{number} divisible by 5 and 10")
else:
    print(f"The given no.:{number} is not divisible by 5 and 10")    