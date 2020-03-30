from sys import stdin
from collections import deque
read = lambda: stdin.readline().rstrip()

m, n, k = map(int, read().split())
area = [[0] * n for i in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, read().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            area[y][x] += 1


res = []
p = [[0, -1], [0, 1], [1, 0], [-1, 0]]

for i in range(m):
    for j in range(n):
        if area[i][j] == 0:
            q = deque()
            bfs = deque()
            q.append([i, j])
            area[i][j] = -1

            while q:
                ci, cj = q.popleft()

                if [ci, cj] not in bfs:
                    bfs.append([ci, cj])

                for ii, jj in p:
                    ti = ci + ii
                    tj = cj + jj

                    if 0 <= ti < m and 0 <= tj < n and area[ti][tj] == 0:
                        q.append([ti, tj])
                        area[ti][tj] = -1

            if bfs:
                res.append(len(bfs))

print(len(res))
print(' '.join(map(str, sorted(res))))