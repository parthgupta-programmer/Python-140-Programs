print("Matrix 1:")

r1=int(input("Rows:"))
c1=int(input("Columns:"))

print("Matrix 2:")

r2=int(input("Rows:"))
c2=int(input("Columns:"))

if(c1==r2):
    matrix1=[]
    print("Enter matrix 1 elements:")
    for i in range(r1):
        l=list(map(int,input().split()))
        matrix1.append(l)
    matrix2=[]
    print()
    print("Enter matrix 2 elements:")
    for i in range(r2):
        l=list(map(int,input().split()))
        matrix2.append(l)
    r=[[0 for _ in range(c2)] for _ in range(r1)]
    print("Multiplication Result:")
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                r[i][j]=r[i][j]+matrix1[i][k]*matrix2[k][j]
            print(r[i][j],end=" ")
        print()
    print(f"Order:({r1},{c2})")
else:
    print("Matrix cannot be multiplied...")
# 1 2  1 2 3  1*1+2*4 1*2+2*5 1*3+2*6  09 12 15
# 3 4  4 5 6  3*1+4*4 3*2+4*5 3*3+4*6  19 26 33
# 5 6         5*1+6*4 5*2+6*5 5*3+6*6  29 40 51