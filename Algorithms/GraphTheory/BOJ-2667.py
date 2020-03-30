from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n = int(read())
maps = [[-1] + [0] * n + [-1] for i in range(n+2)]
maps[0] = [-1] * (n+2)
maps[-1] = [-1] * (n+2)

for i in range(1, n+1):
    maps[i] = [-1] + list(map(int, list(read()))) + [-1]

res = []
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for i in range(1, n+1):
    for j in range(1, n+1):
        if maps[i][j] == 1:
            dfs = deque()
            q = deque()
            q.append([i, j])
            maps[i][j] = 0

            while q:
                ci, cj = q.popleft()
                dfs.append([ci, cj])

                for ii, jj in p:
                    if maps[ci+ii][cj+jj] == 1:
                        maps[ci+ii][cj+jj] = 0
                        q.append([ci+ii, cj+jj])

            if dfs:
                res.append(len(dfs))

print(len(res))
for i in sorted(res):
    print(i)