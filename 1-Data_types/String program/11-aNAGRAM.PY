'''
ANAGRAM : A WORD OR PHASE THAT IS MADE BY ARRABGING THE 
letters of another word or phase in a different order
'''
# WAP to check the two string given by the user are anagrams or not.


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Remove spaces and convert to lowercase
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

# Check if lengths are different
if len(string1) != len(string2):
    print("The strings are not anagrams.")
else:
    # Sort and compare the strings
    if sorted(string1) == sorted(string2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
