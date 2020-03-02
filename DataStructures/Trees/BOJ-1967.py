from sys import stdin
from collections import deque
read = lambda : stdin.readline().rstrip()

def dfs(g, start):
    visited = [0] * len(g)
    visited[start] = 1
    q = deque()
    q.append([start, 0])
    max_val = 0

    while len(q):
        ci, cd = q.popleft()

        for ti, td in g[ci]:
            if not visited[ti]:
                visited[ti] = cd + td
                max_val = max(max_val, cd + td)
                q.append([ti, cd + td])

    return visited.index(max_val), max_val


N = int(read())
G = [[] for _ in range(N+1)]

for i in range(1, N):
    V1, V2, D = map(int, read().split())
    G[V1].append([V2, D])
    G[V2].append([V1, D])

first_idx, first_val = dfs(G, 1)
second_idx, second_val = dfs(G, first_idx)

print(second_val)
