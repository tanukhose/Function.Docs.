# Q33. Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi > 30 return "Obese"
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"


def a(weight,height):
    bmi=weight/height
    if bmi > 30:
        print("Obese")
    if bmi <= 18.5:
        print("Underweight")
    if bmi <= 25.0:
        print("Normal")
    if bmi <= 30.0:
        print("Overweight")
weight=int(input("enter the number "))
height=int(input("enter the number "))
a(weight,height)
