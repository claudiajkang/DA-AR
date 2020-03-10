from sys import stdin
import heapq
read = lambda: int(stdin.readline())

n = read()
h = []

for i in range(n):
    x = read()
    if x == 0:
        v = 0
        if len(h):
            t, v = heapq.heappop(h)
        print(v)
    else:
        heapq.heappush(h, (abs(x), x))
