# Program 3
# Write a Python Program to find the area of a triangle.

import math

print("Enter the sides of the triangle:",end="")
a,b,c=list(map(float,input().split()))
# Applying Heron's Formula
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Area of the Triangle:",area)

