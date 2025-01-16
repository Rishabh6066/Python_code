# import os

# os.remove("abcd.json")

#remove() will give error if file doesnt exists

#replace() to manipulate a particular content in line

#Question
'''
Create a new file xyz.txt
write 5-7 line of content
read a complete file
insert "I am in pune" in line no. 3
read 4 line of file
remove 3 line from a file
delete a file

'''

f=open('xyz.txt','w')
f.write("""
        Hii i am Rishabh
        I am from Mirzapur
        I am a Data analyst student in codenera
        gfh
        fhjdfj
    """)
f=open('xyz.txt','r')
print(f.read())