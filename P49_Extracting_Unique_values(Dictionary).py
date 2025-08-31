# Program 49
# Write a Python Program to extract unique dictionary values.


print("Unique dictionary values:")
# Approach 1: 
d1={"a":10,"b":20,"c":10,"d":30,"e":20}
l=list((set(d1.values())))
print(l)

# Approach 2:

unique_values=[]
for i in l:
    if i not in unique_values:
        unique_values.append(i)
print(unique_values)

