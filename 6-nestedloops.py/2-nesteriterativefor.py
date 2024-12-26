
l=[[10,11,12,13,14],[0,1,2,3,4]]


for x in l:
    for y in x:
        print(y)



#flateen list imp
l = [21, 28, 30, [10, 11, 12, 13, 14], [0, 1, 2, 3, 4]]
flatten_list = []

for x in l:
    if isinstance(x, list):
        for y in x:
            flatten_list.append(y)
    else:
        flatten_list.append(x)

print(flatten_list)

# "isinstance" inbuilt fun to check the data is the given datatype or not

#l=[21,28,30,(0,1,2,3,4)]
#outpur- [21,28,30,0,1,2,3,4]
l1=[21,28,30,(0,1,2,3,4)]
for x in l1:
    if isinstance(x, tuple):
        for y in x:
            flatten_list.append(y)
    else:
        flatten_list.append(x)

print(flatten_list)



#l=[21,28,30,(10,11,12,13,14),[0,1,2,3,4]]
#[21,28,30]
l2=[21,28,30,(10,11,12,13,14),[0,1,2,3,4]]
for x in l2:
    if isinstance(x, tuple):
        for y in x:
            flatten_list.append(y)
    elif isinstance(x, list):
        for y in x:
            flatten_list.append(y)        
    else:
        flatten_list.append(x)

print(flatten_list)