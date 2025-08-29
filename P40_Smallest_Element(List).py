# Program 40
# Write a Python program to find smallest number in a list.

l=list(map(float,input("Enter list elements:").split()))
small=l[0]
for i in l:
    if(i<small):
        small=i
print("Smallest number:",small)



# Output:
# Enter list elements:1 2 3
# Smallest number: 1.0

# However,we could also use min function instead of doing the above code.

# print(min(l)) # 1.0