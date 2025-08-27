# Program 36
# Write a Python program to check if the number entered is a happy number or not.

# Happy Number:
# A Happy Number is a positive integer that, when you repeatedly replace the number by the sum of the squares of its digits and continue the process, eventually reaches 1. 
# If the process never reaches 1 but instead loops endlessly in a cycle, the number is not a Happy Number.

try:
    n=int(input("Enter any number:"))

except ValueError:
    print("Enter valid value!!")
