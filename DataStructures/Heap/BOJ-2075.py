import heapq
from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
h = []

mn = 0
for i in range(n):
    v = list(map(int, read().split()))
    if i == 0:
        mn = max(v)

    for j in v:
        heapq.heappush(h, int(j))

        if len(h) > n:
            v = heapq.heappop(h)

print(heapq.heappop(h))
