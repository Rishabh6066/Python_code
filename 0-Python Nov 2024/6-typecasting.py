# Conter one datatype to another
a=10
print(type(a))

b=5.6
print(type(b))

c="Rahul"
print(type(c))

d=str(a)
print(d)
print(type(d))

e=int(b)
print(e)
print(type(e))

f=float(a)
print(f)
print(type(f))

g= a + b
print(g)

# h= d + e
# print(h)
# '''
# h= d + e
#        ~~^~~
# TypeError: can only concatenate str (not "int") to str
# '''
i= c + d
print(i)