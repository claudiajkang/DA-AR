from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

t = int(read())
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for tt in range(t):
    m, n, k = map(int, read().split())
    g = [[0 for i in range(m)] for j in range(n)]

    for kk in range(k):
        x, y = map(int, read().split())
        g[y][x] = 1

    res = 0

    for y in range(n):
        for x in range(m):
            if g[y][x] == 1:
                q = deque()
                dfs = deque()
                q.append([y, x])
                g[y][x] = -1

                while q:
                    cy, cx = q.popleft()
                    if [cy, cx] not in dfs:
                        dfs.append([cy, cx])

                    for yy, xx in p:
                        ty, tx = cy + yy, cx + xx

                        if 0 <= ty < n and 0 <= tx < m:
                            if g[ty][tx] == 1 and [ty, tx] not in dfs:
                                g[ty][tx] = -1
                                q.append([ty, tx])

                if dfs:
                    res += 1

    print(res)