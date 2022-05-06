# Q41. Write a Python program to find the list with maximum and minimum length.
# Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])


a=[[0], [9, 11], [13, 15, 17]]
i=0
max=len(a[0])
min=len(a[0])
while i<len(a):
    if len(a[i])>max:
        max=len(a[i])
        c=a[i]
    # elif len(a[i])<min:
    else:
        min=len(a[i])
        f=a[i]
    i+=1
print(max,c)
print(min,f)