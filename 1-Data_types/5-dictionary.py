'''
4)  Mapping Type:

Dictionary :
    collection of heterogenous (different) data,
    which is indexed(key is the index) or ordered ,
    which is mutable(changeble),
    it allows duplicate values,
    elements written in curly brackets '{}'
    elements are (key:value) pair

    '''

d={'a':1,'b':4,'c':'jeff','d':1}
print(d)

print(d.keys())
print(d.values())
print(d.items())
print(d['a'])

#Which datatype is use as a key: tuple

#slicing
print(d['c'])
print(d['b'])

car={
    'brand':'tata','year':2024,
     'model':{1:'tiger',2:'nano',3:'neo'}
}

print(car['model'][2])

#updating the value
car['year']=2020
print(car)

car.update({'year':2000})#while updating in dictionary we have to write
print(car)              #in curly brackets

# user={
#     'name':"jeff",
#     'email':'jeff@gmail.com',
#     'mobile':[7634783,36746238,7834687,4789298]
# }

# print(user['mobile'][2])

# #add element
# car={
#     'brand':'tata','year':2024,
#      'model':{1:'tiger',2:'nano',3:'neo'}
# }

# car['price']=20000
# print(car)




# #removing elements

# car.pop('color')
# print(car)

# car.popitem() #this function removes the last element
# print(car)

# del car['year']
# print(car)

# car.clear()
# print(car)

# #del car
# print(car)
'''print(car)
NameError: name 'car' is not defined. 
'''
car={
    'brand': 'tata', 'year': 2024, 
 'model': {1: 'tiger', 2: 'nano', 3: 'neo'}, 
 'price': 20000, 'color': 'black'
 
}

k=('year','model')
d=car.fromkeys(k) # value as None
print(d)

v=0
d=car.fromkeys(k,v)
print(d)

x=car.get('color')
print(x)

print(car.get('color'))

print(car.get('moblile')) #None

