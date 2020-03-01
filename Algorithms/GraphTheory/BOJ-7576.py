from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().split())
B = [[] for _ in range(N+2)]
res = 0
P = [[1, 0], [-1, 0], [0, 1], [0, -1]]
tomato = deque()
at = 0

for i in range(1, N+1):
    v = list(map(int, stdin.readline().split()))
    at += v.count(1)
    B[i] = [-1] + v + [-1]
    if v.count(1) > 0:
        for j in range(M):
            if v[j] == 1:
                tomato.append([i, j+1, 0])

if at == (M*N):
    print(0)

B[0] = [-1] * (M+2)
B[-1] = [-1] * (M+2)


while len(tomato):
    ci, cj, cd = tomato.popleft()
    for ii, jj in P:
        ti = ci + ii
        tj = cj + jj
        if B[ti][tj] == 0:
            B[ti][tj] = cd + 1
            tomato.append([ti, tj, cd + 1])
            res = max(res, cd + 1)

for i in range(1, N+1):
    if B[i][1:M+1].count(0):
        res = -1

print(res)

