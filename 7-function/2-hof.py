'''
Higher order function:
A higher order function is a function that either takes one or more functions as arguments,
returns a function, or both. Thee functions are widely used in a functional programing
and allow for more flexible and reusable code.
'''
'''
HOF types-

1- Map:
The map function applies a given function to each element in a collection
(like a list) and returns new collection with the transformed elements.

Syntax:
map(function(),iterable)
'''

'''
map is the alternate of this-
l1=[]
def add(x):
   return x+1

for x in l:
   l1.append(add(x))
print(l1)      
'''
l=[1,2,3,4,5]

def square(x):             #1,2,3,4,5
    return x*x             #1,4,9,16,25
x=list(map(square,l))      #1,4,9,16,25
print(x)

def add(x):
    return x+2
y=list(map(add,l))
print(y)

def sub(x):
    return x-4
y=list(map(sub,l))
print(y)

def mul(x):
    return x*2
y=list(map(mul,l))
print(y)

def div(x):
    return x/3
y=list(map(div,l))
print(y)


# # map using lambda function

l=[1,2,3,4,5]
y=list(map(lambda x : x+2,l))
print(y)

y=list(map(lambda x : x*2,l))
print(y)

y=list(map(lambda x : x/2,l))
print(y)

y=list(map(lambda x : x*x,l))
print(y)

y=list(map(lambda x : x-2,l))
print(y)

# update this list each elements by 5 using map and lambda
#[12,22,32,42]

l=[12,22,32,42]
z=list(map(lambda a: a+5,l))
print(z)

#....................................
print("here start multiple iterable")
# multiple iteration in map
l=[1,2,3,4]
l1=[5,6,7,8]

def add(x,y):  #1,5  #2,6  #3,7   #4,8
    return x+y   #6    #8    #10   #12

y=list(map(add,l,l1)) #[6,8,10,12]
print(y)

#sub l and l1 elements using map
# o/p:[4,4,4,4]

def sub(x,y):
    return x-y

y=list(map(sub,l1,l))
print(y)


# multiple iteration in map with lambda

y=list(map(lambda x,y : x+y ,l,l1))
print(y)

y=list(map(lambda x,y : x-y ,l1,l))
print(y)
