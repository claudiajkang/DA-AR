from sys import stdin
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
g = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, read().split())
    g[a].append([b, c])

INF = 1e9
dist = [INF] * (n + 1)

dist[1] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for nxt, d in g[j]:
            if (dist[j] != INF) and (dist[nxt] > dist[j] + d):
                if i == n:
                    print(-1)
                    exit()

                dist[nxt] = dist[j] + d

for i in range(2, n + 1):
    print(dist[i] if dist[i] < INF else -1)
