# Program 70
# Write a Python program to convert key-values list to flat dictionary.

l=[["a",1],["b",2],["c",3],["d",4],["e",5]]
flat_dict={}
for key,val in l:
    flat_dict[key]=val
print(flat_dict)
