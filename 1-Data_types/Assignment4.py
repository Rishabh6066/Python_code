
# '''
# Create one heterogenous list. 
#     Perform positive indexed slicing , negative index slicing, positive range slicing, negative range slicing, step slicing, reverse of a list 

# '''

list=[3,5,6,3,8.5,6,7.4,True,'a','b','123',False,19.5]
# print(list)
# print(len(list))

# print('Postive index slicing')
# print(list[5])
# print(list[10])
# print(" ")

# print('Negative index slicing')
# print(list[-5])
# print(list[-13])
# print(" ")

# print('+ve range slicing')
# print(list[:5])
# print(list[::2])
# print(list[1:12])
# print(" ")

# print('-ve range Slicing')
# print(list[-11:-1])
# print(list[:-4])
# print(list[-1:])

# print('Steps Slicing')
# print(list[-13:-5:3])
# print(list[::-2])
# print(list[2:15:5])
# print(list[-13:-1:2])
# print(list[-1:-13:-2])
# print(" ")

# print ('Reverse the list')
# print(list[::-1]) #reversing
# print(list[::-2])
 
# list=[3,5,6,3,8.5,6,7.4,True,'a','b','123',False,19.5]
# print(f"Performing remove() and pop()")
# print("List:",list)
# print("performing remove()")
# list.remove(8.5)
# print(list)
# list.remove(False)
# print(list)
# print("Performing pop()")
# list.pop(4) # delete the index 4
# print(list)
# list.pop() # without argument it will delete the last element
# print(list)

# print(f"Performing append() and insert() :")

# print("List :",list)
# print("Perform append() operation:")
# list.append([2,4,3])
# print(list)
# list.append(3.5)
# print(list)
# print('')
# print(list)
# print("perform insert() operation:")
# list.insert(4,'abc')
# print(list)
# list.insert(9,[4,5,'b'])
# print(list)

# print("Performing del() and clear :")
# print("List: ",list)
# del list[2] # del index 2
# print(list)
# del list[-1] # del index -1
# print(list)

# del list[2:5] #range
# print(list)

# del list[-5:-10:2]
# print(list)

# print("Perform the Clear()")
# list.clear() # it will clear all the elements in list
# print(list)

# del list
# print(list)

Codenera= []
 # taking details
print("Taking Details: ")
print(" ")
id=input("Enter your id: ")	
name=input("Enter your name: ")
email=input("Enter your email: ")
mobile=input("Enter your mobile: ")
salary=input("Enter your salary: ")
experience=input("Enter your experience: ")
designation=input("Enter your designation: ")
address=input("Enter your address: ")
city=input("Enter your City: ")
state=input("Enter your state: ")


# puting this into list
Codenera.append(id)
Codenera.append(name)
Codenera.append(email)
Codenera.append(mobile)
Codenera.append(salary)
Codenera.append(experience)
Codenera.append(designation)
Codenera.append(address)
Codenera.append(city)
Codenera.append(state)

# Creating the complete profile using an f-string 
profile = f""" Employee Profile:
-----------------
 ID: {Codenera[0]} 
 Name: {Codenera[1]} 
 Email: {Codenera[2]} 
 Mobile: {Codenera[3]} 
 Salary: {Codenera[4]} 
 Experience: {Codenera[5]} 
 Designation: {Codenera[6]} 
 Address: {Codenera[7]} 
 City: {Codenera[8]} 
 State: {Codenera[9]} """
 
print(profile)






