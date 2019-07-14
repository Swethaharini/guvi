a=int(input())
b=[]
j = list(map(int,input().split()))
c=[]
for i in j:
    if(j.count(i)>1):
        c.append(i)
if (len(c)>=2):
    d=set(c)
    print(*d)
else:
    print('unique')
