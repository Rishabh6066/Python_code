'''
Scope:
    Variable is only available from inside
    the region it is created, is called as
    scope.

Local Scope:
      A variable is created inside a function belongs
      to local scope of that function, and can only
      be used inside that function.

Global Scope:
     A variable created in the main body
     python code is a global variable and belongs to
     the global scope

GLOBAL variable are available from within
any scope global and local     
'''

a=4                    # global var
print(a)

def add():               
    b=3                 # local var
    print(a)
    print(b)

add()

'''
print(b)
# NameError: name 'b' is not defined
# b is not accessable outside func add
# because it is in local scope of add()
'''
def add():
    b=3
    print(b)
    #print(a)
    def inner():
        a=6
        print(b)
        print(a)
    inner()

add()

'''
if you want to create a global variable but
are stuct in local scope you can use the global keyword
'''

#1)
def func():
    global a 
    a=200

func()
print(a)

# 2)
def add():
    b=3
    def inner():
        global a
        a=6
    inner()
    print("Inside a add()",a) 

add()
print("Globally",a)
