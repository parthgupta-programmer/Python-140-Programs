# Program 46
# Write a Python program to Count occurrences of an element in a list.

l=list(map(int,input("Enter list elements : ").split()))
n=int(input("Enter the number to count its occurences in a list:"))
print("Number of occurence:",l.count(n))

# Output:

# Enter list elements : 1 2 2 3 4 2 5
# Enter the number to count its occurences in a list:2
# Number of occurence: 3