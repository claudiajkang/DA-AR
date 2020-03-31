from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n, m, v = map(int, read().split())
g = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, read().split())
    g[a].append(b)
    g[b].append(a)

dfs = deque()
q = deque()
q.append(v)

for i in range(1, n+1):
    g[i] = sorted(g[i])

while q:
    c = q.pop()
    if c not in dfs:
        dfs.append(c)

    for i in reversed(g[c]):
        if i not in dfs:
            q.append(i)

print(' '.join(map(str, dfs)))

bfs = deque()
q = deque()
q.append(v)

while q:
    c = q.popleft()
    if c not in bfs: bfs.append(c)

    for i in g[c]:
        if i not in bfs:
            q.append(i)

print(' '.join(map(str, bfs)))