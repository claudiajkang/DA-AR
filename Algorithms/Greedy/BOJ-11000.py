from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
s = []

for i in range(n):
    s.append(list(map(int, read().split())))

s.sort(key=lambda x: x[1])
s.sort(key=lambda x: x[0])

q = []
heappush(q, s[0][1])

for i in range(1, n):
    if q[0] <= s[i][0]:
        r = heappop(q)

    heappush(q, s[i][1])

print(len(q))