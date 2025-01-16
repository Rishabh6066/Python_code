'''

eval():
    The eval() function in python in python takes a string expression
    and evalutes it as a Python expression.
    It can execute a dynamically generated python code.
    The results of the expression is returned.

Syntax:
eval(expression)    

'''

s="7+3"
print(eval(s))

s="7-3"
print(eval(s))

s="7*3"
print(eval(s))

s="7%3"
print(eval(s))

s="7/3"
print(eval(s))

s="7//3"
print(eval(s))

s="7+3-5*4+76"
print(eval(s))

s="7+3-(4+6-5)+2"
print(eval(s))

s="7+3*65"
print(eval(s))

s="7+3-8"
print(eval(s))

x=3
y=5
a="x+y"
print(eval(a))