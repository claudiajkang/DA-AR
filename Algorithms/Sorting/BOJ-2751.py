from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline()

n = int(read())
r = []

for i in range(n):
    heappush(r, int(read()))

for i in range(n):
    print(heappop(r))
