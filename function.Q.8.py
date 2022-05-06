# Q9.Write a Python program to generate and print a list of first and last 5 elements where 
#   the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).




def squre():
    i=0
    a=[]
    b=[]
    while i<=30:
        if i>=1 and i<=5:
            a.append(i*i)
        elif i>=26 and i<=30:
            b.append(i*i)
        i+=1
    print(a,",",b)
squre()