age=int(input("Enter your age: "))
citizinship=input("Enter your citizinship:")

if age>=18:
    if citizinship=="INDIA" or citizinship=='india' or citizinship=="India":
        print("You are eligible for vote")
    else:
        print("You are not eligible for vote")    
else:
    print("Not eligible for vote")    