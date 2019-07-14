a=input()
m=0
n=[]
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        m=st1[i:j+1]
        l=m[::-1]
        if m==l:
            n.append(len(a)-len(l))
print(min(n))
