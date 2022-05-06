# Q45. Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the
# user and update each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1 
# Sample Input:
#     23
#     42 
#     41 
#     1
# Sample Output:
#     -23 
#     4200 
#     -41 
#     -1

# def mul():
i=0
while i<=4:
    a=int(input("enter the number "))
    i+=1
if a%2==0:
    print(a*100)
else:
    print(a*-1)
        # i+=1
# mul()
    