a=int(input())
b=[]
j = list(map(int,input().split()))
c=[]
for i in j:
    if(l.count(j)>1):
        c.append(j)
if (len(c)>=2):
    d=set(c)
    print(*d)
else:
    print('unique')
