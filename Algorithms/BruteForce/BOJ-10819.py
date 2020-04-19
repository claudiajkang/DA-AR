from sys import stdin
from itertools import permutations
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))
alist = list(map(list, permutations(sorted(a))))

res = 0

for i in alist:
    ts = 0
    for j in range(n-1):
        ts += abs(i[j] - i[j+1])
    res = max(res, ts)

print(res)
