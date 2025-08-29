# Program 41
# Write a Python program to find largest number in a list.

def largest_number(l):  # Less efficient Time Complexity:O(n^2)
    for i in range(len(l)):
        flag=True
        for j in range(i,len(l)):
                if(l[i]<l[j]):
                    flag=False
        if(flag==True):
            return l[i]
l=list(map(float,input("Enter list elements:").split()))
print(largest_number(l)) 

lar=l[0]
for i in l:  # More efficient Time Complexity:O(n)
    if(i>lar):
        lar=i
print("Largest number:",lar)



# Output:
# Enter list elements:1 2 3
# Largest number: 3.0

# However,we could also use max function instead of doing the above code.

# print(max(l)) # 3.0
