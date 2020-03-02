from sys import stdin
from collections import deque
read = lambda : stdin.readline().rstrip()
qu = lambda : deque()

N = int(read())
MAP = [[-1] * (N+2) for _ in range(N+2)]
LAND = [[-1] + [0] * N + [-1] for _ in range(N+2)]
BOUND = qu()
POINT = [[0, -1], [0, 1], [-1, 0], [1, 0]]

for i in range(1, N+1):
    T = list(map(int, read().split()))
    MAP[i] = [-1] + T + [-1]
    for j in range(1, N+1):
        if [MAP[i][j-1], MAP[i][j]] == [0, 1]:
            BOUND.append([i, j])
        elif [MAP[i][j], MAP[i][j+1]] == [1, 0]:
            BOUND.append([i, j])

LAND_NUM = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if MAP[i][j] == 1 and LAND[i][j] == 0:
            LAND_NUM += 1
            LAND[i][j] = LAND_NUM
            q = qu()
            q.append([i, j])

            while len(q):
                ci, cj = q.popleft()

                for ii, jj in POINT:
                    ti = ci + ii
                    tj = cj + jj
                    if MAP[ti][tj] == 1 and LAND[ti][tj] == 0:
                        LAND[ti][tj] = LAND_NUM
                        q.append([ti, tj])


lq = [[] for _ in range(LAND_NUM+1)]

for i, j in BOUND:
    idx = LAND[i][j]
    lq[idx].append([i, j])

res = [10000 for _ in range(LAND_NUM+1)]

for i in range(1, LAND_NUM+1):
    q = qu()
    DIST = [[0] * (N + 2) for _ in range(N + 2)]

    for ii, jj in lq[i]:
        q.append([ii, jj, 0])

    while len(q) and res[i] == 10000:
        ci, cj, cd = q.popleft()

        for ii, jj in POINT:
            ti = ci + ii
            tj = cj + jj

            if MAP[ti][tj] == 0 and DIST[ti][tj] == 0:
                DIST[ti][tj] = cd + 1
                q.append([ti, tj, cd + 1])

            elif MAP[ti][tj] == 1 and LAND[ti][tj] != i and DIST[ti][tj] == 0:
                res[i] = cd
                break

print(min(res))