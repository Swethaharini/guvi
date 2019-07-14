a=0
b=0
c=[]
v=input()
for i in v:
  if i not in c:
    c.append(i)
    b+=1
    if a<b:
       a=b
  else:
    b=0
print(a)    
