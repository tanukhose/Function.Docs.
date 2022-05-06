# Q27. Write a function for checking the speed of drivers. This function should have one parameter:
#  speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point
#  and print the total number of demerit points. For example, if the speed is 80, it should print:
# “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”
# def speed(a):
def speed(a):

    b=(a-70)//5
    if a<70:
        print("Ok")
    elif a>70 and b>=12:
        print("License suspended")
    elif a>70 and a%5==0:
        # b=(a-70)//5
        print("points",b)
    else:
        print("worng input")
a=int(input("Enter the speed :"))
speed(a)

        