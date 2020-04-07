from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

tt = int(read())
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for t in range(tt):
    m, n, k = map(int, read().split())

    g = [[0] * m for i in range(n)]

    for i in range(k):
        a, b = map(int, read().split())
        g[b][a] = 1

    res = 0

    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                g[i][j] = -1
                q = deque()
                q.append([i, j])

                while q:
                    ci, cj = q.popleft()

                    for ii, jj in p:
                        ti, tj = ii + ci, jj + cj
                        if (ti < 0 or ti >= n) or (tj < 0 or tj >= m):
                            continue

                        if g[ti][tj] == 1:
                            q.append([ti, tj])
                            g[ti][tj] = -1

                res += 1

    print(res)