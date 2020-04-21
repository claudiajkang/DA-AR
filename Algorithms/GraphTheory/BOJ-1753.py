from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()

INF = 1e9
v, e = map(int, read().split())
k = int(read())
g = [[] for i in range(v + 1)]

for i in range(e):
    a, b, c = map(int, read().split())
    g[a].append([b, c])

visited = [False] * (v + 1)
dist = [INF] * (v + 1)

q = []
dist[k] = 0
heappush(q, [dist[k], k])

while q:
    cost, cur = heappop(q)

    if visited[cur]: continue
    visited[cur] = True

    for nexts, d in g[cur]:
        if dist[nexts] > (cost + d):
            dist[nexts] = cost + d
            heappush(q, [dist[nexts], nexts])

for i in range(1, v + 1):
    print("INF" if dist[i] == INF else dist[i])
