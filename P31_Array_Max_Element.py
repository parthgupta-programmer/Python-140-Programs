try:
    print("Enter list elements: ",end="")
    l=list(map(float,input().split()))
    mx=l[0]
    for i in l:
        if(mx<i):
            mx=i
    print("Maximum Element in list:",mx)
except ValueError:
    print("Please enter valid elements")

print(max(l))
# However , there is a in built function that returns the max of  the elements of the list.
# print(max(l))  # 5.0

# Output:
# Enter list elements: 1 2 3 4 5
# Sum of elements of the list: 5.0