from collections import deque
from sys import stdin

read = lambda: stdin.readline().rstrip()

T = int(read())
p = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]

for tt in range(T):
    l = int(read())
    g = [[0] * l for i in range(l)]

    ci, cj = map(int, read().split())
    di, dj = map(int, read().split())

    if [ci, cj] == [di, dj]:
        print(0)
        continue

    q = deque()
    q.append([ci, cj])
    g[ci][cj] = 0
    end = False

    while q:
        ci, cj = q.popleft()

        for ii, jj in p:
            ti, tj = ci + ii, cj + jj

            if ti == di and tj == dj:
                print(g[ci][cj] + 1)
                end = True
                break

            if (ti < 0 or ti >= l) or (tj < 0 or tj >= l):
                continue

            if g[ti][tj] == 0:
                g[ti][tj] = g[ci][cj] + 1
                q.append([ti, tj])

        if end:
            break
