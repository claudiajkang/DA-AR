from heapq import heappush, heappop
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
read = lambda: stdin.readline().rstrip()


def dijkstra(s, e):
    global g, n, INF

    q = []
    dist = [INF] * (n + 1)
    dist[s] = 0
    heappush(q, [0, s])

    while q:
        cost, cur = heappop(q)

        if dist[cur] < cost: continue

        for nxt, d in g[cur]:
            if dist[nxt] > dist[cur] + d:
                dist[nxt] = dist[cur] + d
                heappush(q, [dist[nxt], nxt])

    return dist[e]


INF = 1e9
n, e = map(int, read().split())
g = [[] for i in range(n + 1)]

for i in range(e):
    tu, tv, tw = map(int, read().split())
    g[tu].append([tv, tw])
    g[tv].append([tu, tw])

a, b = map(int, read().split())

d1 = dijkstra(1, a) + dijkstra(a, b) + dijkstra(b, n)
d2 = dijkstra(1, b) + dijkstra(b, a) + dijkstra(a, n)

res = min(d1, d2)
print(res if res < INF else -1)
