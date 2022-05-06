# Q43.  Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last ‘N’ elements of
# the given list. ‘N’ is accepted from the user.
# Sample Input:
# 1
# Sample Output:
# q 
# Sample Input:
# 3
# Sample Output:
# 5 #q
# b #b
# q#5

def re():
    b=int(input("enter the number "))
    a=['a', 1, '2', 5, 'b', 'q']
    i=1
    while i<=b:
        print(a[-i])
        i+=1
re()


def name(b):
    a=['a', 1, '2', 5, 'b', 'q']
    i=0
    while i<=(b)+1:
        print(a[-b])
        i+=1
        b-=1
b=int(input("enter the number "))
name(b)

