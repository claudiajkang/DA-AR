from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

n = int(read())
m = int(read())

g = [[] for i in range(n+1)]
visited = [False] * (n+1)
dist = [-1] * (n+1)

for i in range(m):
    u, v, w = map(int, read().split())
    g[u].append([v, w])

start, end = map(int, read().split())

q = []
dist[start] = 0
heappush(q, [0, start])

while q:
    cur = heappop(q)[1]

    if visited[cur]: continue
    visited[cur] = True

    for i in g[cur]:
        nxt = i[0]
        d = i[1]

        if dist[nxt] == -1 or dist[nxt] > dist[cur] + d:
            dist[nxt] = dist[cur] + d
            heappush(q, [dist[nxt], nxt])

print(dist[end])