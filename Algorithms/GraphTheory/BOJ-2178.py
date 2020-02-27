from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
MAP = [[] for _ in range(N+2)]
MAP[0] = [-1] * (M+2)
MAP[-1] = [-1] * (M+2)
q = deque()
P = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(1, N+1):
    MAP[i] = [-1] + list(map(int, list(stdin.readline().strip()))) + [-1]

for i in range(1, N+1):
    for j in range(1, M+1):
        if MAP[i][j] == 1:
            q.append([i, j, 1])

            while len(q):
                ci, cj, d = q.popleft()

                for ii, jj in P:
                    ti = ii + ci
                    tj = jj + cj
                    if MAP[ti][tj] == 1:
                        MAP[ti][tj] = d + 1
                        q.append([ti, tj, d+1])

print(MAP[N][M])
