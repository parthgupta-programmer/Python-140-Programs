# Program 16
# Write a Python Program to print the factorial of a given number.


n=int(input("Enter any number:"))
f=1

if(n<0):
    print("Factorial does not exist for negative numbers.")
else:
    for i in range(1,n+1):
        f=f*i
    print("Factorial:",f)

