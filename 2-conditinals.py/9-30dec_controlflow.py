
'''
1- pass
     The pass statement is a placeholder
     that does nothing when executed.
     It is typically used as a syntactic placeholder
     where code will written later, or in situation
     where no action is required
'''
for x in range(5):
    if x%2==0:
        pass

'''
2. continue
       The continue statement skips the
       restr of the code in the current
       iteration and proceds to 
       the next iteration of the loop.
'''
for x in range(5):
    if x ==2:
        continue
    print(x)


'''
3- break
      The break statement exits the loop immediately,
      regardless of the loop's condition
'''

for x in range(5):
    if x==3:
        break
    print(x)


