# Q14.Write a function to check if a number is prime or not.
   


# def prime(a):
#     i=1
#     count=0
#     while i<=a:
#         if a%i==0:
#             count+=1
#         i+=1
#     if count==2:
#         print("prime number ")
#     else:
#         print("not ")
# a=int(input("enter the number "))
# prime(a)





i=1
l=[]
while i<=100:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    if c==2:
        l.append(i)
    i+=1
print(l)
    