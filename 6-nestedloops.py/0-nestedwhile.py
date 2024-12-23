# nested ;oops: a loop within a loop

i=0
while i<=6:
    j=0
    while j<=5:
        print('*',end=" ")
        j+=1
    print()
    i+=1


'''
* * * * * *   i=0   j=0,1,2,3,4,5
* * * * * *   i=1   j=0,1,2,3,4,5
* * * * * *   i=2   j=0,1,2,3,4,5
* * * * * *   i=3   j=0,1,2,3,4,5
* * * * * *   i=4   j=0,1,2,3,4,5
* * * * * *   i=5   j=0,1,2,3,4,5
* * * * * *   i=6   j=0,1,2,3,4,5
'''
print('\n')

i=0
while i<=6:
    j=0
    while j<=5:
        print('*',"(",i,',',j,")",end=" ")
        j+=1
    print()
    i+=1

'''
i/j  |   0      1       2        3       4      5  
-----------------------------------------------------
0    | *(0,0)  *(0,1)  *(0,2)   *(0,3)  *(0,4) *(0,5)
1    | *(1,0)  *(1,1)  *(1,2)   *(1,3)  *(1,4) *(1,5)
2    | *(2,0)  *(2,1)  *(2,2)   *(2,3)  *(2,4) *(2,5)
3    | *(3,0)  *(3,1)  *(3,2)   *(3,3)  *(3,4) *(3,5)
4    | *(4,0)  *(4,1)  *(4,2)   *(4,3)  *(4,4) *(4,5)
5    | *(5,0)  *(5,1)  *(5,2)   *(5,3)  *(5,4) *(5,5)
6    | *(6,0)  *(6,1)  *(6,2)   *(6,3)  *(6,4) *(6,5)
'''    