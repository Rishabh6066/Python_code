# s= "Garett Jacob Hobbs "
# count b
# s= "Garett Jacob Hobbs "
# count=0
# index=[]

# for i,char in s:
#     if i=='b':
#         count+=1
#     if char=='b':
#         index.append(char)    
# print(f'{count}: times')
# print(f"Index={index}")  
# 


s = "Garett Jacob Hobbs "


count = 0
index = []


for i in range(len(s)):
    if s[i] == 'b':
        count += 1
        index.append(i)  # Append the index of 'b' to the list

# Print the results
print(f"b is occured in the string {s} : {count} times on indexs : {index}")

