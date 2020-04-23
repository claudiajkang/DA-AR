from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
g = [[] for i in range(n + 1)]
r = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, read().split())
    g[a].append([b, -c])
    r[b].append(a)

visited = [False] * (n + 1)
INF = 1e9
dist = [INF] * (n + 1)

visited[n] = True
q = deque()
q.append(n)

while q:
    cur = q.popleft()

    for j in r[cur]:
        if not visited[j]:
            visited[j] = True
            q.append(j)

dist[1] = 0
prev = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for nxt, d in g[j]:
            if dist[nxt] > dist[j] + d:
                if i == n and visited[nxt]:
                    print(-1)
                    exit()

                prev[nxt] = j
                dist[nxt] = dist[j] + d

if dist[n] == INF:
    print(-1)
else:
    res = [n]

    c = n
    for i in range(1, n + 1):
        if prev[c] == 0: continue
        res.append(prev[c])
        c = prev[c]

    print(' '.join(map(str, reversed(res))))