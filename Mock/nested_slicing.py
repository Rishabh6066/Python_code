'''l=[1,2,3,[11,41,'William',(42,60,('III'),42)],['a','f',('Henery','b','d')],('jeff','Gates'),60]

o/p: William Henery Gates III   

using slicing'''

l=[1,2,3,[11,41,'William',(42,60,('III'),42)],['a','f',('Henery','b','d')],('jeff','Gates'),60]

print(l[3][2],end=" ")
print(l[4][2][0],end=" ")
print(l[5][1],end=" ")
print(l[3][3][2],end=" ")