# Program 15
# Write a Python Program to print all Prime Numbers between 1-10

def check_prime_number(n):
    if(n==1):
        return 0
    else:
        for i in range(2,n):
            if(n%i==0):
                return 0
        else:
            return 1

print("List of Prime Numbers between 1-10 : ",end="")
for i in range(1,11):
    if(check_prime_number(i)==1):
        print(i ,end=" ")
    
