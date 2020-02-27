from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
BOX = [[] for i in range(N+2)]
BOX[0] = [-1] * (M+2)
BOX[-1] = [-1] * (M+2)
day = 0
tomato = deque()
Point = [[-1, 0], [1, 0], [0, -1], [0, 1]]
tsum = 0

for i in range(1, N+1):
    val = list(map(int, stdin.readline().split()))
    tsum += sum(val)
    BOX[i] = [-1] + val + [-1]
    if val.count(1) > 0:
        for j in range(1, M+1):
            if BOX[i][j] == 1:
                tomato.append([i, j, 1])

if tsum == (N*M):
    print(0)

else:
    while tomato:
        ci, cj, d = tomato.popleft()

        for ii, jj in Point:
            ti = ci + ii
            tj = cj + jj
            if BOX[ti][tj] == 0:
                BOX[ti][tj] = d + 1
                day = max(day, d + 1)
                tomato.append([ti, tj, d + 1])

    for i in range(1, N+1):
        if BOX[i].count(0) >= 1:
            day = -1
            break

    if day > 0:
        day -= 1

    print(day)

