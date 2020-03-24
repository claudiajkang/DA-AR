from sys import stdin
from heapq import heappush, heappop

n = int(stdin.readline().rstrip())
hq = []
res = 0

for i in range(n):
    heappush(hq, int(stdin.readline().rstrip()))

while len(hq) > 1:
    h1 = heappop(hq)
    h2 = 0
    if hq: h2 = heappop(hq)
    res += (h1+h2)
    if hq: heappush(hq, h1+h2)

print(res)