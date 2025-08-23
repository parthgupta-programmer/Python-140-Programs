# Program 31
# Write a Python Program for cube sum of first n natural numbers?

n=int(input("Enter the number(N):"))
s=0
for i in range(1,n+1):
    s=s+(i**3)
print("Cube Sum of first N natural numbers:",s)