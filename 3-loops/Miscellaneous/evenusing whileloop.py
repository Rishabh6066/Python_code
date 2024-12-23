#Write a Python program that takees a list of numbers and returns a new list containing only the 
# even number from the original list. uimg while loop

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num=[]

i=0
while num[i]<len(num):
    if i%2==0:
        even_num.append(num[i])
    i+=1

print(even_num)