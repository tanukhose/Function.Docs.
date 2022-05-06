 # Q7.Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"


def a(weight,height):
    bmi=weight / height
    if bmi<=18.5:
        return "Underweight"

    if bmi<=25.0:
        return "Normal"

    if bmi<=30.0:
        return "Overweight"
        
    if bmi>30:
        return "Obese"
        
weight=int(input("enter the number "))
height=int(input("enter the number "))
print(a(weight,height))


