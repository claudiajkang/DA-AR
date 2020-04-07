from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
g = [[-1] * (m + 2) for i in range(n + 2)]

for i in range(1, n + 1):
    g[i] = [-1] + list(map(int, list(read()))) + [-1]

q = deque()
q.append([1, 1])
p = [[0, -1], [0, 1], [-1, 0], [1, 0]]

while q:
    ci, cj = q.popleft()

    for ii, jj in p:
        ti, tj = ii + ci, jj + cj
        if g[ti][tj] == 1:
            q.append([ti, tj])
            g[ti][tj] = g[ci][cj] + 1

print(g[n][m])
