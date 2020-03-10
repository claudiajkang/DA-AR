from sys import stdin
import heapq
read = lambda: int(stdin.readline())

h = []
n = read()

for i in range(n):
    heapq.heappush(h, read())

if len(h) == 1:
    print(0)
    exit()

i = 1
r = 0
while len(h) > 0:
    a1 = heapq.heappop(h)
    a2 = 0
    if len(h):
        a2 = heapq.heappop(h)

    r += (a1 + a2)
    if len(h):
        heapq.heappush(h, a1+a2)

print(r)
