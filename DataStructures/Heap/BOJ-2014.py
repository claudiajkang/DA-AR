from sys import stdin
from heapq import heappush, heappop
import copy
read = lambda: stdin.readline().rstrip()

k, n = map(int, read().split())
un = list(map(int, read().split()))
hq = copy.deepcopy(un)
res = 0

for i in range(n-1):
    c = heappop(hq)
    for j in un:
        heappush(hq, c*j)
        if c % j == 0:
            break

print(heappop(hq))