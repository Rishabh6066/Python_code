#take full name from user
fullname= input("Enter Your Full name:  ")

#check the full name contains
name=fullname.split(' ')
if len(name)==3:
    print(f"First name: {name[0]} ,\n Middle name: {name[1]} ,\n Last name: {name[2]}")
else:
    print("error")    


#Eg. : 'Jeff Daniel Bazos'
#print:
# first name: jeff
# middle name: Daniel
# last name : Bazos

#else give error
#full name must contain first name , middle name, last name