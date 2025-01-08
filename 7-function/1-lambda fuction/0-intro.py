'''
Lambda function:
It is a small anonymous (unknown) function.
Can take any number of arguments and only one expression

Syntax:
lambda arguments: expression

The expression is executed and the result is returned
'''


# x= lambda a:a+3
# print(x(5))

# print((lambda a:a+3)(4))

# # reduce the value 7 by 2 using lambda

# print((lambda b:b-2)(7))

# # 2 argument
# print((lambda a,b:a+b)(2,3))

# # 3 argument
# print((lambda a,b,c:a+b+c)(2,3,6))

# filter even num from list 

# l=[1,2,3,4,5,6]
# even=[]
# def filter_even(l):
#     for x in l:
#         if x% 2==0:
#             even.append(x)
#     return even
        
# print(filter_even(l))


# l1=[1,2,3,4,5,6]
# even=[]
# for x in l1:
#     if((lambda x:x%2==0)(x)):
#        even.append(x)
# print(even)


# l = [1, 2, 3, 4, 5, 6]
# even = list(filter(lambda x: x % 2 == 0, l))  # Filter only even numbers
# print(even)



# Condition in lambda
a=4
if(lambda x:x%2==0)(a):
    print(f"{a} is even")

# Lambda in other function

def myfunc(n):
    return lambda a:a*n
y=myfunc(6)
print(y(3))


# Lambda in list comprehension
l=[1,2,3,4,5,6]
l1=[x for x in l if ((lambda a:a % 2==0)(x))]
print(l1)


l=[1,21,3,41,5,61]
l2=[(lambda a:str(a)+':even')(x) if x%2==0 else (lambda a:str(a)+':odd')(x) for x in l]
print(l2)
