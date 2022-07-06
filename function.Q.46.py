# Q47. Draw a flowchart to take a list of 7 numbers from the user, print True if the complete
# list consists of consecutive numbers with any constant difference between numbers. Print 
# False otherwise. 
# Sample Input:
# 2 4 6 8
# Sample Output:
# True
# Sample Input:
# -5 -6 -7 -8
# Sample Output:
# True
# Sample Input:
# 1 2 4 6
# Sample Output:
# False
# Sample Input:
# 3 6 9 12 16
# Sample Output:
# False


l=[1,2,3,5,7,9]
i=0
b=[]
while i<len(l)-1:
  k=l[i+1]-l[i]
  b.append(k)
  i+=1
print(b)
i=0
c=0
a=b[i]
while i<len(b):
  if b[i]==a:
    c+=1
  i+=1
if c==len(b):
  print("true")
else:
  print("false")
