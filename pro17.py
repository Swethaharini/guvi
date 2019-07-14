c,d=map(int,input().split())
l=list(map(int,input().split()))
p=0
for i in range(0,c):
    for j in range(1,c):
        if l[i]+l[j]==d and i!=j:
            p=1
            break
print("yes" if p else "no")
