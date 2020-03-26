from sys import stdin
from heapq import heappush, heappop
from copy import deepcopy
read = lambda: map(int, stdin.readline().rstrip().split())

k, n = read()
arr = list(read())
hq = deepcopy(arr)
cur = 0

for i in range(n):
    cur = heappop(hq)
    for j in arr:
        heappush(hq, (cur*j))
        if cur % j == 0: break

print(cur)