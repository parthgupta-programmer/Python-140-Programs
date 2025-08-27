# Program 35
# Write a Python program to check if number entered is a disarium number.


# A Disarium number is a number that is equal to the sum of its digits each raised to the power of its respective position. 
# For example, 89 is a Disarium number because
# 8^1 + 9^2 = 8 + 81 = 89

# Approach 1


n=int(input("Enter any number:"))
temp=n
temp2=n

coun=0
while(n!=0):
    n=int(n/10)
    coun+=1
sum=0
i=coun

while(temp2!=0):
    sum=sum+(temp2%10)**i
    temp2=int(temp2/10)
    i-=1

if(sum==temp):
    print("Entered number is a disarium number.")
else:
    print("Entered number is not a disarium number.")


# Another way of doing this:

# Approach 2:

# n=(input("Enter any number:"))
# temp=n
# digits=[int(d) for d in (n)]
# s=sum([d**(i+1) for i,d in enumerate(digits)])
# if(s==int(temp)):
#     print("Entered number is a disarium number.")
# else:
#     print("Entered number is not a disarium number.")



# Output:

# Approach 1:

# Enter any number:89
# Entered number is a disarium number.

# Approach 2:
# Enter any number:89
# Entered number is a disarium number.
