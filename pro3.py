a,b=input().split()
r=abs(len(b)-len(a))
for l in range(len(a)):
  if(len(b)==1 and p[l] in a):
    break
  if(a[l]!=b[l]):
    r=r+1
print(r)
