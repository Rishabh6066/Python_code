# WAP to find all the possible sub-string of a string "abc" using loops.

s="abc"
sub=[]

for i in range(len(s)):
    word=""                    # a,b,c,d
    for j in range(i,len(s)):  # for a: a, ab , abc #for b: b,bc, bcd for c: c, cd for d: d 
        word+=s[j]
        sub.append(word)
print(sub)        


for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j],end=" ")