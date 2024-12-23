'''
1-Reverse a string using a loop.

2-Count the occurrences of a specific character in a string using a loop.

3-Remove leading and trailing whitespaces from a string without using strip().

4-Replace all occurrences of a character in a string with another character using a loop.

5-Split a sentence into words using a loop.

6-Format a string with values (e.g., name and city) without using the format() method.

7-Print the string with escape characters (e.g., \n, \t, \r) visible, without actually executing them.

8-Convert all characters of a string to uppercase using a loop.

9-Convert all characters of a string to lowercase using a loop.

10-Count how many words are in a string without using split().

11-Remove extra spaces between words in a string.

12-Replace all occurrences of a substring in a string without using replace().

'''
#Reverse a string using a loop.
s='hello'
for i in range(len(s)-1,-1,-1):
    print(s[i],end=" ")
'''
Output-
o l l e h 

'''    
#2nd the occurrences of a specific character in a string using a loop.

#3 Remove leading and trailing whitespaces from a string without using strip()
print()
s="       hello world !!!     "
print(s.strip())



