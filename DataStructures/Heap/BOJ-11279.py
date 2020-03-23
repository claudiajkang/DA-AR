from sys import stdin
from heapq import heappush, heappop
read = lambda: int(stdin.readline().rstrip())

n = read()
hq = []

for i in range(n):
    t = read()

    if t == 0:
        if hq: print(heappop(hq)[1])
        else: print(t)

    else:
        heappush(hq, [abs(t), t])