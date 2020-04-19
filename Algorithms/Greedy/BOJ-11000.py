from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
time = [list(map(int, read().split())) for i in range(n)]
time.sort(key=lambda x: x[1])
time.sort(key=lambda x: x[0])

q = []
heappush(q, time[0][1])

for i in range(1, n):
    if q[0] <= time[i][0]:
        r = heappop(q)

    heappush(q, time[i][1])

print(len(q))
