from sys import stdin
from copy import deepcopy
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

k, n = map(int, read().split())
arr = list(map(int, read().split()))
res = deepcopy(arr)

for i in range(1, n):
    cur = heappop(res)
    for j in arr:
        heappush(res, cur * j)
        if cur % j == 0: break

print(heappop(res))