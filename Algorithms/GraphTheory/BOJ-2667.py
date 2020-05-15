from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n = int(read())
g = [[-1] + [0] * n + [-1] for i in range(n+2)]

for i in range(1, n+1):
    g[i] = [-1] + list(map(int, list(read()))) + [-1]

res = []
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for i in range(1, n+1):
    for j in range(1, n+1):
        if g[i][j] == 1:
            q = deque()
            dfs = deque()
            q.append([i, j])
            dfs.append([i, j])

            while q:
                ci, cj = q.popleft()

                for ii, jj in p:
                    ti = ci + ii
                    tj = cj + jj

                    if g[ti][tj] == 1:
                        g[ti][tj] = -1
                        q.append([ti, tj])
                        if [ti, tj] not in dfs:
                            dfs.append([ti, tj])

            res.append(len(dfs))


print(len(res))
print('\n'.join(map(str, sorted(res))))
