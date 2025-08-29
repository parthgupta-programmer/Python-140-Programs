# Program 44
# Write a Python program to Remove empty List from List.


original_list=[[1,2,3],[],[9,8,10]]
filtered_list=[i for i in original_list if i] # Empty list returns False as the boolean value 

print(filtered_list) # [[1, 2, 3], [9, 8, 10]]

# Modifying existing list

# for i in original_list:
#     if(bool(i)==False):
#         original_list.remove(i)
# print(original_list) # [[1, 2, 3], [9, 8, 10]]

