e=int(input())
f=list(map(int,input().split()))
g=[]
for i in f:
  if(f.count(i)<2):
    if i not in g:
      g.append(i)
print(*g)
