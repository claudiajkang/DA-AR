from sys import stdin
import heapq
read = lambda: int(stdin.readline())

h = []
N = read()

for i in range(N):
    x = read()
    if x == 0:
        v = 0
        if len(h) > 0:
            v = heapq.heappop(h) * (-1)
        print(v)
    else:
        heapq.heappush(h, x*(-1))


