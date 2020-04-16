from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
g = [[] for i in range(n)]
maxlevel = 0

for i in range(n):
    g[i] = list(map(int, read().split()))
    maxlevel = max(maxlevel, max(g[i]))

level = [0] * (maxlevel + 2)
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for h in range(maxlevel + 2):
    visited = [[False] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if g[i][j] >= h and not visited[i][j]:
                visited[i][j] = True
                q = deque()
                q.append([i, j])
                level[h] += 1

                while q:
                    ci, cj = q.popleft()

                    for ii, jj in p:
                        ti = ci + ii
                        tj = cj + jj

                        if ti < 0 or tj < 0 or ti >= n or tj >= n:
                            continue

                        if g[ti][tj] >= h and not visited[ti][tj]:
                            visited[ti][tj] = True
                            q.append([ti, tj])

print(max(level))
