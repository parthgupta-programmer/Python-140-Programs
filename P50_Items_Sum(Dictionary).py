# Program 50
# Write a Python program to find the sum of all items in a dictionary.

# Approach 1
d1={"a":10,"b":20,"c":10,"d":30,"e":20}
print("Sum:",sum(d1.values()))

# Approach 2
s=0
for i in d1.values():
    s+=i
print("Sum:",s)

# Output:

# Sum: 90
# Sum: 90