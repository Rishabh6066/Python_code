#saturday test

#performing Swapping
#Take two input from user
a=int(input("Enter the first number:"))
b=int(input("Enter the Second number:"))

print(f"Before Swapping the value of a: {a} and b: {b}")
#performing Swapping with two no.
a=a+b
b=a-b
a=a-b
print(f"After Swaping the value of a: {a} and b: {b}")


#performing arithmatic operation on that no. using assignment operator
print('performing arithmatic operation')
print(f"first no: {a} second no.: {b}")
a= 4 #update first no. by 4
print(a)

b-=2 # subtract second no. by 2
print(b)

a*=5 # multiply first no. by 5
print(a)

b/=6 #divide by second no. by 6
print(b)

a%=2 # amod first no. by 2

b//=2 # floor div second no. by 2

# perform comparison operation
print('perform comparison operation')
print(f"first no: {a} second no.: {b}")

a>b

a<b

a==b

a!=b

a<=b

a>=b

#perform logical operation
print('perform logical operation')
print(f"first no: {a} second no.: {b}")

print(a>=b and a==b ) #  performing and

print(not(a<b and a!=b)) # performing not

s="I love Mumbai"

new="am"
print(new in s) #apply in 
print(new not in s) #apply not in


#Performing bitwise operator
print('perform bitwise operation')

print(10 & 7)
'''
1010
0111 &
-----
0010   #output is 2
'''


print(3 or 1)
'''
0011
0001 or
-----
0011   #output is 3
'''

print(10^2)
'''
1010
0010 ^
-----
1000   #output is 8
'''

c=11
print(~(c)) #output: -12

print(12 << 2) #output: 48

print(3 >> 2) # output : 0

# perform identity operation
print('perform identity operation')

x=['a']
y=['b']
z=x
#perform is operation
print(x is z) # true
print(x is y) # false

#perform is not operation
print(x is not z) #false
print(x is not y) #true








