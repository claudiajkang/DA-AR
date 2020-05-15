from collections import deque
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, m = read()
g = [[] for i in range(n + 1)]

for i in range(m):
    a, b = read()
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n + 1)
res = 0

for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        q = deque()
        q.append(i)

        while q:
            cur = q.popleft()

            for j in g[cur]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = True

        res += 1

print(res)
