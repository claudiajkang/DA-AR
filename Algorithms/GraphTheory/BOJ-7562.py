from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

tt = int(read())
p = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

for t in range(tt):
    l = int(read())

    ci, cj = map(int, read().split())
    di, dj = map(int, read().split())

    if [ci, cj] == [di, dj]:
        print(0)
        continue

    g = [[0] * l for i in range(l)]

    q = deque()
    q.append([ci, cj])

    while q:
        ci, cj = q.popleft()

        if [ci, cj] == [di, dj]:
            print(g[ci][cj])
            break

        for ii, jj in p:
            ti, tj = ci + ii, cj + jj

            if (ti < 0 or ti >= l) or (tj < 0 or tj >= l):
                continue

            if g[ti][tj] == 0:
                q.append([ti, tj])
                g[ti][tj] = g[ci][cj] + 1
