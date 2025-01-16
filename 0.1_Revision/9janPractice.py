'''
1) Extracting a Torn Map:  
   A torn piece of the pirate map is stored as a nested list:  
   map_piece = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']].  
   - Slice to extract only the diagonal elements ['A', 'E', 'I'].
'''
map_piece = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

print(list(f"{map_piece[0][0]}{map_piece[1][1]}{map_piece[2][2]}"))

'''
2) take full name from user
check it has first name  , middle name and last name 
else give error message
if correct print 
first name : 
middle name:
last name :

'''
full_name=input("Enter your full name: ")

name=full_name.split(" ")

if len(name)==3:
    print(f" first name: {name[0]}\n middle name: {name[1]}\n last name: {name[2]}")
else:
    print('error')    

'''
3)
Create a User Authentication system

0- Registration 
1- Login
3- Logout
take choice from user

if 0

ask user to give email and password
store it in users dictionary as key and password

if 0
ask user to give email and password 
check that pair is in users 
if then print welcome email string part before @

if 3 
print thanks and
close the app
'''
print("______User Auhentication System________")
print(" Press Button")
print()
if 'choice'==0:
