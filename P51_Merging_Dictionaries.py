# Program 51
# Write a Python program to Merging two Dictionaries.

d1={"a":10,"b":20,"c":10,"d":30,"e":20}
d2={"f":10,"g":20,"h":10,"i":30,"j":20}

d1.update(d2)
print(d1)

# Output:
# {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20, 'f': 10, 'g': 20, 'h': 10, 'i': 30, 'j': 20}