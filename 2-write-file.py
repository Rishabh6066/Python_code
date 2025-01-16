# #Write in files

# f=open('abc.txt','a')          # "a" appends in file
# f.write("Hello World!!!!!")    # write the content in a file
# f.close()

# # Read in files

f=open('abc.txt','a')            # "a" appends in file
f.write('''
        I am Student of Data Science
        I am learning Python
        I am a fresher.
''') #Write a content in a file
f.close()

f=open("abc.txt",'r')        # 'r' read a file
print(f.read())              # read() read the file

#readline()
with open('abc.txt','r') as file:
    line=file.readline()
    print(line)

#readlines()
with open('abc.txt','r') as file:
    line=file.readlines()
    print(line)

print(line[2])  

# insert()

line.insert(1,'Hi i am Rishabh')
with open('abc.txt','w') as file:
    file.writelines(line)

f=open('abc.txt','r')
print(f.read()) 

'''
With def- 

In Python, the with statement is used to manage resources 
efficiently and safely, such as files, network connections,
or locks, by automatically handling setup and cleanup 
actions. This ensures that resources are properly 
released or closed, even if an error occurs during 
execution.

'''

with open("abc.txt",'r') as file:
    line=file.readlines()

print(line[0])

#delete a particular line from a file

line.pop(0)

with open('abc.txt','r') as file:
    file.writelines(line)
f=open('abc.txt','r')
print(f.read())