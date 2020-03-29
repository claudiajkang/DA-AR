from sys import stdin
from copy import deepcopy
from collections import deque
read = lambda: stdin.readline().rstrip()

n, m, k = map(int, read().split())
maps = [[-1] + [0] * m + [-1] for i in range(n + 2)]
maps[0] = [-1] * (m + 2)
maps[-1] = [-1] * (m + 2)

visited = deepcopy(maps)

for i in range(k):
    x, y = map(int, read().split())
    maps[x][y] = 1

res = 0

p = [[0, 1], [0, -1], [-1, 0], [1, 0]]

for i in range(1, n+1):
    for j in range(1, m+1):
        if maps[i][j] == 1 and visited[i][j] == 0:
            dq = deque()
            dq.append([i, j])
            visited[i][j] = 1
            dfs = list()

            while dq:
                ci, cj = dq.popleft()

                dfs.append([ci, cj])

                for ii, jj in p:
                    ti = ci + ii
                    tj = cj + jj

                    if maps[ti][tj] == 1 and visited[ti][tj] == 0:
                        dq.append([ti, tj])
                        visited[ti][tj] = 1

            if len(dfs) > res:
                res = len(dfs)

print(res)