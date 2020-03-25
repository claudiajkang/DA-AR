from sys import stdin
from heapq import heappush, heappop
from copy import deepcopy
read = lambda: stdin.readline().rstrip()

k, n = map(int, read().split())
arr = list(map(int, read().split()))
hq = deepcopy(arr)

for i in range(n-1):
    c = heappop(hq)
    for j in arr:
        heappush(hq, c*j)
        if c % j == 0: break

print(heappop(hq))