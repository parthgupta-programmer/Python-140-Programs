# Program 36
# Write a Python program to check if the number entered is a harshad number or not.

# A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
# In other words, a number is considered a Harshad number if it can be evenly divided by thesum of its own digits.
# For example = 18 is a harshad number
# 1+8=9  18%9==0

# Approach 1
try:
    
    n=int(input("Enter any number:"))
    temp=n
    s=0
    while(n!=0):
        s=s+n%10
        n=int(n/10)
    if(temp%s==0):
        print(f"{temp} is a harshad number.")
    else:
        print(f"{temp} is not a harshad number.")
except ValueError:
    print("Enter valid value!!")

# Output:

# Enter any number:18
# 18 is a harshad number.

# Enter any number:19
# 19 is not a harshad number.

# Enter any number:50
# 50 is a harshad number.

# Approach 2

def check_harshad_no(n):
    s=sum([int(i) for i in n])
    if(int(n)%s==0):
        print("Harshad number")
    else:
        print("Not a Harshad number")
check_harshad_no(str(18))

# Output:

# Enter any number:18
# 18 is a harshad number.
# Harshad number