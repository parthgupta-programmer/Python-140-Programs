# Program 10
# Write a Python Program to swap two variables using OR operator.

print("Enter two numbers :")
a=int(input("a:"))
b=int(input("b:"))

# Using OR(^) Operator
a=a^b
b=a^b
a=a^b

print(f"After Swapping:\na:{a} b:{b}")