# Q34. Write a function which converts the input string to uppercase.
# Write a function which converts the input string to uppercase.
# For example:-
# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.
def s(b):
    i=0
    max=0
    maxs=0
    while i<len(b):
        if b[i]>max:
            max=b[i]
        i+=1
    i=0
    while i<len(b):
        if b[i]>maxs and b[i]!=max:
            maxs=b[i]
        i+=1
    print(max,"+",maxs,"=",max+maxs)
# b=[10, 14, 2, 23, 19] 
b=[99, 2, 2, 23, 19]
s(b)