# Program 42
# Write a Python program to print even numbers in a list.

l=list(map(int,input("Enter list elements:").split()))
even=[i for i in l if i%2!=0]
print("Even Elements list:",even)

# Output:

# Enter list elements:1 2 3 4 5 6 7 8 9 10
# Even Elements list: [1, 3, 5, 7, 9]