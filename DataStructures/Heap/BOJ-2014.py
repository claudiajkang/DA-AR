from sys import stdin
from copy import deepcopy
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

k, n = map(int, read().split())
arr = list(map(int, read().split()))
hq = deepcopy(arr)

for i in range(n-1):
    cur = heappop(hq)
    for j in arr:
        heappush(hq, cur * j)
        if cur % j == 0: break

print(heappop(hq))