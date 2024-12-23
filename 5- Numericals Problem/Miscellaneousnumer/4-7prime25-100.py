#write a program to print a list of 7 prime no. between 10 to 50

prime=[ ]
n=2

while len(prime) < 7:
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    if flag:
        prime.append(n)  # Add the prime number to the list
    n += 1

print("First 7 prime numbers:", prime)

'''
output-

First 7 prime numbers: [2, 3, 5, 7, 11, 13, 17]
'''