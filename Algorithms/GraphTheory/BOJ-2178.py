from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

n, m = map(int, read().split())
g = []

for i in range(n):
    g.append(list(map(int, list(read()))))

p = [[0, -1], [0, 1], [-1, 0], [1, 0]]
q = deque()
q.append([0, 0])
g[0][0] = 1

while q:
    ci, cj = q.popleft()

    for ii, jj in p:
        ti, tj = ci + ii, cj + jj
        if (ti < 0 or ti >= n) or (tj < 0 or tj >= m):
            continue

        if g[ti][tj] == 1:
            q.append([ti, tj])
            g[ti][tj] = g[ci][cj] + 1

print(g[n - 1][m - 1])
