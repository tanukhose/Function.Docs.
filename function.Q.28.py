# Q29. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
def sum(n):

    i=1
    while i<=n:
        if i%3==0 or i%5==0:
            print(i)
        
        i+=1
n=int(input("enter the  :"))
sum(n)




