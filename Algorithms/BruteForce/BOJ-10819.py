from itertools import permutations
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))
a.sort()

tlist = list(permutations(a))

res = 0
for tt in tlist:
    s = 0
    for j in range(n - 1):
        s += (abs(tt[j] - tt[j + 1]))

    res = max(res, s)

print(res)
