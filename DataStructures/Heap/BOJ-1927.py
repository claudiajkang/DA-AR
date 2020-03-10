from sys import stdin
import heapq
read = lambda: int(stdin.readline())

h = []
n = read()

for i in range(n):
    x = read()
    if x == 0:
        v = 0
        if len(h):
            v = heapq.heappop(h)
        print(v)
    else:
        heapq.heappush(h, x)
