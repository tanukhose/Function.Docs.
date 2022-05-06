# Q1.Write a Python program to count the number of strings where the string length is 2     
# or more and the first and last characters are the same from a given list of strings.
#  ist=['abc', 'xyz', 'aba', '1221']
# result= 2.




a=["abc","12121","dcad"]
i=0
while i<len(a):
    j=0
    count=0
    while j<len(a[i]):
        if a[i][j]==a[i][-j]:
            count+=1
        j+=1
    i+=1
print(count)