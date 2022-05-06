# Q42. Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

 
def sum(a):
    i=0
    b=[]
    while i<len(a):
        a[i]=str(a[i])
        j=0
        sum=0
        while j<len(a[i]):
            sum+=int(a[i][j])
            j+=1
        b.append(sum)
        i+=1
    print(b)
a=[12, 67, 98, 34]
sum(a)