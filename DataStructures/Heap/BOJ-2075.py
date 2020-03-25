from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

n = int(read())
q = []

for i in range(n):
    for j in map(int, read().split()):
        heappush(q, j)

    while len(q) > (n*2):
        heappop(q)

r = 0
for j in range(n):
    r = heappop(q)

print(heappop(q) if q else r)