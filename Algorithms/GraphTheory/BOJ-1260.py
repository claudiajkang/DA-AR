from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m, v = map(int, read().split())
g = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, read().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1, n + 1):
    g[i] = sorted(g[i])

dfs = []
q = deque()
q.append(v)

while q:
    cur = q.pop()
    if cur not in dfs:
        dfs.append(cur)

    for i in reversed(g[cur]):
        if i not in dfs:
            q.append(i)


print(' '.join(map(str, dfs)))

bfs = []
q = deque()
q.append(v)

while q:
    cur = q.popleft()
    if cur not in bfs:
        bfs.append(cur)

    for i in g[cur]:
        if i not in bfs:
            q.append(i)

print(' '.join(map(str, bfs)))
