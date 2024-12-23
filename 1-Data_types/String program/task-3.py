'''using a loop write a program
i/p: 'I love Python'
o/p: 'python love I
'''


string = "I love Python"


words = string.split()


reversed_string = ""


for i in range(len(words) - 1, -1, -1):
    reversed_string += words[i] + " "

print(reversed_string)

#other method

s= 'I love python'

word=""
l=[]
for x in s:
    if x != " ": 
        word+=x  #I # l o v e
    else:
        l.append(word)
        word=""
l.append(word)
l1=l[::-1]

rev_word=" ".join(l1)
print(rev_word)

