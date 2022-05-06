# Q44.Bonus - Given the same list, print the last ‘N’ elements in reverse order.
# Sample Input:
# 2
# Sample Output:
# q
# b 
# Sample Input:
# 3
# Sample Output:
# q
# b 
# 5


# a=[1,2,3,4,5]
# i=1
# b=[]
# while i<len(a)+1:
#     b.append(a[-i])
#     i+=1
# print(b)

def rev(a):

    b=[]
    i=1
    while i<=a:
        f=int(input("enter the number "))
        b.append(f)
        i+=1
    print(b)
    i=1
    c=[]
    while i<len(b)+1:
        c.append(b[-i])
        i+=1
    print(c)
a=int(input("enter the"))
rev(a)