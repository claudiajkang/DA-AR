from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
g = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, read().split())
    g[a].append(b)
    g[b].append(a)

res = 0

for i in range(1, n+1):
    if not visited[i]:
        q = deque()
        q.append(i)
        visited[i] = True
        dfs = deque()

        while q:
            c = q.popleft()
            dfs.append(c)

            for j in g[c]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = True

        res += 1

print(res)
