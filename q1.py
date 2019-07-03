a=input()
l=[]
for i in range(len(a)):
    l.append(a[i])
for i in range(len(l)-1,0,-1):
    print(l[i],end='')
print(l[0])
