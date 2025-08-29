# Program 47
# Write a Python program to split and join a string.

s="Hello I am Parth Gupta , I love Python!!"

splitted_string_list=s.split() # By default : takes argument as space(" ") as a seperator
joined_string=" ".join(splitted_string_list) #(join string lists using (" " as a seperator))

print(splitted_string_list)
print(joined_string)