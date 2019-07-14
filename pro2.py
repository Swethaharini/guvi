from itertools import combinations
b,c=map(int,input().split())
a=len(str(b))
lst=list(combinations(str(b),a-c))
lst=sorted(lst)
print(*lst[0],sep='')
