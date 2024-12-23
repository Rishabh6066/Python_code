'''Sequence Type:
2) Tuple:
  Collection of hetrogenous(different) data,
  which is indexed or ordered,
  immutable(unchangable)
  allows duplicatesvalue
  elements written in squre brackets '()'
'''
# t=(1,2,3,5.6,'a')
# print(t)
# print(type(t)) # <class 'tuple'>

# t=(1)
# print(type (t)) #< class 'Int>

# t=(1,) # if we seprated by , the it will be tuple
# print(type(t)) #< class 'Int>


tuple=(3,5,6,3,8.5,6,7.4,True,'a','b','123',False,19.5)
 #perform slicing

print('Postive index slicing')
print(tuple[5])
print(list[10])
print(" ")

print('Negative index slicing')
print(tuple[-5])
print(tuple[-13])
print(" ")

print('+ve range slicing')
print(tuple[:5])
print(tuple[::2])
print(tuple[1:12])
print(" ")

print('-ve range Slicing')
print(tuple[-11:-1])
print(tuple[:-4])
print(tuple[-1:])

print('Steps Slicing')
print(tuple[-13:-5:3])
print(tuple[::-2])
print(tuple[2:15:5])
print(tuple[-13:-1:2])
print(tuple[-1:-13:-2])
print(" ")

print ('Reverse the tuple')
print(tuple[::-1]) #reversing
print(tuple[::-2])
 


# what is difference between list and tuple
'''Ans- 
1- list is mutable while tuples are immutable
2- we can do change in list but not in tuple,
3- the function like append extend pop insert
 del keyword will not work in tuple
 nither we can update any value in tuple
4- list is written in [] while tuple in written in ()
5- tuple is faster that list.
6- tuple is memory efficient than list.
7- we can use tuple as key in dictionary.

example of tup llatitude , logitude
''' 

t1=(1,2,3,4)

'''
t.append(5)
print(t)

# attributeError : 'tuple' object has no atribute 'append'
# attributeError : 'tuple' object has no atribute 'pop'
# attributeError : 'tuple' object has no atribute 'reomove'
# attributeError : 'tuple' object has no atribute 'clear'
# attributeError : 'tuple' object has no atribute 'reomove'
# attributeError : 'tuple' object has no atribute 'insert'

# '''

# '''
# del t[2]
# print(t)
# TypeError: 'tuple' object doesn't support item deletion
# '''

# '''
# del t
# print(t)
# NameError: name 't' is not defined

# *** It works because del is permanently deleating the tuple
#     not making any changes.
# '''
t1 = (1,2,3)
t2=(4,5,6)
t3= t1 + t2
print(t3)

print(id(t1)) # 2365249257152 on this address in memory

t1= t1 + t2
print(t1)
print(id(t1)) # 2365248430592 on this address in memory
#so t1 and t1=t1 + t2 are on different memory location

t4= t2 * 3
print(t4)

'''
if you want to make changes in tuple then you have to 
type cast it
'''
t=(1,2,3,4,5,6,7)
print(t,type(t))

t=list(t)
print(t,type(t))

t.append(8)
print(t)

t=tuple(t)
print(t,type(t))