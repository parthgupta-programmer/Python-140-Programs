# Program 19
# Write a Python Program to Check Armstrong Number?

import math

n=int(input("Enter any number:"))
n1=n
n2=n

c=0

while(n!=0):
    n=int(n/10)
    c+=1


r=0

while(n1!=0):
    r=r+(n1%10)**c 
    n1=int(n1/10)

if(r==n2):
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")


# Output:
# Enter any number:153 
# Armstrong Number
