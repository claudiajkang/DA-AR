from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

n = int(read())
hq = []

for i in range(n):
    for j in map(int, read().split()):
        heappush(hq, j)

    while len(hq) > n:
        heappop(hq)

print(heappop(hq))