from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
G = [[] for _ in range(N+2)]
G[0] = [-1] * (M+2)
G[-1] = [-1] * (M+2)
P = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(1, N+1):
    G[i] = [-1] + list(map(int, list(stdin.readline().strip()))) + [-1]

route = deque()
route.append([1, 1, 1])

while len(route):
    ci, cj, d = route.popleft()

    for ii, jj in P:
        ti = ii + ci
        tj = jj + cj
        if G[ti][tj] == 1:
            G[ti][tj] = d + 1
            route.append([ti, tj, d+1])

print(G[N][M])