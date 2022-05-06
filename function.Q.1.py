def max():
    num=[23,4,3,67,5,7,5,76,]
    i=0
    max=0
    while i<len(num):
        if num[i]>max:
            max=num[i]
        i+=1
    print(max)
max()