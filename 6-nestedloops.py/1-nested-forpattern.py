# nested for

for x in range(6):
    for y in range(6):
        print('* ',end=" ")
    print() 

'''
* * * * * *   x=0   y=0,1,2,3,4,5
* * * * * *   x=1   y=0,1,2,3,4,5
* * * * * *   x=2   y=0,1,2,3,4,5
* * * * * *   x=3   y=0,1,2,3,4,5
* * * * * *   x=4   y=0,1,2,3,4,5
* * * * * *   x=5   y=0,1,2,3,4,5
* * * * * *   x=6   y=0,1,2,3,4,5
'''
print('\n')
for x in range(6):
    for y in range(6):
        print('*',"(",x,',',y,")",end=" ")
    print() 

'''
x/y  |   0      1       2        3       4      5  
-----------------------------------------------------
0    | *(0,0)  *(0,1)  *(0,2)   *(0,3)  *(0,4) *(0,5)
1    | *(1,0)  *(1,1)  *(1,2)   *(1,3)  *(1,4) *(1,5)
2    | *(2,0)  *(2,1)  *(2,2)   *(2,3)  *(2,4) *(2,5)
3    | *(3,0)  *(3,1)  *(3,2)   *(3,3)  *(3,4) *(3,5)
4    | *(4,0)  *(4,1)  *(4,2)   *(4,3)  *(4,4) *(4,5)
5    | *(5,0)  *(5,1)  *(5,2)   *(5,3)  *(5,4) *(5,5)
6    | *(6,0)  *(6,1)  *(6,2)   *(6,3)  *(6,4) *(6,5)
''' 
print('\n')
for x in range(6):
    for y in range(x+1):
        print('* ',end=" ")
    print() 


print('\n')
for x in range(6):
    for y in range(x+1):
        print('*',"(",x,',',y,")",end=" ")
    print() 

'''
x/y  |   0      1       2        3       4      5  
-----------------------------------------------------
0    | *( 0 , 0 )
       *( 1 , 0 )  *( 1 , 1 )
       *( 2 , 0 )  *( 2 , 1 )  *( 2 , 2 )
       *( 3 , 0 ) * ( 3 , 1 ) * ( 3 , 2 ) * ( 3 , 3 )
       *( 4 , 0 ) * ( 4 , 1 ) * ( 4 , 2 ) * ( 4 , 3 ) * ( 4 , 4 )
    * ( 5 , 0 ) * ( 5 , 1 ) * ( 5 , 2 ) * ( 5 , 3 ) * ( 5 , 4 ) * ( 5 , 5 )
'''

#try this pattern

'''
0
1 1
2 2 2
3 3 3 3
4 4 4 4 4
5 5 5 5 5 5

'''

'''
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5

'''

for i in range(6):
    for j in range(i+1):
        print(i, end=" ")
    print() 

print('\n') 

for i in range(6):
    for j in range(i+1):
        print(j, end=" ")
    print() 

'''
1
2 3
4 5 6
7 8 9 10
'''
print('\n')
k=1
for i in range(4):
    for j in range(i+1):
        print(k, end=" ")
        k+=1
    print()  



print('\n')

n=5
for x in range(n):
    for y in range(n-x-1,-1,-1):
        print("* ",end=" ")
    print()
'''
Output-

*  *  *  *  *  # x=0 y=5-0-1=4; 4-0
*  *  *  *     # x=1 y=5-1-1=3; 3-0
*  *  *        # x=2 y=5-2-1=2; 2-0
*  *           # x=3 y=5-3-1=1; 1-0
*              # x=4 y=5-4-1=1; 0
'''    

# another method
print('\n')
n=5
for x in range(n):
    for y in range(n-x):
        print("* ",end=" ")
    print()

'''
Output-
*  *  *  *  *  # x=0  y=5-0=5;   4-0
*  *  *  *     # x=1  y=5-1=4; 3-0
*  *  *        # x=2  y=5-2=3; 2-0
*  *           # x=3  y=5-3=2; 1-0
*              # x=4  y=5-4-1=1; 0

'''

#try this

'''
        *
      * *
    * * *
  * * * *
* * * * *     
'''
print('\n')
n=5
for x in range(n):
    for y in range(n-x-1):
        print(" ",end=" ")
    for k in range(x+1):
        print("*", end=" ")   
    print()

'''
         *
       *   *
     *   *   *
   *   *   *   *
 *   *   *   *   *
'''

n=5
for x in range(n):
    for y in range(n-x-1):
        print(" ",end=" ")
    for y in range(x+1):
        print(' * ',end=" ")
    print() 

'''
A
B C
D E F
G H I J
K L M N O

'''

# ASCII : Is American Standard Code for Information Interchange

# it is character encoding standard 

# used to represent text in 

# computer,telecommunicational devices and other devices

# ASCII is a 7-bit code, it can represent 128 characters

# Upper case letters A-Z lowecase letters a-z 

# numbers 0-9 special characters 

# basic punctuational symbols

# only 95 out of 128 code points are printable characters

# ASCII : 65 - A , 97 - a


z=65              # ASCII : 65 - A , 97 - a
for x in range(5):
    for y in range(x+1):
        print(chr(z),end=" ")
        z+=1
    print()    

#........................................................

print('\n')
n=5
z=65
for x in range(n):
    for y in range(n-x):
        print(chr(z),end=" ")
        z+=1
    print()

'''
output-
A B C D E
F G H I
J K L
M N
O
'''   

z=65              # ASCII : 65 - A , 97 - a
for x in range(5):
    for y in range(x+1):
        print(chr(z),end=" ")
    z+=1
    print()  

'''
output-
A
B B
C C C
D D D D
E E E E E

'''

print('\n')
n=5
z=65
for x in range(n):
    for y in range(n-x):
        print(chr(z),end=" ")
    z+=1
    print()

'''
output-
A A A A A
B B B B
C C C
D D
E
'''   

#..........................................

'''
A
B B
C C C 
D D D D
E E E E E
F F F F F F
G G G G G
H H H H
I I I
J J
K

'''
print('\n')
n=6
z=65

for x in range(n):
    for y in range(x+1):
        print(chr(z),end=" ")
    z+=1
    print()
z=71
n=5   
for x in range(n):
    for y in range(n-x):
        print(chr(z),end=" ")
    z+=1
    print()     
