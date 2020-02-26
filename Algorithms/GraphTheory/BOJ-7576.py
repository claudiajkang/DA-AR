from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
B = [[] for i in range(N + 2)]
tv = 0
day = 0
tomato = deque()

B[0] = [-1] * (M + 2)
B[-1] = [-1] * (M + 2)

for i in range(1, N + 1):
    B[i] = list(map(int, stdin.readline().split()))
    tv += sum(B[i])
    B[i] = [-1] + B[i] + [-1]
    if B[i].count(1) > 0:
        for k in range(M+2):
            if B[i][k] == 1:
                tomato.append([i, k, 0])

if tv == (M * N):
    print(0)

else:
    Point = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    while len(tomato):
        ci, cj, d = tomato.popleft()

        for ii, jj in Point:
            ti = ci + ii
            tj = cj + jj
            if B[ti][tj] != 0:
                continue
            else:
                td = d + 1
                B[ti][tj] = td
                if td > day:
                    day = td
                tomato.append([ti, tj, td])

    for i in range(1, N + 1):
        if B[i].count(0) > 0:
            day = -1
            break

    print(day)
