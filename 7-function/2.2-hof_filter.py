'''
2- Filter
  The filter function selects elements
  from a collection (eg : list) based
  on whether they satisfy a
  given condition (evaluates to true)

  Syntax:
  filter(functions,iterable)
'''
l=[1,2,3,4,5,6]

def is_even(x):
    if x %2 ==0:
        return x
    
x=list(filter(is_even,l))
print(x)    

# print a list of oddnos from the list using filter
#[11,32,34,35,54,57]

l=[11,32,34,35,54,57]

def is_odd(x):
    if x%2!=0:
        return x

x=list(filter(is_odd,l))    
print(x)


#filter with lambda

x=list(filter(lambda x:x%2==0,l))
print(x)

y=list(filter(lambda x: x%2!=0,l))
print(x)
