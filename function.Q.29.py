# Q30. Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
def prime(n):
    i=1
    while i<=n:
        count=0
        a=1
        
        while a<=i:
            if i%a==0:
                count+=1
            a+=1
        if count==2:
            print(i)
        i+=1
n=int(input("enter the  :"))
prime(n)
