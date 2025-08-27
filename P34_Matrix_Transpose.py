# Program 34
# Write a Python program to return the transpose of the matrix.


print("Matrix :")

r=int(input("Rows:"))
c=int(input("Columns:"))
 
 
print("Enter the elements of the matrix:")
matrix=[]
for i in range(r):
    l=list(map(int,input().split()))
    matrix.append(l)
print("Transpose of the matrix:")
t=[[0 for j in range(r)] for i in range(c)]
for i in range(c):
    for j in range(r):
        t[i][j]=matrix[j][i]
        print(t[i][j],end=" ")
    print()

# Output:

# Matrix :
# Rows:2
# Columns:3
# Enter the elements of the matrix:
# 1 2 3
# 4 5 6
# Transpose of the matrix:
# 1 4
# 2 5
# 3 6