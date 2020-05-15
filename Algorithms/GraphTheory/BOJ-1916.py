from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
m = int(read())

g = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, read().split())
    g[a].append([b, c])

start, end = map(int, read().split())

visited = [False] * (n + 1)
dist = [1e9] * (n + 1)

dist[start] = 0
q = []
heappush(q, [dist[start], start])

while q:
    cost, cur = heappop(q)

    if visited[cur]:
        continue

    visited[cur] = True

    for nxt, d in g[cur]:
        if dist[nxt] > cost + d:
            dist[nxt] = cost + d
            heappush(q, [dist[nxt], nxt])

print(dist[end])