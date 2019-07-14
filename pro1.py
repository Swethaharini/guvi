import os
b=int(input())
lst=[]
for i in range(b):
    lst.append(input())
print(os.path.commonprefix(lst))
