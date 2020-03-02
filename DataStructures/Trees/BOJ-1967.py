from collections import deque
from sys import stdin
read = lambda : stdin.readline().rstrip()

def dfs(g, start):
    visited = [-1] * (len(g))
    q = deque()
    q.append([start, 0])
    md = 0

    while len(q):
        cur, curd = q.popleft()

        for i, d in g[cur]:
            if visited[i] == -1:
                visited[i] = curd + d
                md = max(md, curd + d)
                q.append([i, curd+d])

    return visited.index(md), md

N = int(read())
G = [[] for _ in range(N+1)]

for i in range(1, N):
    V, N, D = map(int, read().split())
    G[V].append([N, D])
    G[N].append([V, D])

fmi, fm = dfs(G, 1)
tmi, tm = dfs(G, fmi)

print(tm)

