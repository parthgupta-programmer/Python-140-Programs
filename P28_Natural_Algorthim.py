# Program 30
# Write a Python Program to calculate the natural logarithm of any number.

import math
num=int(input("Enter any number:"))
if(num<=0):
    print("Please enter any number...")
else:
    print(f"The natural logarithm of {num} is {math.log(num)}")

# Output:
# Enter any number:8
# The natural logarithm of 8 is 2.0794415416798357