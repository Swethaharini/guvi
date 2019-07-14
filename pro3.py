a,b=input().split()
r=abs(len(b)-len(a))
for k in range(len(a)):
  if(len(b)==1 and p[k] in a):
    break
  if(a[k]!=b[k]):
    r=r+1
print(r)
