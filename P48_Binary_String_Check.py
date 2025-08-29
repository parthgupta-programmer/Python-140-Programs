# Program 48
# Write a Python program to check if a given string is binary string or not.

s=input("Enter a string:")
for i,ch in enumerate(s):
    if(s[i]!='1' and s[i]!='0'):
        print("Not a Binary String")
        break
else:
    print("String you have entered is a Binary String.")

# Output:

# Enter a string:1011010101
# String you have entered is a Binary String.

# Enter a string:100441104
# Not a Binary String