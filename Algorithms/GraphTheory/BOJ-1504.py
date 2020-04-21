from heapq import heappush, heappop
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def search(start, end):
    global g, n, INF

    dist = [INF] * (n + 1)
    dist[start] = 0

    q = []
    heappush(q, [0, start])

    while q:
        cost, cur = heappop(q)

        if dist[cur] < cost:
            continue

        for nxt, d in g[cur]:
            if dist[nxt] > (dist[cur] + d):
                dist[nxt] = dist[cur] + d
                heappush(q, [dist[nxt], nxt])

    return dist[end]


INF = 1e9
n, e = map(int, read().split())
g = [[] for i in range(n + 1)]

for i in range(e):
    a, b, c = map(int, read().split())
    g[a].append([b, c])
    g[b].append([a, c])

v1, v2 = map(int, read().split())

d1 = search(1, v1) + search(v1, v2) + search(v2, n)
d2 = search(1, v2) + search(v2, v1) + search(v1, n)

res = min(d1, d2)
print(res if res < 1e9 else -1)
