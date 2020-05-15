from heapq import heappush, heappop
from sys import stdin

read = lambda: stdin.readline().rstrip()


def distance(start, end):
    global g, INF, n

    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)

    dist[start] = 0
    q = []
    heappush(q, [dist[start], start])

    while q:
        cost, cur = heappop(q)

        if visited[cur]: continue
        visited[cur] = True

        for j, d in g[cur]:
            if dist[j] > dist[cur] + d:
                dist[j] = dist[cur] + d
                heappush(q, [dist[j], j])

    return dist[end]


n, e = map(int, read().split())
g = [[] for i in range(n + 1)]
INF = 1e9

for i in range(e):
    a, b, c = map(int, read().split())
    g[a].append([b, c])
    g[b].append([a, c])

a, b = map(int, read().split())

d1 = distance(1, a) + distance(a, b) + distance(b, n)
d2 = distance(1, b) + distance(b, a) + distance(a, n)

res = min(d1, d2)

print(res if res < INF else -1)
