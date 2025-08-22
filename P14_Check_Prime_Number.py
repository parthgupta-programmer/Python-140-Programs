# Program 14
# Write a Python Program to Check Prime Number.

n=int(input("Enter any number:"))
if(n==1):
    print("Not a Prime Number")
else:
    for i in range(2,n):
        if(n%i==0):
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")