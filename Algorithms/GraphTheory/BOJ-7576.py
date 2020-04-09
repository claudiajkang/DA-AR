from collections import deque
from sys import stdin

read = lambda: map(int, stdin.readline().rstrip().split())

m, n = read()
box = [[-1] * m for i in range(n)]

q = deque()
zero = 0
minus = 0

for i in range(n):
    box[i] = list(read())

    if box[i].count(1) > 0:
        for j in range(m):
            if box[i][j] == 1:
                q.append([i, j])

    zero += box[i].count(0)
    minus += box[i].count(-1)

if len(q) + minus == (m * n):
    print(0)
    exit()

p = [[0, -1], [0, 1], [-1, 0], [1, 0]]
res = 0

while q:
    ci, cj = q.popleft()

    for ii, jj in p:
        ti = ci + ii
        tj = cj + jj

        if 0 <= ti < n and 0 <= tj < m:
            if box[ti][tj] == 0:
                box[ti][tj] = box[ci][cj] + 1
                q.append([ti, tj])
                if box[ti][tj] > res:
                    res = box[ti][tj] - 1

for i in range(n):
    if box[i].count(0) > 0:
        res = -1
        break

print(res)
