s="I am in Mirzapur"

print(s.upper())

print(s.lower())

s="   I am from Uttar Pradesh    "

print(s.strip()) # removes the whitespace from start and end

#replace
a="Hello World!!"
print(a.replace('W','w'))

a="Hello and welcome.Jeff!!"
print(a.replace('Jeff','Bob'),id(a))
a=a.replace('jeff','Bob')
print(a,id(a))


#split
a="Hello,World!"
print(a.split(","))
