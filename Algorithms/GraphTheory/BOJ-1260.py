from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n, m, v = map(int, read().split())

g = [[] for i in range(n+1)]

for i in range(m):
    A, B = map(int, read().split())
    g[A].append(B)
    g[B].append(A)

for i in range(1, n+1):
    g[i] = sorted(g[i])

stack = [v]
dfs = []

while stack:
    cur = stack.pop()

    if cur not in dfs:
        dfs.append(cur)

    for i in reversed(g[cur]):
        if i not in dfs:
            stack.append(i)

q = deque()
q.append(v)
bfs = []

while q:
    cur = q.popleft()
    if cur not in bfs:
        bfs.append(cur)

    for i in g[cur]:
        if i not in bfs:
            q.append(i)

print(' '.join(map(str, dfs)))
print(' '.join(map(str, bfs)))