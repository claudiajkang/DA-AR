from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
g = [[] for i in range(n)]
minh = 1000
maxh = 0

for i in range(n):
    g[i] = list(map(int, read().split()))

    if min(g[i]) < minh: minh = min(g[i])
    if max(g[i]) > maxh: maxh = max(g[i])

level = [1] * (minh) + [0] * (maxh - minh + 1)

for hh in range(minh, maxh + 1):
    visited = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if g[i][j] > hh and not visited[i][j]:
                q = deque()
                q.append([i, j])
                visited[i][j] = True

                while q:
                    ci, cj = q.popleft()

                    for ii, jj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                        ti = ci + ii
                        tj = cj + jj

                        if ti < 0 or tj < 0 or tj >= n or ti >= n:
                            continue

                        if g[ti][tj] > hh and not visited[ti][tj]:
                            visited[ti][tj] = True
                            q.append([ti, tj])

                level[hh] += 1

print(max(level))
