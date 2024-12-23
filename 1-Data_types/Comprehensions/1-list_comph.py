'''
List Comprehension:
    List comphresion offers a shorter syntax when you want to
    creates a new list or new list based on based on the values on an exixting list.
'''
l=[x for x in range(11)] # x is the value where we stored the range value.
print(l)

l=[x for x in range(11,-1,-1)]
print(l)

#list a o no. bet 20-30 using list comprehension
l=[x for x in range(20,30)]
print(l)

# list of nos. between 50-25 using
l=[x for x in range(50,25,-1)]
print(l)


#even no. betwwen 0 to 10
l=[x for x in range(11) if x%2 == 0]
print(l)


# odd no between 20-30 using list comprehension
l1=[x for x in range(20,30) if x%2 != 0]
print(l1)

#....................................................

# do this in existing list

l=[1,2,3,4,5,6,7,8,9,10,11,12,1,3,14,15]
l1=[x for x in l if x%2==0]
print(l1)

l=[1,2,3,4,5,6,7,8,9,10,11,12,1,3,14,15]
l1=[str(x)+" : even" if x%2==0 else str(x)+" : odd" for x in l]
print(l1)

#create a list of even index elements on the list[1,2,3,4,5,6,7,8,9,10]
#create a list of odd index elements on the list[1,2,3,4,5,6,7,8,9,10]
#create a list of square of each elements on the list[1,2,3,4,5]
print('\n')
#even indexed
l=[1,2,3,4,5,6,7,8,9,10]
l1=[l[x] for x in range(len(l)) if x%2==0] #x is works as what you want to print
print(l1)

#odd indexed
l=[1,2,3,4,5,6,7,8,9,10]
l1=[l[x] for x in range(len(l)) if x%2!=0]
print(l1)

#square
l=[1,2,3,4,5]
l1=[x**2 for x in l]
print(l1)

#cube
l=[1,2,3,4,5,6]
l1=[x**3 for x in l if x%2==0]
print(l1)


