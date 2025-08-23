# Program 32
# Write a Python Program to find sum of array.

try:
    print("Enter list elements:",end="")
    s=0
    l=list(map(float,input().split()))
    for i in l:
        s=s+i
    print("Sum of elements of the list : ",s)
except ValueError:
    print("Please enter valid elements!!")
else:
    print("Program Successfully Runs!! Thank U")

# However , there is a in built function that returns the sum of all the elements of the list.
# print(sum(l))  # 15.0

# Output:
# Enter list elements:1 2 3 4 5
# Sum of elements of the list :  15.0
# Program Successfully Runs!! Thank U