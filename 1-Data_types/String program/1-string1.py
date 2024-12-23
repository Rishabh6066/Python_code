#find the even indexed and odd indexed elements:

s="My name is Garett Jacob Hobbs"
even_indexed_s=" "
odd_indexed_s=" "

for i in range(len(s)):
    if i%2==0:
        even_indexed_s += s[i]
    else:
        odd_indexed_s += s[i]

print(f"Even indexed of s: {even_indexed_s} \n Odd indexed of s: {odd_indexed_s}")

'''
output-

Even indexed of s:  M aei aetJcbHbs
 Odd indexed of s:  ynm sGrt ao ob

'''
    