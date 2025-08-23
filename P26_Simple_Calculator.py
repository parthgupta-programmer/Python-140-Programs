# Program 26
# Write a Python Program to Make a Simple Calculator with 4 basic mathematicaloperations.


print("SIMPLE CALCULATOR\n")
print("Enter the operation u want to perform:-")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
print("Enter here:",end='')

choice=int(input())

if(choice==1):
    print("Enter two numbers to add:",end="")
    a,b=list(map(float,input().split()))
    print(f"{a} + {b} = {a+b}")
elif(choice==2):
    a=float(input(("Enter number to subtract:")))
    b=float(input(("Enter number to subtract from:")))
    print(f"{b} - {a} = {b-a:.2f}")
elif(choice==3):
    print("Enter two numbers to multiply:",end="")
    a,b=list(map(float,input().split()))
    print(f"{a} x {b} = {a*b}")
elif(choice==4):
    a=float(input(("Enter Dividend:")))
    b=float(input(("Enter Divisor:")))
    if(b==0):
        print("Math Error!!")
    else:
            print(f"{a} / {b} = {a/b}")

else:
    print("Wrong Choice entered...Try Again!!")

    