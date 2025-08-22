# Program 13
# Write a Python Program to check if entered year is a leap year or not.

year=int(input("Enter any year:"))
if(year%4==0 & year%100==0):
    print("Leap Year")
else:
    print("Common Year")