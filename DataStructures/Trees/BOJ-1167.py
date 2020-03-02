from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()


def dfs(g, start):
    visited = [0] * (len(g))
    q = deque()
    q.append([start, 0])
    md = 0
    visited[start] = 1

    while len(q):
        cur, cd = q.popleft()

        for ti, td in g[cur]:
            if not visited[ti]:
                visited[ti] = cd + td
                md = max(md, cd + td)
                q.append([ti, cd + td])

    return visited.index(md), md


V = int(read())
G = [[] for _ in range(V + 1)]

for i in range(1, V + 1):
    T = list(map(int, read().split()[:-1]))
    for j in range(1, len(T), 2):
        G[T[0]].append([T[j], T[j + 1]])

first_idx, first_val = dfs(G, 1)
second_idx, second_val = dfs(G, first_idx)

print(second_val)
