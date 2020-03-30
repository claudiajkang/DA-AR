from sys import stdin
from collections import deque
read = lambda: map(int, stdin.readline().rstrip().split())

n, m = read()
g = {i: [] for i in range(1, n+1)}

for i in range(m):
    a, b = read()
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n+1)
res = 0

for i in range(1, n+1):
    if not visited[i]:
        res += 1
        dfs = deque()
        s = deque()
        s.append(i)
        visited[i] = True

        while s:
            c = s.popleft()

            if c not in dfs:
                dfs.append(c)

            for k in g[c]:
                if not visited[k]:
                    s.append(k)
                    visited[k] = True

print(res)