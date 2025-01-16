'''
zip():
     The zip() function in python is 
     used  to combine multiple iterable (like list ,tuple , etc.)
     elements by elements. It returns an iterator of tuples,
     where each tuple contains the elements from 
     all the iterables at the same position.
     The function steps when the shortest iterable is exhausted.

Returns a zip objects

syntsx:
zip(iterable1. iterable2, ...)
'''
l1=[1,2,"3",4]
l2=['3',5,7,7]
l=list(zip(l1,l2))
print(l)

# l1=
# l2=