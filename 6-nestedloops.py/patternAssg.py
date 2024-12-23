'''
Write the programs to print the given patterns

*
**
***
****
*****

*****
****
***
**
*

1
12
123
1234

1234
123
12
1 	

        *
      * *
    * * *
  * * * *
* * * * *


*
**
***
****
****
***
**
*


1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


1 2 3 4 5
1 2 3 4
1 2 3
1 2
1


1
12
123
1234
1234
123
12
1




*
* #
* # *
* # * #
* # * # *
'''

#1 pattern

for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print() 

'''
output-
*
**
***
****
*****
'''
print('\n')
#2nd pattern
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print() 

'''
output-
*****
****
***
**
*

'''
print('\n')
#3rd pattern

for i in range(4):
    for j in range(i+1):
        print(j+1,end="")
    print()    
'''
output-
1
12
123
1234
'''
print('\n')
#4th pattern

for i in range(4):
    for j in range(4-i):
        print(j+1,end="")
    print()  

'''
output-
1234
123
12
1
'''

print('\n')
#5th pattern
for i in range(5): # for rows
    for j in range(5-i): #for space
        print(" ",end=" ")
    for k in range(i+1): # for star
        print("*",end=" ")
    print() 

'''
Output-
        *
      * *
    * * *
  * * * *
* * * * *
'''
print('\n')
#6th pattern
for i in range(4):
    for j in range(i+1):
        print('*',end="")
    print()
#for decinding
for l in range(4):
   for k in range(4-l):
      print("*",end="")
   print() 

'''
output-

*
**
***
****
****
***
**
*
''' 
print('\n')
#7th pattern  
for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")
    print()    
'''
Output-

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''

print('\n')
# 8th pattern  
for i in range(5):
    for j in range(5-i):
        print(j+1,end=" ")
    print()

'''
Output-
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

print('\n')
#9th pattern
for i in range(4):
    for j in range(i+1):
        print(j+1,end="")
    print()
#for decending
for l in range(4):
   for k in range(4-l):
      print(k+1,end="")
   print() 
'''
Output-
1
12
123
1234
1234
123
12
1
'''
print('\n')
#10th pattern
for i in range(5):
    for j in range(i+1):
        if j % 2 == 0: 
            print('*', end=" ")
        else:
            print('#', end=" ")
    print()

'''
output-
*
* #
* # *
* # * #
* # * # *
'''

        
   

