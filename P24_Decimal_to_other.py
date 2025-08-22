# Program 24
# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.

n=int(input("Enter the number in Decimal:"))

print("Enter choice to convert into:")
print("1.Binary\n2.Octal\n3.Hexadecimal")

print("Type here:",end="")
choice=int(input())

def conversion(base,n):
    l=[]
    while(n!=0):
        if(n%base<=9):
            l.append(n%base)
        else:
            d={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
            l.append(d[n%base])

        n=int(n/base)
    
    l="".join(str(num) for num in l)
    return (l[::-1])

198
if(choice==1):
    print(f"Binary Number:{conversion(2,n)}")
elif(choice==2):
    print(f"Octal Number:{conversion(8,n)}")
elif(choice==3):
    print(f"Hexadecimal Number:{conversion(16,n)}")
else:
    print("Wrong Number ENTERED.Try Again!!")

# # However,there are the functions for doing these kind of conversions
# print(bin(198))  # 0b11000110
# print(oct(198))  # 0o306
# print(hex(198))  # 0xc6


# Output:
# Enter the number in Decimal:198
# Enter choice to convert into:
# 1.Binary
# 2.Octal
# 3.Hexadecimal
# Type here:1
# Binary Number:11000110

# Enter the number in Decimal:198
# Enter choice to convert into:
# 1.Binary
# 2.Octal
# 3.Hexadecimal
# Type here:2
# Octal Number:306


# Enter the number in Decimal:198
# Enter choice to convert into:
# 1.Binary
# 2.Octal
# 3.Hexadecimal
# Type here:3
# Hexadecimal Number:C6


# Rough:

#   2 9 1
#   2 4 0
#   2 2 0
#     1 
# 1001

#   2 8 0
#   2 4 0
#   2 2 0
#     1 
# 1000