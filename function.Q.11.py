# Q12.Numbers ending with zeros are boring.

# They might be fun in your world, but not here.

# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

 
a=input("enter the number ")
i=0
while i<len(a):
    if a[i]!=0:
        print(a[i])
    i+=1
