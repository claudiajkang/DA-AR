from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n = int(read())
g = [[] for i in range(n + 1)]
h = [deque() for i in range(101)]
mh = 0

for i in range(1, n + 1):
    g[i] = [0] + list(map(int, read().split()))
    if max(g[i]) > mh:
        mh = max(g[i])

    for j in range(1, n + 1):
        h[g[i][j]].append([i, j])

res = [0] * 101

for hh in range(mh + 1):
    if len(h[hh]) == 0:
        if hh <= 1:
            res[hh] = 1
        else:
            res[hh] = res[hh - 1]
        continue

    while h[hh]:
        ci, cj = h[hh].popleft()
        g[ci][cj] = -1

    visited = [[False] * (n + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if g[i][j] > hh and not visited[i][j]:
                q = deque()
                q.append([i, j])
                area = 1
                visited[i][j] = True

                while q:
                    ci, cj = q.popleft()

                    for ii, jj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        ti = ci + ii
                        tj = cj + jj

                        if ti <= 0 or ti > n or tj <= 0 or tj > n:
                            continue

                        if (g[ti][tj] > hh) and (not visited[ti][tj]):
                            visited[ti][tj] = True
                            q.append([ti, tj])
                            area += 1

                if area:
                    res[hh] += 1

print(max(res))
