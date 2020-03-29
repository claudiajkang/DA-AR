from sys import stdin
from collections import deque
from copy import deepcopy
read = lambda: stdin.readline().rstrip()

t = int(read())
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]
res = [0] * t

for tt in range(t):
    m, n, k = map(int, read().split())
    g = [[0] * m for i in range(n)]
    b = deque()

    for i in range(k):
        x, y = map(int, read().split())
        g[y][x] = 1
        b.append([y, x])

    for i in range(n):
        for j in range(m):
            if [i, j] in b and g[i][j] == 1:
                g[i][j] = 0
                q = deque()
                q.append([i, j])
                res[tt] += 1

                while q:
                    ci, cj = q.popleft()

                    for ii, jj in p:
                        ti = ci + ii
                        tj = cj + jj

                        if (0 <= ti < n) and (0 <= tj < m):
                            if g[ti][tj] == 1:
                                g[ti][tj] = 0
                                q.append([ti, tj])


print('\n'.join(map(str, res)))