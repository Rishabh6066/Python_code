# Identity op : is , is not

x=['a','b']
y=['a','b']

z=x

print(x is z) # True: x and z are same objs
print(x is y) #

print(x==y) # True: Content of x and y is same

print(['a','b'] is x) #False
print(['a','b'] is not x) # true

print(x is not z) #false
print(x is not y) #true

w=[1,2]
w=x
print(x is w) #true