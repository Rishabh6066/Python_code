'''
s="i love India"

# convert the string to first alphabet capital 
# and all other alphabets to small 

a=s.capitalize()    # I love india
print(a)

# converts the string in lower case
b=s.casefold()   # i love india
print(b)

s1="I LOVE INDIA"
c= s1.isupper() # True if all the alphabets are capital  
print(c)

s2="i love python"
c= s2.islower() # True if all the alphabets are small  
print(c)


t="apple"   # o/p :"       apple      "
d=t.center(20)
print(d)

t="apple"   # o/p :"_______apple________"
d=t.center(20,'_')
print(d)


t="I love India"
e=t.count('I') # 2
print(e)

f=t.count('I',3,11) # I occured once in the inde range 3:11
print(f)



t="I love India"
g=t.find('love') # 2 ;index where the text occured in the string
print(g)

t="I love India"
h=t.find('I',3,11) # 7 ;index where the text first occured in the string
print(h)


t="I love India"
i=t.index('I') # 0 ;index where the text occured in the string
print(i)

t="I love India"
j=t.index('I',3,11) # 7 ;index where the text first occured in the string
print(j)


t="I love India"
k=t.find('z') # -1 ;if element not in string
print(k)

# t="I love India"
# k=t.index('z') 
# print(k)

# ValueError: substring not found





t="Company12"
l=t.isalnum() # "Company":True,"12":True,"Company 12":False 
print(l)

# checks if the character at unicode is decimal or not
t="\u0033"   # unicode for 3
t1="\u0047"  # unicode for G
m=t.isdecimal()
print(m)
n=t1.isdecimal()
print(n)

t="50299"
o=t.isdigit() # if all the elements are digits then True 
print(o)

t="   "
p=t.isspace()  # True if string have only spaces
print(p)

t="abc"
q=t.isalpha() # True if string have only alphabets
print(q)

t="50299"
r=t.isnumeric() # if all the elements are numbers then True 
print(r)

t="-1"
r=t.isnumeric()  # False beacuse it takes '-' as 'hypen'
print(r)

t="1.5"
r=t.isnumeric()  # False beacuse it takes '.' as 'full stop'
print(r)


t="I love India"
s=t.split(' ')  # ['I', 'love', 'India']
print(s)

t="I love India"
u=t.partition(' ')  # ('I', ' ', 'love India')
print(u)

t="I am from Pune\nI live in Baner."
v=t.splitlines() #  ['I am from Pune', 'I live in Baner.']
print(t,v)


t="Hello , I am Ramesh"
w=t.startswith('Hello') # True
print(w)
'''

s="I love Pune"
l=s.split()
l=l[::-1]
s1=" ".join(l)
print(s1)

'''
Important string functions
join()
lower()
upper()
count()
index()
isalpha()
isdigit()
isspace()
isalnum()
split()
'''

# i/p: s="I live in Pune 411045"
# o/ps: s_a="IliveinPune" , s_n="411045"
# using loop and string functions

s="I live in Pune 411045"
s_a=""
s_n=""
for x in s:
    if x.isalpha():
        s_a+=x
    elif x.isdigit():
        s_n+=x

print(s_a,s_n)