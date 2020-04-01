from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
g = [[-1] + [0] * m + [-1] for i in range(n+2)]
g[0] = [-1] * (m+2)
g[-1] = [-1] * (m+2)
visited = [[False] * (m+2) for i in range(n+2)]
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for i in range(1, n+1):
    g[i] = [-1] + list(map(int, list(read()))) + [-1]

for i in range(1, n+1):
    for j in range(1, m+1):
        if g[i][j] == 1 and not visited[i][j]:
            q = deque()
            visited[i][j] = True
            q.append([1, i, j])

            while q:
                c, ci, cj = q.popleft()

                for ii, jj in p:
                    ti = ci + ii
                    tj = cj + jj

                    if not visited[ti][tj] and g[ti][tj] == 1:
                        visited[ti][tj] = True
                        g[ti][tj] = c + 1
                        q.append([c+1, ti, tj])

print(g[n][m])