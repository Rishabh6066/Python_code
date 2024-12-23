# # first 10 even no.
# even_number=[2,4,6,8,10,12,14,16,18,20]

# # first 10 odd no.
# odd_number=[1,3,5,7,9,11,13,15,17,19]

# #Merging the list

# merging_list= even_number + odd_number

# print("Merged_list:",merging_list)

# # List of even numbers up to 7 
# even_numbers = [2, 4, 6] 
# #Repeating the list 4 times 
# repeated_list = even_numbers * 4 
# print("Repeated List:", repeated_list)

l = [1, 2, 3, 4, 5, 6, 1, 8, 8, 9] 

first_index = l.index(1)
print(first_index)
second_index = l.index(1, first_index + 1)
print(second_index)