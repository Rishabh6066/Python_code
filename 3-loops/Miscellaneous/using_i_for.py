'''
Given a list of integer, write a program that uses a loop to calculate and print the sum of all
the number that are divisible by 3. using iterative for
[1,2,3,4,5,6,7,8,9,10,21,22,23,24,25,26,27,28,29,30]
'''
num=[1,2,3,4,5,6,7,8,9,10,21,22,23,24,25,26,27,28,29,30]
sum=0
for x in num:
    if x%3==0:
        sum+=x
print(f"the value divisible by 3 sum is: {sum}")        