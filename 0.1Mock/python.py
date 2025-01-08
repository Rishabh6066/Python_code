'''
Write a Python function common_elements_in_tuples(tuples_list) that takes a list of tuples as input. Each tuple contains two sets of integers. 
The function should return a new list of tuples, where each tuple contains:

The original tuple from the input.
A set of integers that are common between the two sets in that tuple.
If there are no common elements between the two sets in a tuple, exclude that tuple from the result.
Constraints:
Each tuple in the input list will contain exactly two sets.
Sets can have 0 or more integers.
The result should only include tuples where the intersection of the two sets is not empty. give me its answer
'''

def common_elements_in_tuples(tuples_list):
    result = []
    
    for tup in tuples_list:
        set1, set2 = tup
        common_elements = set1 & set2  # Find the intersection of the two sets
        
        if common_elements:  # Only include tuples with non-empty intersection
            result.append((tup, common_elements))
    
    return result

# Example usage:
tuples_list = [
    ({1, 2, 3}, {3, 4, 5}),
    ({6, 7, 8}, {9, 10, 11}),
    ({12, 13}, {13, 14}),
    ({0, 1}, {2, 3}),
]

result = common_elements_in_tuples(tuples_list)
for original_tuple, common_set in result:
    print(f"Original tuple: {original_tuple}, Common elements: {common_set}")



