# Program 18
# Write a Program to print the fibonacci sequence.

n=int(input("Enter the number of terms of the fibonacci sequence:"))
if(n<=0):
    print("No. of terms is less than equal to zero.No output!!")
else:
    i=0 # First term
    j=1 # Second term
    res=0 # Result
    print("Fibonacci Sequence:")
    for k in range(n):
        print(res,end=" ")
        i=j
        j=res
        res=i+j


