import heapq
from sys import stdin
read = lambda: stdin.readline().rstrip()

n = int(read())
a = []

for i in range(n):
    v = list(map(int, read().split()))

    for j in v:
        heapq.heappush(a, j)

        if len(a) > n:
            heapq.heappop(a)

print(heapq.heappop(a))
