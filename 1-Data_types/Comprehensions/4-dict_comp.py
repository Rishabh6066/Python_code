'''
Dict Comprehension:
    dict comphresion offers a shorter syntax when you want to
    creates a new dict or new list based on based on the values on an exixting dict.
'''




d={x:x**2 for x in range(11)}
print(d)  

d={1:1,2:4,3:9,4:16,5:25}
d1={k:v for k,v in d.items() if k%2==0}
print(d1)
#{2:4,4:16}
#{1:1,3:9,5:25}
d2={k:v for k,v in d.items() if k%2!=0}
print(d2)
