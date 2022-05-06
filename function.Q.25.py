# Q26. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.


def div(a):
    if a%3==0:
        print("3 divisible")
    if a%5==0:
        print("5 divisible")
    elif a%3==0 and a%5==0:
        print("both of divisible ")
    else:
        print("not divisible")
a=int(input("enter the number "))
div(a)
