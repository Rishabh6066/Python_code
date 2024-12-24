'''
Function:
          block of code
          which only run when it is called

you can pass data to a function as parameters
a function can return data
Types:          
1- in bult function : Eg: print(), len(), etc..
2- user defined function
    four type:-
    a) without parameter/ar
    b) with parameter/arguments
    c) without parameter with argument  
    d) with argument with parameter
3- lambada function

'''

'''
Syntax of function-

def name_of function(arguments):   # defnition of function
    func body
    return date

how to call it-

name_of_func(parameters)          # call a func

'''

def show():
    print("I am show")

show()

#create a function that print your name

# def name():
#     a=input('Enter your name: ')
#     print(name)

# name()
#User define fun types:

#1- Without parameter
def add():
    a=5
    b=9
    print(f"a: {a} + b: {b} = {a+b}")
add()

#sub() mul() div()    
def sub():
    a=5
    b=9
    print(f"a: {a} - b: {b} = {a-b}")
sub

def mul():
    a=5
    b=9
    print(f"a: {a} * b: {b} = {a*b}")
mul()

def div():
    a=5
    b=9
    print(f"a: {a} / b: {b} = {a/b}")
div()

#2- With parameter/arguments without return

def add(a,b):
    print(f"{a} + {b} = {a+b}")

add(2,4)

def sub(a,b):
    print(f"{a} - {b} = {a-b}")

sub(2,4)

def mul(a,b):
    print(f"{a} / {b} = {a*b}")

mul(2,4)

def div(a,b):
    print(f"{a} / {b} = {a/b}")

div(2,4)

#---------------------------------
# 3 Without argument with return
def add():
    a=2
    b=4
    return a + b
print(add())

def sub():
    a=2
    b=4
    return a - b
print(sub())

def mul():
    a=2
    b=4
    return a * b
print(mul())

def div():
    a=2
    b=4
    return a / b
print(div())

#---------------------------------
# 4 With argument / with return

def add(a,b):
    return (f"{a} + {b} = {a+b}")

print(add(2,4))

def sub(a,b):
    return (f"{a} - {b} = {a-b}")

print(sub(2,4))

def mul(a,b):
    return (f"{a} / {b} = {a*b}")

print(mul(2,4))

def div(a,b):
    return (f"{a} / {b} = {a/b}")

print(div(2,4))