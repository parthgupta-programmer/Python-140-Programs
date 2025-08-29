# Program 45
# Write a Python program to Cloning or Copying a list.

l=list(map(int,input("Enter list elements:").split())) # 1,2,3,4,5

# Using slice operator
cloned1=l[:]

# Using list comprehension
cloned2=[i for i in l]

# Using list constructor
cloned3=list(l)

print(cloned1) # [1, 2, 3, 4, 5]
print(cloned2) # [1, 2, 3, 4, 5]
print(cloned3) # [1, 2, 3, 4, 5]