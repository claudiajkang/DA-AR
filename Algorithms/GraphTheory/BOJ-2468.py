from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
g = [[] for i in range(n)]
maxh = 0
minh = 100

for i in range(n):
    g[i] = list(map(int, read().split()))
    if max(g[i]) > maxh: maxh = max(g[i])
    if min(g[i]) < minh: minh = min(g[i])

level = [1] * minh + [0] * (maxh - minh + 1)

for l in range(minh, maxh + 1):
    visited = [[False] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if g[i][j] > l and not visited[i][j]:
                q = deque()
                q.append([i, j])
                visited[i][j] = True
                level[l] += 1

                while q:
                    ci, cj = q.popleft()

                    for ii, jj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        ti, tj = ci + ii, cj + jj
                        if ti < 0 or ti >= n or tj < 0 or tj >= n:
                            continue

                        if g[ti][tj] > l and not visited[ti][tj]:
                            q.append([ti, tj])
                            visited[ti][tj] = True

print(max(level))
