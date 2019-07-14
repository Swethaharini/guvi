a1 = int(input())
a2 = list(map(int, input().split()))
a3 = int(len(a2)/2)
if sum(a2[:a3])//len(a2[:a3]) == sum(a2[a3:])//len(a2[a3:]):
    print('yes')
else:
    print('no')
