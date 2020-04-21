from heapq import heappush, heappop
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def search(start, end):
    global n, INF, g

    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    dist[start] = 0

    q = []
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
INF = 1e9
g = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, read().split())
    g[a].append([b, c])

res = 0

for i in range(1, n + 1):
    t = search(i, x) + search(x, i)
    if t >= INF: continue
    res = max(res, t)

print(res)
