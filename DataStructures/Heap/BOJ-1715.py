from sys import stdin
from heapq import heappush, heappop
read = lambda: int(stdin.readline().rstrip())

n = read()
hq = []

for i in range(n):
    heappush(hq, read())

res = 0
while len(hq) > 1:
    h1 = heappop(hq)
    h2 = heappop(hq)
    res += (h1+h2)
    if hq:
        heappush(hq, (h1+h2))

print(res)