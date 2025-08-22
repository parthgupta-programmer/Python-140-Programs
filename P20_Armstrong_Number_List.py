# Program 20
# Write a Python Program to Find Armstrong Number in an Interval

import math

def check_armstrong_number(n):
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
        return 1
    else:
        return 0


l=int(input("Enter lower limit of the interval for armstrong number:"))
u=int(input("Enter upper limit of the interval for armstrong number:"))

print(f"Armstrong Number list between ({l}-{u}):")
for i in range(l,u+1):
    if(check_armstrong_number(i)==1):
        print(i,end=" ")


# Output:
# Enter lower limit of the interval for armstrong number:10
# Enter upper limit of the interval for armstrong number:1000
# Armstrong Number list between (10-1000):
# 153 370 371 407
