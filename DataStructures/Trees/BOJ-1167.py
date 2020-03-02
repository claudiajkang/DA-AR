from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()


def dfs(g, start, visited):
    q = deque()
    q.append([start, 0])
    visited[start] = 0
    md = 0

    while len(q):
        ci, cd = q.popleft()

        for i, d in g[ci]:
            if visited[i] == -1:
                visited[i] = cd + d
                md = max(md, cd + d)
                q.append([i, cd + d])

    return visited.index(md), md


V = int(read())
G = [[] for _ in range(V + 1)]
visited = [-1] * (V + 1)

for i in range(1, V + 1):
    T = list(map(int, read().split()[:-1]))
    for j in range(1, len(T), 2):
        G[T[0]].append([T[j], T[j + 1]])

fmidx, fmval = dfs(G, 1, visited)

visited = [-1] * (V + 1)

tmidx, tmval = dfs(G, fmidx, visited)

print(tmval)
