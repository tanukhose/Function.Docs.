# Q10.Create a function that takes 2 positive integers in form of a string as an 
# input, and outputs
#  the sum (also as a string):

# "4",  "5" --> "9"
# "34", "5" --> "39"
# Notes:

# If either input is an empty string, consider it as zero.


# a="34"
# i=0
# sum=0
# while i<len(a):

#     # print(i)
#     sum+=int(a[i])
#     i+=1
# print(sum)


def sum(a,b):
    sum=str(int(a)+int(b))
    print(type(sum))
a=input("enter the number ")
b=input("enter the number ")
sum(a,b)
    




