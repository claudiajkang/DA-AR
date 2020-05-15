from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()


def distance(start, end):
    global n, g, INF

    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    q = []

    dist[start] = 0
    heappush(q, [dist[start], start])

    while q:
        cost, cur = heappop(q)

        if visited[cur]: continue
        visited[cur] = True

        for nxt, d in g[cur]:
            if dist[nxt] > dist[cur] + d:
                dist[nxt] = dist[cur] + d
                heappush(q, [dist[nxt], nxt])

    return dist[end]


n, m, x = map(int, read().split())
g = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, read().split())
    g[a].append([b, c])

INF = 1e9

res = [0] * (n + 1)

for i in range(1, n + 1):
    res[i] = distance(i, x) + distance(x, i)

print(max(res))
