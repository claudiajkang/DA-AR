from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

v, e = map(int, read().split())
k = int(read())

g = [[] for i in range(v+1)]

for i in range(e):
    tu, tv, tw = map(int, read().split())
    g[tu].append([tv, tw])

dist = [-1] * (v+1)
visited = [False] * (v+1)

q = []

dist[k] = 0
heappush(q, [0, k])

while q:
    cur = heappop(q)[1]

    if visited[cur]: continue
    visited[cur] = True

    for i in g[cur]:
        n = i[0]
        d = i[1]

        if dist[n] == -1 or dist[n] > dist[cur] + d:
            dist[n] = dist[cur] + d
            heappush(q, [dist[n], n])

for i in range(1, v+1):
    if dist[i] == -1:
        print("INF")
    else:
        print(dist[i])