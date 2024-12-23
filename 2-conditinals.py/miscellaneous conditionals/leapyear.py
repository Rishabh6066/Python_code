
# year=int(input("Entert the Year:"))

# if year%400==0:
#     if year%4==0 and year%100!=0:
#         print("This is leap year")

# else:
#     print("The year is not a Leap year")        

year = int(input("Enter the Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("This is a leap year")
else:
    print("The year is not a leap year")

'''
Output-

Enter the Year: 2017
The year is not a leap year

Enter the Year: 2020
This is a leap year

Enter the Year: 2024
This is a leap year

'''    
