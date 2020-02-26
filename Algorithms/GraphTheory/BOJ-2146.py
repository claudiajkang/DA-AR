from sys import stdin
from collections import deque
read = lambda : stdin.readline().rstrip()

N = int(read())
MAP = [[-1] * (N+2) for _ in range(N+2)]
LAND = [[-1] + [0] * (N+1) + [-1] for _ in range(N+2)]
LAND[0] = [-1] * (N+2)
LAND[-1] = [-1] * (N+2)
POINT = [[0, -1], [0, 1], [1, 0], [-1, 0]]
bq = []

for i in range(1, N+1):
    MAP[i] = [-1] + list(map(int, read().split())) + [-1]
    for j in range(2, N+1):
        if [MAP[i][j-1], MAP[i][j]] == [1, 0]:
            bq.append([i, j-1])
        elif [MAP[i][j-1], MAP[i][j]] == [0, 1]:
            bq.append([i, j])

ln = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if MAP[i][j] == 1 and LAND[i][j] == 0:
            q = deque()
            q.append([i, j])
            ln += 1
            LAND[i][j] = ln

            while len(q):
                ci, cj = q.popleft()

                for ii, jj in POINT:
                    ti = ci + ii
                    tj = cj + jj
                    if MAP[ti][tj] == 1 and LAND[ti][tj] == 0:
                        LAND[ti][tj] = ln
                        q.append([ti, tj])

lq = [[] for _ in range(ln+1)]

for i, j in bq:
    idx = LAND[i][j]
    lq[idx].append([i, j, 0])

res = [200 for _ in range(ln+1)]

for i in range(1, ln+1):
    q = deque()
    DIS = [[0] * (N+2) for _ in range(N+2)]
    end = 0

    for ii, jj, dd in lq[i]:
        q.append([ii, jj, dd])

    while len(q):
        ci, cj, cd = q.popleft()
        ln = LAND[ci][cj]

        for ii, jj in POINT:
            ti = ci + ii
            tj = cj + jj
            if MAP[ti][tj] == 0:
                if DIS[ti][tj] == 0:
                    DIS[ti][tj] = cd + 1
                    q.append([ti, tj, cd+1])
            elif MAP[ti][tj] == 1:
                if LAND[ti][tj] != i:
                    res[i] = min(res[i], cd)
                    break

        if res[i] != 200:
            break

print(min(res))