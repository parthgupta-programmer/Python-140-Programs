# Program 23
# Write a Python Program to find the LCM of two numbers.

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))

def gcd(a,b): # GCD=HCF
    while(b!=0):
        a,b=b,a%b
    return a
print(f"LCM:{int(a*b/gcd(a,b))}") # LCM*HCF=a*b