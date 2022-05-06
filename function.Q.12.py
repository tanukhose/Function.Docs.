# Q13.Write a function to check if a number is even or not.


def even(a):
    if a%2==0:
        print("even number ")
    else:
        print("not")
a=int(input("enter the number "))
even(a)