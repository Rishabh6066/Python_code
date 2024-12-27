'''
Enumerate:
  The enumerate function adds a counter to 
  an iterable and returns it as an enumerate object.
  It is commonly used to iterate through a sequence
  while keeping track of the index.
'''

l=[11,31,70,48,35]
for index,value in enumerate(l):
    print(index,value)

print()
t=(11,234,345,321,678,432)
for index,value in enumerate(t):
    print(index,value)

print()
s={11,234,345,321,678,432}
for index,value in enumerate(s):
    print(index,value)

print()
d={1: 'a', 2: 'b', 77: 'g', 48: 'i' }
for index,value in enumerate(d):
    print(index,value)        

print()
s=" I am from Mirzapur"
for index,value in enumerate(s):
    print(index,value)     