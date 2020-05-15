from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m, k = map(int, read().split())

g = [[-1] + [0] * m + [-1] for i in range(n + 2)]

for i in range(k):
    a, b = map(int, read().split())
    g[a][b] = 1

res = 0
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if g[i][j] == 1:
            q = deque()
            q.append([i, j])
            g[i][j] = -1
            dfs = [[i, j]]

            while q:
                ci, cj = q.popleft()

                for ii, jj in p:
                    ti = ci + ii
                    tj = cj + jj

                    if g[ti][tj] == 1:
                        g[ti][tj] = -1
                        dfs.append([ti, tj])
                        q.append([ti, tj])

            if len(dfs) > res:
                res = len(dfs)

print(res)