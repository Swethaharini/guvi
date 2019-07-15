from itertools import permutations
c=input()
d=permutations(c)
for i in list(d):
    print("".join(i))
