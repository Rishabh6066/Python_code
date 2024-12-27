'''
Recursion:
   Recursion is a programming concept
   where a function calls itself
   to solve a smaller instance of 
   the same problem until it reaches a base case,
   which is a condition that stops the recursion.
'''

def summation(n):
    if n==0:
        return 0
    else:
        return n + summation(n-1)
'''
           5 + summation(4)
           5 + 4 summation(3)
           5 + 4 + 3 summation(2)
           5 + 4 + 3 + 2 summation(1)
           5 + 4 + 3 +2 + 1 + 0
           15
         '''
print(summation(5)) # 5 + 4 + 3 + 2 + 1 = 15

#factorial of using recursion

def recursion(n):
      if n==0 or n==1:
           return 1
      else:
           return n * recursion(n-1)
      
      
print(recursion(7)) 

# first 10 elements of fibonacci series using function

def fibo(n):
     if n==0:
          return 0
     elif n==1:
          return 1
     else:
          return fibo(n-1) + fibo(n-2)

'''
How this work-

# 0 = 0
# 1 = 1
# 2 : fibo(1) + fibo(0)
      = 1 + 0
      = 1
#3 :  fibo(2) + fibo(1)
      fibo(1) + fibo(0) + fibo(1)
      = 1 + 0 + 1
      = 2
#4 :  fibo(3) + fibo(2)  # breaking it
      fibo(2) + fibo(1) + fibo(1) + fibo(0)
      fibo(1) + fibo(0) + fibo(1) + fibo(1) + fibo(0)
      = 1 + 0 + 1 + 1 + 0
      =3
#5 :  fibo(4) + fibo(3)
      fibo(3) + fibo(2) + fibo(2) + fibo(1)
      fibo(2) + fibo(1)  +  fibo(1) + fibo(0) + fibo(1) + fibo(0) + fibo(1)
      fibo(1) + fibo(0) + fibo(1)  +  fibo(1) + fibo(0) + fibo(1) + fibo(0) + fibo(1)
      = 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1
      = 5
              
'''     
     
     
for x in range(10):
     print(fibo(10)) 

'''

'''
     
    