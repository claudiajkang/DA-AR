from sys import stdin
from heapq import heappush, heappop
read = lambda: int(stdin.readline().rstrip())

n = read()
q = []
res = 0

for i in range(n):
    heappush(q, read())

while len(q) > 1:
    h1 = heappop(q)
    h2 = 0
    if q:
        h2 = heappop(q)

    res += (h1+h2)

    if q:
        heappush(q, h1+h2)

print(res)
