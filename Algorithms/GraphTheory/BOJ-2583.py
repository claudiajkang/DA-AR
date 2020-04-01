from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

m, n, k = map(int, read().split())
g = [[0] * n for i in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, read().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            g[y][x] = 1

res = []
p = [[0, 1], [0, -1], [-1, 0], [1, 0]]

for i in range(m):
    for j in range(n):
        if g[i][j] == 0:
            q = deque()
            dfs = deque()
            q.append([i, j])
            dfs.append([i, j])
            g[i][j] = -1

            while q:
                ci, cj = q.popleft()

                for ii, jj in p:
                    ti, tj = ci+ii, cj + jj

                    if 0 <= ti < m and 0 <= tj < n:
                        if g[ti][tj] == 0:
                            g[ti][tj] = -1
                            q.append([ti, tj])
                            if [ti, tj] not in dfs:
                                dfs.append([ti, tj])

            res.append(len(dfs))

print(len(res))
print(' '.join(map(str, sorted(res))))
