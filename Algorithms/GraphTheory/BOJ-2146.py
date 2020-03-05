from collections import deque
from sys import stdin
read = lambda: stdin.readline().rstrip()

N = int(read())
MAP = [[-1] * (N+2) for _ in range(N+2)]
LAND = [[-1] + [0] * N + [-1] for _ in range(N+2)]
POINT = [[0, -1], [0, 1], [-1, 0], [1, 0]]
BOUND = deque()

for i in range(1, N + 1):
    MAP[i] = [-1] + list(map(int, read().split())) + [-1]

    for j in range(1, N + 1):
        if [MAP[i][j], MAP[i][j + 1]] == [1, 0]:
            BOUND.append([i, j])

        elif [MAP[i][j - 1], MAP[i][j]] == [0, 1]:
            BOUND.append([i, j])

ln = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if MAP[i][j] == 1 and LAND[i][j] == 0:
            ln += 1
            LAND[i][j] = ln
            q = deque()
            q.append([i, j])

            while len(q):
                ci, cj = q.popleft()

                for ii, jj in POINT:
                    ti = ci + ii
                    tj = cj + jj
                    if MAP[ti][tj] == 1 and LAND[ti][tj] == 0:
                        LAND[ti][tj] = ln
                        q.append([ti, tj])

BLAND = [[] for _ in range(ln + 1)]
RES = [10000 for _ in range(ln + 1)]

for ii, jj in BOUND:
    BLAND[LAND[ii][jj]].append([ii, jj])

for i in range(1, ln + 1):
    q = deque()
    DIS = [[-1] + [0] * N + [-1] for _ in range(N + 2)]

    for ti, tj in BLAND[i]:
        q.append([ti, tj, 0])

    while len(q):
        ci, cj, cd = q.popleft()

        for ii, jj in POINT:
            ti = ci + ii
            tj = cj + jj

            if MAP[ti][tj] == 0 and DIS[ti][tj] == 0:
                DIS[ti][tj] = cd + 1
                q.append([ti, tj, cd + 1])

            elif MAP[ti][tj] == 1 and LAND[ti][tj] != i:
                RES[i] = cd
                break

        if RES[i] != 10000:
            break

print(min(RES))
