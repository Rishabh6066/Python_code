'''
set type:
3) set:
   Collection of hetrogenous(different) data,
   which is unindexed or unordered,
   mutable(changable)
   duplicate values are not allowed  (only unique values are allowed)
   elements written in curly brackets '{}'
'''

# s={1,5.6,'z', 'jeff',1,'a','d','z'}
# print(s)

# print(type(s)) #<class 'set'>

# s1={1}
# print(type(s1))# <class 'set'>

#set() convert the given datatype in unique elements data
 # i/p l=[1,2,3,1,2,3,1,2,3]
 # o/p l=[1,2,3]
l=[1,2,3,1,2,3,1,2,3]

# l=set(l)
# print(l)

# l=list(l)
# print(l,type(l))
'''
#we can solve the above question like this to
l=list(set(l))
print(l,type(l))
'''
# t=(1,2,3,1,2,3)

# t=tuple(set(t))
# print(t)

'''
t=set(t)
t=tuple(t)
print(t)
'''

#perform mutation sets

#1) addind the elements

# s={1,7,3,5,'a','jeff','d','b'}
# print(s)

# s.add(5)
# print(s) #it will update the 5 in set but unorderly

# #2) Update

# s.update({'A',3})
# print(s)

# s.update(['G',8])
# print(s)

'''
s.add({'s','f'})
print(s)

TypeError: unhashable type: 'set'
'''

'''
s.update(1)
print(s)

TypeError: 'int' object is not iterable
'''

# s.update("jefff")
# print(s)
#niterables can be updated in sets using set()
# str,list,tuple,set are  iterable
# int,float are not iterables

#3) delete elements

# s={1,7,'a',4.5,0,'f'}
# print(s)

# s.remove('a')
# print(s)

# s.discard('f')
# print(s)
# '''
# s.remove('t')
# print(s)

# Keyerror: 't'
# '''
# s.discard('t')
# print(s)
# #if we will try to delete  a value which is not in the set.
# # remove() will give 'KeyError' error
# # discard() will not give any error

# s.pop()
# print(s)
# #as set is unordered
# #so when using pop()
# #you dont know which item gets removed

# s.clear()
# print(s)

# del s

# '''print(s)
# NameError: name 's' is not defined
# '''

# #Join two or more set

#1) Union
# we can crete multiple set and union them

s1={1,2,3}
s2={4,5,6}

s3=s1.union(s2)
print(f"s3:{s3}, s1:{s1}, s2:{s2} Using Union")

s1.update(s2)
print(f"s1:{s1}, s2:{s2},using update")

# #difference between union and update
# #uniion() return a new set
# #update() modifies the original set

# # 2) Intersection

# s1={1,2,3}
# s2={2,4,5}

# s3=s1.intersection(s2)
# print(s2)
# #intersection() returns a new set
# # which will have common elementsof both the set

# s1.intersection_update(s2)
# print(s1)

# # intersection_update() updates the existing set
# # which will have common elements of bothe the set

# 3) difference

s1={1,2,3}
s2={2,4,5}

s3=s1.difference(s2)
print(s3)

s4=s2.difference(s1)
print(s4)
#difference() returns a new set
# new_set=first_set.difference(second_set)
#which will have different elements of first_set from second_set

s3=s1.symmetric_difference(s2)
print(s3)
#symmetric_difference() returns a new set
#which will have different elements of both the set

s1.symmetric_difference_update(s2)
print(s1)
#symmetric_difference_update() updates exixting set
# which will update different elements of both the sets. 

