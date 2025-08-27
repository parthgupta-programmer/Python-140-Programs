# Program 36
# Write a Python program to print the list of disarium number between 1 and 100.


def dis(n):
    digits=[int(d) for d in str(n)]
    s=sum([d**(i) for i,d in enumerate(digits,start=1)])
    if(s==int(n)):
        return 1
    else:
        return 0
l=[]
print("List of disarium number between 1 and 100:")
for i in range(1,101):
    if(dis(i)==1):
        l.append(i)
        print(i,end=" | ")
print(l)

# Output:
# 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 89 | [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]