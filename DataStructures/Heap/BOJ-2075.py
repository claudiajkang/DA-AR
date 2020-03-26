from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

n = int(read())
hq = []

for i in range(n):
    for j in map(int, read().split()):
        heappush(hq, j)

    while len(hq) > (n + n):
        heappop(hq)

r = 0
for j in range(n+1):
    if hq:
        r = heappop(hq)

print(r)