'''
WAP to print a string of consonants from a given string.

i/p: "Garett Jacob Hobbs "
'''
# Input string
string = "Garett Jacob Hobbs "
sc=""
for i in string:
    if not(i!='a' and i!='A' and i!='e' and i!='E' and i!='i' and i!='I' and i!='o' and i!='O' and i!='u' and i!='U'):
        sc+=(i)
print(sc)        


s= "Garett Jacob Hobbs "
vowel="aeiouAEIOU"
sc=""
for x in s:
    if (x not in vowel):
        sc+=(x)
print(sc)        


