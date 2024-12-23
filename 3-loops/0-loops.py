'''
Loop:
loop is a sequence of instruction
that is countinuosly repeated until
a certain  condition is reached

Types: 
   # while
   # for(iterative for , for with range()) for two types   
'''
'''
# initialization , condition , increment/decrement

i=0 #initialization ; i is iterator
while i<10:   #condition
    print(i)
    i+=1      # increment/decrement
'''

# print no. 10-20 using while loop

# i=10
# while i<=20:
#     print(i)
#     i+=1

# # reverse loop

# i = 9
# while i>=0:
#     print(i)
#     i-=1

#reverse 20-10

# i=20
# while i>=10:
#     print(i)
#     i-=1

# # even no. between 0-9 using while loop and conditionals

# i=0
# while i<10:
#     if i%2 == 0:
#         print(i)
#     i+=1

# # odd no. between 20-50 using while loop and conditionals

# i=20
# while i<=50:
#     if i%2 != 0:
#         print(i)
#     i+=1    


# # iterate a list using while loop

# l=[1,2,3,4,5,6,7]
# i=0
# while i<len(l):
#     print(l[i])
#     i+=1

# # REverse the list

# l=[45,9,2,0,11,41,'a','w',3]
# i=len(l)-1         # last index which len of list -1
# while i>=0:        # till first index which is 0
#     print(l[i])    # value of that index
#     i-=1           # decrement from last to first index

#create a list of even which will even no

# l=[20,21,23,24,26,25,27,29,30]
# even=[]
# i=0
# while i<len(l):
#     if l[i] % 2==0:
#         even.append(l[i])
#     i+=1
# print(even)

# #create a list of even which will even no for odd

# l=[20,21,23,24,26,25,27,29,30]
# even=[]
# odd=[]
# i=0
# while i<len(l):
#     if l[i] % 2==0:
#         even.append(l[i])
#     else:
#         odd.append(l[i])    
#     i+=1
# print(even)
# print(odd)

#program
l=[20,21,23,24,26,25,27,29,30]
even_indexed=[]
odd_indexed=[]
i=0
while i<len(l):
    if i % 2==0:
        even_indexed.append(l[i])
    else:
        odd_indexed.append(l[i])
    i+=1
print(even_indexed, odd_indexed) 
