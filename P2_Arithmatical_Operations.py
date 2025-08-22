# Program 2
# Write a Python Program to do Arithmatical Operations Addition and Division

print("Select what to do :")
print("1.Addition\n2.Division")
print("Enter here:",end="")
c=int(input())
if(c==1):
    a=int(input("Enter the first number for addition:"))
    b=int(input("Enter the second number for addition:"))
    print("The Result of Addition of two numbers is : ",a+b)
elif(c==2):
    a=int(input("Enter the dividend for division:"))
    b=int(input("Enter the divisor for divisions:"))
    if(b==0):
        print("Zero cannot be divisor.Math Error!!")
    else:
        print("The Result of Division of [Dividend/Divisor] is : ",a/b)
else:
    print("You have entered wrong choice.Run the program again.")
