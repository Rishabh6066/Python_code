'''
3-Reduce:
   The Reduce function applies a binary function
   (a functiion that takes two arguments)
   cummulatively to the elements of collection,
   reduce it to a single value.
   It is found in the functools module in python.

  Syntax:
  from functools import reduce
  reduce(function , iterables , initializer= None) 
'''

from functools import reduce
l=[1,2,3,4,5]

def add(x,y):
    return x + y

a= reduce(add,l) #0,1,3,6,10,15
print(a)

a= reduce(add,l,10) # 10,11,13,16,20,25
print(b)
