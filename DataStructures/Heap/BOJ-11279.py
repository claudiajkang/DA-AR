from sys import stdin
from heapq import heappush, heappop
read = lambda: int(stdin.readline().rstrip())

n = read()
hq = []

for i in range(n):
    t = read()
    if t == 0:
        print(heappop(hq)*(-1) if hq else t)
    else:
        heappush(hq, t*(-1))
