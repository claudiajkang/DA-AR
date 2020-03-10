from sys import stdin
import itertools
read = lambda: stdin.readline().rstrip()

n = int(read())
a = list(map(int, read().split()))
allarr = list(map(list, itertools.permutations(sorted(a))))

res = 0
for arr in allarr:
    tr = 0
    for i in range(n-1):
        tr += abs(arr[i] - arr[i+1])

    res = max(res, tr)

print(res)
