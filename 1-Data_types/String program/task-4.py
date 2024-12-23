'''
WAP a program to print a Dictionary of count of characters in
a string given by user.

Eg: i/p: 'Hello'
o/p: {'H':1 ,'e':2 , 'l':2, 'o':1}
'''

s="Ramesh Pawar"
d={}

for x in s:
    if x not in d:
        d[x]-1
    else:
        d[x]+=1
print(d)            