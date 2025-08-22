# Program 4
# Write a Program to swap two variables.

a=int(input("Enter First Number (a):"))
b=int(input("Enter Second Number (b):"))

a1=a
b1=b

# Using a third variable:
c=a
a=b
b=c

print("After Swapping(With using a third variable)\na=",a)
print("b=",b)


# Without using a third variable:
a1=a1 + b1
b1=a1 - b1
a1=a1 - b1
print("After Swapping(Without using a third variable)\na=",a1)
print("b=",b1)
