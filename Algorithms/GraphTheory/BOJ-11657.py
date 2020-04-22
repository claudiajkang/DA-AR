from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
adj = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, read().split())
    adj[a].append([b, c])

minusCycle = False
INF = 1e9

dist = [INF] * (n + 1)
dist[1] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for nxt, d in adj[j]:
            if (dist[j] != INF) and (dist[nxt] > dist[j] + d):
                dist[nxt] = dist[j] + d
                if i == n:
                    minusCycle = True

if minusCycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
