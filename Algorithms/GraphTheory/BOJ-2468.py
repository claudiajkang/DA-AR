from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
g = [[] for i in range(n)]
maxh = 0
minh = 1000

for i in range(n):
    g[i] = list(map(int, read().split()))
    maxh = max(maxh, max(g[i]))
    minh = min(minh, min(g[i]))

res = [0] * (maxh + 1)
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]
for h in range(maxh + 1):
    visited = [[False] * n for k in range(n)]

    for i in range(n):
        for j in range(n):
            if g[i][j] > h and not visited[i][j]:
                visited[i][j] = True
                q = deque()
                q.append([i, j])
                res[h] += 1

                while q:
                    ci, cj = q.popleft()

                    for ii, jj in p:
                        ti = ci + ii
                        tj = cj + jj

                        if ti < 0 or tj < 0 or ti >= n or tj >= n:
                            continue

                        if g[ti][tj] > h and not visited[ti][tj]:
                            visited[ti][tj] = True
                            q.append([ti, tj])

print(max(res))
