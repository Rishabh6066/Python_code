#Write the program to print a list of prime no. between 25 to 100

prime=[]

for i in range(25,101):
    flag= True
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
    
    if flag:
        prime.append(i)
print(f"List of prime numbers between 25 and 100: {prime}")

'''
output-
List of prime numbers between 25 and 100: [29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
'''