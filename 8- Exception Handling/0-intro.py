
'''
Exception Handling:
When an error occurs, or exception as we call it
Python will normally stops and generate an error message.

The Try block lets you test a block of code for errors.

The except blocks lets you handel the error.

The else block  lets you execute code when there is no error.

The finally block lets you execute code,
regardless of the result of the try - and except blocks.
'''
# print("----------try except---------")
# print("hi")
# try:
#     print(x)
# except:
#     print("An error occured")

# print("hi")

# print("------multiple except------")


# try:
#     print(x)

# except NameError:
#     print("Name error occured")
# except:
#     print("An error occured")

# print("hi")
# print("hi")



# print("-------else-------")
# try:
#     print('x')
# except:
#      print("Name error occured")
# else:
#     print("All good")

# print("-------finally-------")
# try:
#     print(x)
# except:
#      print("Name error occured")
# else:
#     print("All good")
# finally:
#     print("I don't care I will run")


'''

You work for a housekeeper who is responsible for 
tracking daily temperature readings. 
She receives a list of 30 days of temperature data, 
but some of the readings are in string format. 
Your job is to find out how many days
had temperatures above 25°C, 
as those are the days the housekeeper
needs to take extra precautions.

temperatures = [22, "30", "25", "29", "not available", "20", "35"]

'''
temp=  [22, "30", "25", "29", "not available", "20", "35"]
l=[]
for x in temp:
    try:
        if int(x) > 25:
            l.append(x)
    except ValueError:
        continue

print(l)
