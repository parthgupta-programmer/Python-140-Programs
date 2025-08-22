# Program 9
# Write a Program to solve Quadratic Equation.

import math
print("Enter the Coefficents of the Quadratic Equation: ax² + bx + c = 0")

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

d=(b*b)-(4*a*c) # Discriminant
if(d==0):
    print("Real and Equal Roots.")
    r=(-b)/(2*a)
    r1=r
    r2=r
elif(d>0):
    print("Real and Distinct Roots.")
    r1=(-b+math.sqrt(d))/2*a
    r2=(-b-math.sqrt(d))/2*a
else:
    print("Imaginary(Complex) Roots.")
    real_part=-b/(2*a)
    imaginary_part=d/(2*a)
    r1=f"{real_part} + {imaginary_part}i"
    r2=f"{real_part} - {imaginary_part}i"
    
print("Root 1:",r1)
print("Root 2:",r2)