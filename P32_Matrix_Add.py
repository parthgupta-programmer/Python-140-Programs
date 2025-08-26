# Program 37
# Write a Python Program to Add Two Matrix.

rows=int(input("Enter number of rows:"))
colmns=int(input("Enter number of columns:"))

print("Enter data row by row:")

matrix1=[]
matrix2=[]

print("Enter Matrix 1 Elements:")
for i in range(rows):
    l=list(map(int,input().split()))
    matrix1.append(l)

print("Enter Matrix 2 Elements:")
for i in range(rows):
    l=list(map(int,input().split()))
    matrix2.append(l)

r=[]
print("Result of Matrix 1 + Matrix 2:")
for i in range(rows):
    l=[]
    for j in range(colmns):
        l.append(matrix1[i][j]+matrix2[i][j])
        print(matrix1[i][j]+matrix2[i][j],end=" ")
    print()
    r.append(l)
print(r)
