# Program 43
# Write a Python program to print odd numbers in a list.

l=list(map(int,input("Enter list elements:").split()))
odd=[i for i in l if i%2!=0]
print("Odd Elements list:",odd)

# Output:

# Enter list elements:1 2 3 4 5 6 7 8 9 10
# Odd Elements list:[2, 4, 6, 8, 10]