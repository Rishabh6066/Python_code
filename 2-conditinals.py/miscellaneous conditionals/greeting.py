'''What greeting do you receive based on the time of day given by user

(Good morning, Good afternoon, Good evening, Good night) (24 hours time format)
'''

time = int("input(Enter the time in 24-hour format (0-23): ")

if 0 <= time < 6:
     greeting = "Good night" 
     elif 6 <= time < 12: 
        greeting = "Good morning"
     elif 12 <= time < 18: 
        greeting = "Good afternoon" 
     elif 18 <= time < 22: 
        greeting = "Good evening" 
     elif 22 <= time <= 23: 
        greeting = "Good night" 
     else:
        greeting = "Invalid time. Please enter a time between 0 and 23."

print(f"The unique list is: {unique_list}"     