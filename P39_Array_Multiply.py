# Program 39
# Write a Python program to Multiply all numbers in the list.

l=list(map(int,input("Enter list elements:").split()))
m=1
for i in l:
    m=m*i
print("Mulitplication of the elements of the list:",m)

