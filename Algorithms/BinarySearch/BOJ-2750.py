from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

n = int(read())
q = []

for i in range(n):
    heappush(q, int(read()))

for i in range(n):
    print(heappop(q))
