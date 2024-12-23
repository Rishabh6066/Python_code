'''
Function:
          block of code
          which only run when it is called

you can pass data to a function as parameters
a function can return data
Types:          
1- in bult function : Eg: print(), len(), etc..
2- user defined function
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

#1- Without parameter/arguments with return
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
