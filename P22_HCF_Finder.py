# Program 22
# Write a Python Program to print the HCF of two numbers

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))

print("HCF:",end="")
# Common Method
hcf=1
for i in range(1,min(a,b)+1):
    if((a%i==0) and (b%i==0)):
        hcf=i
print(hcf)

# Euclidean Algorithm(This is Fastest)
# gcd(a,b)=gcd(b,a mod b)
# It keeps reducing the numbers quickly using modulus.
# Example: gcd(48, 18)
# 48 % 18 = 12   → gcd(18, 12)
# 18 % 12 = 6    → gcd(12, 6)
# 12 % 6 = 0     → gcd(6, 0)
# Answer = 6

def hcf(a,b):
    while(b!=0):
        a,b=b,a%b
    return a

print(hcf(a,b))

# Output
# Enter First Number:48
# Enter Second Number:18
# HCF:6
# 6