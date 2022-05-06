# Q16.Print multiplication table of 12 using function.


def table(a):
    i=1
    while i<=10:
        print(a*i)
        i+=1
a=int(input("enyer the number "))
table(a)