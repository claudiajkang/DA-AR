from sys import stdin
from collections import deque

read = lambda: stdin.readline().rstrip()

M, N = map(int, read().split())
TOMA = [[-1] * (M + 2) for _ in range(N + 2)]
q = deque()
ALLTOMA = 0
POINT = [[0, -1], [0, 1], [1, 0], [-1, 0]]

for i in range(1, N + 1):
    T = list(map(int, read().split()))
    TOMA[i] = [-1] + T + [-1]
    if T.count(1) > 0:
        ALLTOMA += T.count(1)
        for j in range(1, M + 1):
            if TOMA[i][j] == 1:
                q.append([i, j, 0])

if ALLTOMA == (M * N):
    print(0)

else:
    days = 0

    while len(q):
        ci, cj, cd = q.popleft()

        for ii, jj in POINT:
            ti = ii + ci
            tj = jj + cj
            if TOMA[ti][tj] == 0:
                TOMA[ti][tj] = cd + 1
                q.append([ti, tj, cd + 1])
                days = max(days, cd + 1)

    for i in range(1, N + 1):
        if TOMA[i].count(0) > 0:
            days = -1
            break

    print(days)

