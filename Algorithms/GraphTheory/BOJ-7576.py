from collections import deque
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

n, m = read()
g = [[0] * n for i in range(m)]
q = deque()
zero = 0
minus = 0

for i in range(m):
    g[i] = list(read())

    if 1 in g[i]:
        for j in range(n):
            if g[i][j] == 1:
                q.append([i, j])

    zero += g[i].count(0)
    minus += g[i].count(-1)

if len(q) + minus == (n * m):
    print(0)

else:
    res = 0

    while q:
        ci, cj = q.popleft()

        for ii, jj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ti, tj = ii + ci, jj + cj
            if (0 <= ti < m) and (0 <= tj < n):
                if g[ti][tj] == 0:
                    g[ti][tj] = g[ci][cj] + 1
                    q.append([ti, tj])
                    if g[ti][tj] > res:
                        res = g[ti][tj] - 1

    for i in range(m):
        if 0 in g[i]:
            res = -1
            break

    print(res, end="")
