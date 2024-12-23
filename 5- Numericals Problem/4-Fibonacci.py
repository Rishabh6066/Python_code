'''
Fibonaci series:

0 1 1 2 3 5 8 13 21 34 55 89
'''
# fibonaci_no=int(input("Enter the no.:"))
# fibonaci_list=[]
# a=0
# b=1
# print(a)
# print(b)
# n=1
# while (n<=fibonaci_no):
#     c= a + b    # 0+1=1   # 1+1=2  # 1+2=3
#     print(c)    # 1       # 2      # 3
#     a=b         # a=1     # a=1    # a=2
#     b=c         # b=1     # b=2    # b=3   like this it will go to the no given by user
#     n+=1


#.........................................................

# list of first 10 fibonacci series
fibonaci_no=int(input("Enter the no.:"))
a=0
b=1
fibonaci_list=[a,b]
n=1
while (n<=fibonaci_no):
    c= a + b   
    #print(c)    
    a=b         
    b=c         
    fibonaci_list.append(c)
    n+=1

print(f'fibonacci list : {fibonaci_list}')