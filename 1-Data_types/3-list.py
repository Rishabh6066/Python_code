
# #Sequence type:

'''
list:
Collection of hetrogenous(different) data,
which is indexed or ordered,
mutable(changable)
allows duplicatesvalue
elements written in squre brackets[]
'''
l=[1,2,3.4,1,2,'a',True]
print(l)
print(type(l))

print(len(l)) #count the value of list

#slicing
#nameof_datatype[index]

print(l[5])
print(l[3])

# -ve indexing
print(l[-1])
print(l[-5])
print(l[-7])

# slicing using range

print(l[2:5]) # will stat from 2 but it will exclude 2
# Output: 2,3.4

print(l[3:6])

print(l[:6])

print(l[1:])

print(l[-4:-1])

print(l[-2 : -5])

# print 1 to "a" and 3.4 to true using -ve indexing
# Note: -ve indexing always start with left to right


print(l[:]) # it will giv all the list

# datatype[start_index : end_index : ]
# default value: [0 : len[l] : 1]
print(l[::1])

print(l[::2])

print(l[::-1]) # reverse the list

print(l[::-2])

print(l[::-2])

print(l[:-1:2])

#..............................................................
#Mutation Ecaxmple Wolverine (they are changable)

l.append(42)  # adding one element at last but as a index
print(l)
print("extend")
l2=[5,8]
l.extend(l2) # adding multiple element in list
print(l)

#exaple
l.append([22,11])
print(l)
print(l[10])
#Note:
# append create single index at the end of the list
# extend create multiple index at the end of the list

#..............................................
l.insert(3,'one')
#if we want to add the value in the middle then we use insert
#Note: it will add "one" at index 3 and rest will shifted 
#it will not update the value
l.insert(3,['t','s'])
print(l)

#.......................................
#Update
print("update")
l[3] = 0
print(l)
#
#two value update
l[3:5]= 0,3
print(l)

#what if we do this
#if we put extra value then it will shift
l[3:5]= 'abc','123',6

#........................................
#delete have 3 method
'''
1-remove - here we write element
2-pop - it will remove the index value here we give index.
        in pop if we dont give index it will remove last index
        pop() - not give error

3- del - del is a key word it works as slicing
'''
'''
4- clear - it is a fun it will empty the list
'''
l.remove(42) #element
print(l)

l.pop(3) # index
print(l)

'''
l.remove()
TypeError: list.remove( takes exactly one argument)
'''
l.pop() # it will delete the last value

del l[3] #del is a keyword
print(l)

# -ve index , range , step

del l[-3] #-ve index
print(l)

del l[-3:-5] # range
print(l)

del l[-2::2] # step
print(l)

l.clear()
print (l)

del l # it will del the whole list

print(l)

list=[1,3,4,7,9,34,78,22]

print(len(list))

print(max(list))

print(min(list))

print(sum(list))

list.sort(reverse=True)
print(list)

a=['a','z','c']

a.sort()
print(a)

print(min(a))
print(max(a))

a.sort(reverse=True)
print(a)

li=[3,6,3,8,4]
li.reverse()
print(li)

l2=[1,4,0,57,3,4,9,2]
l2.sort(reverse=True)
print(l2)

#..............................

l3=[2,4,5,3,4,1,6,7,3,2]

print(l3.count(3))
print(l3.count(7))

print(f'5 is at index: {l3.index(5)}')

print(l3.index(4,2,7)) # index of 4 in range 2 to 7
                       # (element,start,end)


#Concatinate or merge

l4=[1,2,3]
l5=[4,5,6]
l7=[4,5,6]
l6= l4 + l5 + l7
print(l6)

# product a list

l8= l4 * 3
print(l8)

l9= l4 * 0
print(l9)

