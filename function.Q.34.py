# Q35. Kids drink toddy.
#     Teens drink coke.
#     Young adults drink beer.
#     Adults drink whisky.
#     Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky".


def a(kid):
    if kid<14:
        return"drink toddy"
    if kid <18:
        return "drink coke"
    elif kid ==18:
        return "drink beer"
    elif kid <20:
        return "drink vadka"
    elif kid>20:
        return "drink whisky"
kid=int(input("enter the age"))
print(a(kid))