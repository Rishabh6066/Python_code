# # 1- Iterative for
# l=[1,2,3,4,5,6,7,8]

# for x in l: 
#     print(x)

# l=[2,6,0,'a',6,'x',4]

# for i in l:
#     print(i)

# l=[2,23,11,4,6,21,14,45,33,0]
# even=[]
# odd=[]

# #using iterative for

# for x in l:
#     if x %2==0:
#         even.append(x)
#     else:
#         odd.append(x)    
#     x+=1

# print(f"even: {even} odd: {odd}")

# even no. sum

# l=[1,2,3,4,5,6,7,8,9]
# even_sum=0
# odd_sum=0

# for i in l:
#     if i % 2==0:
#         even_sum +=i
#     else:
#         odd_sum +=i 
# print("sum of")
# print(f'Even sum = {even_sum} , Odd sum= {odd_sum}')


# 2nd type in for using range function
'''
for x in range(10): #(0:10:1) (i=0 i<10 i+=1) # default values
    print(x)

for x in range(1,10): #(1:10:1) (i=1 i<10 i+=1) 
    print(x)

for x in range(1,10,2): #(1:10:2) (i=1 i<=10 i+=2)
    print(x)

for x in range(10,0,-1): #(10:0:-1) (i=10 i>0 i-=1)
    print(x)

for x in range(10,-1,-1): #(10:-1:-1) (i=10 i>-1 i-=1)
    print(x)    
'''
# # 0 to 10 even no using range

# for i in range(0,11):
#     if i%2==0:
#         print(i,end=" ")
        
# #15-35 odd no. sing range
# print('\n')
# for i in range(15,36):
#     if i%2!=0:
#         print(i,end=" ")

# #13-50 even no. in reverse order
# print('\n')
# for i in range(50,12,-1):
#     if i%2==0:
#         print(i,end=" ")
# print("\n")

# # using range() print all the elements of the list
# l=[1,3,6,7,8]

# for i in range(len(l)): # i is the index
#     print(l[i])         # l[i] is the value of that index


# l=[1,2,3,4,5,6,7,8,9,10]
# #print all the elements from index 3 using range()

# for i in range(len(l)):
#     if i>=3:
#         print(l[i])
#  #or
# print('\n')
# for i in range(3,len(l)):
#     print(l[i])

# create list: even_index=[] odd_index , even[] ,odd[] l=[1,2,3,4,5,6,7,8,9,10]
l=[1,2,3,4,5,6,7,8,9,10]
even_index=[] 
odd_index=[] 
even=[] 
odd=[]
for x in range(len(l)):
    if x%2==0:
        even_index.append(l[x])
    else:
        odd_index.append(l[x])    
        
print(f"even_indexed:{even_index}, odd_index={odd_index}")

for x in range(len(l)):
    if l[x]%2==0:
        even.append(l[x])
    else:
        odd.append(l[x])    
        
print(f"even:{even}, odd={odd}")

'''
print the index: value of list [1,2,3,4,5,6,7,8,9,10]
#eg:
#0:1
# 1:2
# and so on using range

'''
# l= [1,2,3,4,5,6,7,8,9,10]
# for x in range(len(l)):
#     print(f"{x}:{l[x]}")

'''
*** imp form interview point of view
i/p: l=[1,2,3,4,1,2,3,4,1,2,3,4]
#o/p: [1,2,3,4]
#without using inbuit function
'''
l=[1,2,3,4,1,2,3,4,1,2,3,4]
new_list=[]
for i in l:
    if i not in new_list:
        new_list.append(i)

print(new_list)






