from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

n = int(read())
table = [0] * (2*n)

for i in range(n):
    for j in map(int, read().split()):
        heappush(table, j)

    while len(table) > (2*n):
        heappop(table)

for i in range(n):
    heappop(table)

print(heappop(table))