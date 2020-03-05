from sys import stdin
from collections import deque
read = lambda : stdin.readline().rstrip()

N, M = map(int, read().split())
G = [[-1] * (M+2) for _ in range(N+2)]
W = []
POINT = [[0, -1], [0, 1], [1, 0], [-1, 0]]

for i in range(1, N+1):
    G[i] = [-1] + list(map(int, list(read()))) + [-1]
    
    for j in range(1, M+1):
        if G[i][j] == 1:
            W.append([i, j])

res = []
for i in range(1, N+2):
    for j in range(1, M+2):
        if G[i][j] == 1:
            G[i][j] = 0
            DIS = [[0] * (M+2) for _ in range(N+2)]
            q = deque()
            q.append([1, 1, 1])

            while len(q):
                ci, cj, cd = q.popleft()

                for ii, jj in POINT:
                    ti = ci + ii
                    tj = cj + jj

                    if G[ti][tj] == 0 and DIS[ti][tj] == 0:
                        DIS[ti][tj] = cd + 1
                        q.append([ti, tj, cd + 1])

            G[i][j] = 1
            if DIS[N][M] != 0:
                res.append(DIS[N][M])

if len(res) == 0:
    print(-1)
else:
    print(min(res))
