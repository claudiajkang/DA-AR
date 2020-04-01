from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n, m, k = map(int, read().split())
g = [[-2] + [0] * m + [-2] for j in range(n+2)]
g[0] = [-2] * (m + 2)
g[-1] = [-2] * (m + 2)

for kk in range(k):
    a, b = map(int, read().split())
    g[a][b] = 1

res = 0
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for i in range(1, n+1):
    for j in range(1, m+1):
        if g[i][j] == 1:
            q = deque()
            dfs = deque()
            q.append([i, j])
            dfs.append([i, j])
            g[i][j] = -1

            while q:
                ci, cj = q.popleft()

                for ii, jj in p:
                    ti, tj = ci + ii, cj + jj

                    if g[ti][tj] == 1:
                        g[ti][tj] = -1
                        q.append([ti, tj])
                        dfs.append([ti, tj])

            if len(dfs) > res:
                res = len(dfs)

print(res)